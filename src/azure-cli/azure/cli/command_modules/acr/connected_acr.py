# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from enum import Enum
from msrest.exceptions import ValidationError
from knack.log import get_logger
from knack.util import CLIError
from azure.cli.core.commands import LongRunningOperation
from azure.core.exceptions import ResourceNotFoundError
from azure.cli.core.commands.client_factory import get_subscription_id
from ._client_factory import cf_acr_registries, cf_acr_tokens, cf_acr_scope_maps
from ._utils import (
    get_registry_by_name,
    validate_managed_registry,
    user_confirmation,
    create_default_scope_map,
    get_token_from_id,
    get_scope_map_from_id,
    parse_actions_from_repositories,
    parse_repositories_from_actions
)

class ConnectedRegistryModes(Enum):
    MIRROR = 'mirror'
    REGISTRY = 'registry'

DEFAULT_GATEWAY_SCOPE = ['config/read', 'config/write', 'messages/read', 'messages/write']
REPO_SCOPES_BY_MODE = {
    ConnectedRegistryModes.MIRROR.value: ['content/read', 'metadata/read'],
    ConnectedRegistryModes.REGISTRY.value: ['content/read', 'content/write', 'content/delete',
                                            'metadata/read', 'metadata/write']
}
SYNC_SCOPE_MAP_NAME = "{}-sync-scope-map"
SYNC_TOKEN_NAME = "{}-sync-token"
REPOSITORY = "repositories/"
GATEWAY = "gateway/"

logger = get_logger(__name__)


def acr_connected_acr_create(cmd,
                             client,
                             registry_name,
                             connected_acr_name,
                             repositories,
                             client_token_ids=None,
                             resource_group_name=None,
                             mode=None,
                             parent=None,
                             sync_schedule=None,
                             sync_message_ttl=None,
                             sync_window=None,
                             log_level=None,
                             sync_audit_logs_enabled=True):

    registry, resource_group_name = get_registry_by_name(
        cmd.cli_ctx, registry_name, resource_group_name)
    subscription_id = get_subscription_id(cmd.cli_ctx)

    if parent:
        try:
            parent = acr_connected_acr_show(cmd, client, parent, registry_name, resource_group_name)
        except ResourceNotFoundError as e:
            raise CLIError("The parent connected registry '{}' could not be found.".format(parent))
        if parent.mode.lower() != ConnectedRegistryModes.REGISTRY.value and parent.mode.lower() != mode.lower():
            raise CLIError("Cannot create the connected registry '{}' with mode '{}'".format(connected_acr_name, mode) +
                           "when the connected registry parent '{}' has mode '{}'.".format(registry_name, parent.mode) +
                           "For more information on connected registries, please visit https://aka.ms/acr/onprem.")

        _update_parent_sync_token(cmd, resource_group_name, registry_name,
                                  connected_acr_name, parent.parent.sync_properties.token_id)
        sync_token_id = _create_sync_token(cmd, resource_group_name, registry_name,
                                           connected_acr_name, repositories, mode)
    else:
        sync_token_id = _create_sync_token(cmd, resource_group_name, registry_name,
                                           connected_acr_name, repositories, mode)

    from .azure.mgmt.containerregistry.v2020_11_01_preview.models import ConnectedRegistry, LoggingProperties, ParentProperties, SyncProperties
#    ConnectedRegistry, LoggingProperties, SyncProperties, ParentProperties = cmd.get_models(
#        'ConnectedRegistry', 'LoggingProperties', 'SyncProperties', 'ParentProperties')
    connected_acr_create_parameters = ConnectedRegistry(
        provisioning_state=None,
        mode=mode,
        parent=ParentProperties(
            id=parent.id if parent else None,
            sync_properties=SyncProperties(
                token_id=sync_token_id,
                schedule=sync_schedule,
                message_ttl=sync_message_ttl,
                sync_window=sync_window
            )
        ),
        client_token_ids=client_token_ids,
        logging=LoggingProperties(
            log_level=log_level,
            audit_log_status='Enabled' if sync_audit_logs_enabled else 'Disabled'
        )
    )

    if not registry.data_endpoint_enabled:
        from .custom import acr_update_custom
        acr_update_custom(cmd, cf_acr_registries(cmd.cli_ctx), data_endpoint_enabled=True)

    try:
        return client.create(subscription_id=subscription_id,
                             resource_group_name=resource_group_name,
                             registry_name=registry_name,
                             connected_registry_name=connected_acr_name,
                             connected_registry_create_parameters=connected_acr_create_parameters)
    except Exception as e:
        # Delete the previously created sync scope map. TODO Should I remove the scopeMap from the parent?
        scope_map_client = cf_acr_scope_maps(cmd.cli_ctx)
        scope_map_client.delete(resource_group_name, registry_name, SYNC_SCOPE_MAP_NAME.format(connected_acr_name))
        raise CLIError(e)


def acr_connected_acr_update(cmd,
                             client,
                             registry_name,
                             connected_acr_name,
                             add_client_token_ids=None,
                             remove_client_token_ids=None,
                             add_repository=None,
                             remove_repository=None,
                             resource_group_name=None,
                             sync_schedule=None,
                             sync_window=None,
                             log_level=None,
                             sync_message_ttl=None,
                             sync_audit_logs_enabled=None):

    _, resource_group_name = validate_managed_registry(
        cmd, registry_name, resource_group_name)

    current_connected_acr = acr_connected_acr_show(cmd, client, connected_acr_name, registry_name, resource_group_name)

    # Add or remove from the current client token id list
    add_client_token_set = set(add_client_token_ids) if add_client_token_ids else set()
    remove_client_token_set = set(remove_client_token_ids) if remove_client_token_ids else set()
    duplicate_client_token = set.intersection(add_client_token_set, remove_client_token_set)
    if duplicate_client_token:
        errors = sorted(map(lambda action: action[action.find('/') + 1:], duplicate_client_token))
        raise CLIError(
            'Update ambiguity. Duplicate client token ids were provided with ' +
            '--add-client-token-ids and --remove-client-token-ids arguments.\n{}'.format(errors))

    from .azure.mgmt.containerregistry.v2020_11_01_preview.models import ConnectedRegistryUpdateParameters, SyncProperties, LoggingProperties
#    ConnectedRegistryUpdateParameters, SyncProperties, LoggingProperties = cmd.get_models(
#                'ConnectedRegistryUpdateParameters', 'SyncProperties', 'LoggingProperties')
    connected_acr_update_parameters = ConnectedRegistryUpdateParameters(
        sync_properties=SyncProperties(
            token_id=current_connected_acr.parent.sync_properties.token_id,
            schedule=sync_schedule,
            message_ttl=sync_message_ttl,
            sync_window=sync_window
        ),
        logging=LoggingProperties(
            log_level=log_level,
            audit_log_status=sync_audit_logs_enabled if sync_audit_logs_enabled is not None else \
                            current_connected_acr.logging.audit_log_status
        ),
        client_token_ids=list(
            set(current_connected_acr.client_token_ids).
            union(add_client_token_set).
            difference(remove_client_token_set)
        )
    )

    # Add or remove the repo permissions from the sync token scope map id
    if add_repository or remove_repository:
        _ = _update_sync_token_scope_map(cmd, resource_group_name, registry_name, connected_acr_name,
                                         current_connected_acr.parent.sync_properties.token_id,
                                         current_connected_acr.mode, add_repository, remove_repository)
    try:
        return client.update(resource_group_name=resource_group_name,
                             registry_name=registry_name,
                             connected_registry_name=connected_acr_name,
                             connected_registry_update_parameters=connected_acr_update_parameters)
    except ValidationError as e:
        raise CLIError(e)


def acr_connected_acr_delete(cmd,
                             client,
                             connected_acr_name,
                             registry_name,
                             yes=False,
                             resource_group_name=None):

    _, resource_group_name = validate_managed_registry(
        cmd, registry_name, resource_group_name)

    #TODO disable tokens?
    user_confirmation("Are you sure you want to delete the Connected Registry '{}' from '{}'?".format(
        connected_acr_name, registry_name), yes)
    try:
        return client.delete(resource_group_name, registry_name, connected_acr_name)
    except ValidationError as e:
        raise CLIError(e)


def acr_connected_acr_deactivate(cmd,
                                 client,
                                 connected_acr_name,
                                 registry_name,
                                 resource_group_name=None):
    _, resource_group_name = validate_managed_registry(
        cmd, registry_name, resource_group_name)
    subscription_id = get_subscription_id(cmd.cli_ctx)
    return client.deactivate(subscription_id=subscription_id,
                             resource_group_name=resource_group_name,
                             registry_name=registry_name,
                             connected_registry_name=connected_acr_name)


def acr_connected_acr_list(cmd,
                           client,
                           registry_name,
                           parent=None,
                           cascading=False,
                           resource_group_name=None):
    _, resource_group_name = validate_managed_registry(
        cmd, registry_name, resource_group_name)
    connected_acr_list = list(client.list(resource_group_name, registry_name))
    result = []
    if not cascading:
        if parent:
            result = [registry for registry in connected_acr_list \
                if registry.parent.id is not None and registry.parent.id.endswith(parent)]
        else:
            result = [registry for registry in connected_acr_list if not registry.parent.id]
    elif parent:
        family_tree = {}
        for registry in connected_acr_list:
            family_tree[registry.id] = {
                "registry": registry,
                "childs": []
            }
            if registry.name == parent:
                root_parent_id = registry.id
        for registry in connected_acr_list:
            parent_id = registry.parent.id
            if parent_id and not parent_id.isspace():
                family_tree[parent_id]["childs"].append(registry.id)
        result = _get_descendancy(family_tree, root_parent_id)
    else:
        result = connected_acr_list
    return result


def acr_connected_acr_show(cmd,
                           client,
                           connected_acr_name,
                           registry_name,
                           resource_group_name=None):
    _, resource_group_name = validate_managed_registry(
        cmd, registry_name, resource_group_name)
    return client.get(resource_group_name, registry_name, connected_acr_name)


def acr_connected_acr_list_client_tokens(cmd,
                                         client,
                                         connected_acr_name,
                                         registry_name,
                                         resource_group_name=None):
    _, resource_group_name = validate_managed_registry(
        cmd, registry_name, resource_group_name)
    current_connected_acr = acr_connected_acr_show(cmd, client, connected_acr_name, registry_name, resource_group_name)
    result = []
    for token_id in current_connected_acr.client_token_ids:
        token = get_token_from_id(cmd, token_id)
        result.append(token)
    return result


def _create_sync_token(cmd,
                       resource_group_name,
                       registry_name,
                       connected_acr_name,
                       repositories,
                       mode):
    token_client = cf_acr_tokens(cmd.cli_ctx)

    mode = mode.lower()
    if not any(option for option in ConnectedRegistryModes if option.value == mode):
        raise CLIError("usage error: --mode supports only 'registry' and 'mirror' values.")
    repository_actions_list = [[repo] + REPO_SCOPES_BY_MODE[mode] for repo in repositories]
    gateway_actions_list = [[connected_acr_name] + DEFAULT_GATEWAY_SCOPE]
    try:
        message = "Created by connected registry sync token: {}"
        scope_map_id = create_default_scope_map(cmd, resource_group_name, registry_name,
                                                SYNC_SCOPE_MAP_NAME.format(connected_acr_name),
                                                repository_actions_list, gateway_actions_list,
                                                message.format(connected_acr_name))

        Token = cmd.get_models('Token')
        poller = token_client.create(
            resource_group_name,
            registry_name,
            SYNC_TOKEN_NAME.format(connected_acr_name),
            Token(
                scope_map_id=scope_map_id,
                status="enabled"
            )
        )

        token = LongRunningOperation(cmd.cli_ctx)(poller)
        return token.id
    except ValidationError as e:
        raise CLIError(e)


def _get_descendancy(family_tree, parent_id):
    childs = family_tree[parent_id]['childs']
    result = []
    for child_id in childs:
        result = [family_tree[child_id]["registry"]]
        descendancy = _get_descendancy(family_tree, child_id)
        if descendancy:
            result.extend(descendancy)
    return result


def _update_parent_sync_token(cmd,
                              resource_group_name,
                              registry_name,
                              connected_acr_name,
                              parent_sync_token_id):
    from .scope_map import acr_scope_map_update
    scope_map_client = cf_acr_scope_maps(cmd.cli_ctx)
    sync_token = get_token_from_id(cmd, parent_sync_token_id)
    scope_map_name = sync_token.scope_map_id.split('/scopeMaps/')[1]
    gateway_actions_list = [[connected_acr_name] + DEFAULT_GATEWAY_SCOPE]

    acr_scope_map_update(cmd, scope_map_client,
                         registry_name,
                         scope_map_name,
                         resource_group_name=resource_group_name,
                         add_gateway=gateway_actions_list)


def _update_sync_token_scope_map(cmd,
                                 resource_group_name,
                                 registry_name,
                                 connected_acr_name,
                                 sync_token_id,
                                 mode,
                                 add_repository=None,
                                 remove_repository=None):
    scope_map_client = cf_acr_scope_maps(cmd.cli_ctx)
    sync_token = get_token_from_id(cmd, sync_token_id)
    current_scope_map = get_scope_map_from_id(cmd, sync_token.scope_map_id)
    current_actions = current_scope_map.actions
    add_repo_set = set(add_repository) if add_repository else set()
    remove_repo_set = set(remove_repository) if remove_repository else set()
    duplicate_repos = set.intersection(add_repo_set, remove_repo_set)
    if duplicate_repos:
        errors = sorted(map(lambda action: action[action.find('/') + 1:], duplicate_repos))
        raise CLIError(
            'Update ambiguity. Duplicate repositories were provided with ' +
            '--add-repository and --remove-repository arguments.\n{}'.format(errors))

    repositories = parse_repositories_from_actions(current_actions)
    repositories = list(set(repositories).union(add_repo_set).difference(remove_repo_set))
    if not repositories:
        raise CLIError("Update blocked: all repository would be removed from the connected" +
                       "registry '{}'.The connected registry needs to ".format(connected_acr_name) +
                       "have access to at least one repository")
    repository_actions_list = [[repo] + REPO_SCOPES_BY_MODE[mode] for repo in repositories]
    actions_list = [repo for repo in current_actions if repo.startswith(GATEWAY)]
    actions_list += parse_actions_from_repositories(repository_actions_list)

    try:
        return scope_map_client.update(
            resource_group_name,
            registry_name,
            current_scope_map.name,
            current_scope_map.description,
            actions_list
        )
    except ValidationError as e:
        raise CLIError(e)
