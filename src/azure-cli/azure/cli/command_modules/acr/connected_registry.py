# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.exceptions import ValidationError
from knack.log import get_logger
from knack.util import CLIError
from azure.cli.core.commands.client_factory import get_subscription_id
from ._utils import (
    get_registry_by_name,
    validate_managed_registry,
    user_confirmation
)

DEFAULT_MODE = 'registry'
DEFAULT_LOG_LEVEL = 'Info'
DEFAULT_MESSAGE_TTL = 'P2D'

logger = get_logger(__name__)


def acr_connected_registry_create(cmd,
                                  client,
                                  registry_name,
                                  connected_registry_name,
                                  repositories,
                                  resource_group_name=None,
                                  mode=DEFAULT_MODE,
                                  parent=None,
                                  sync_schedule=None,
                                  sync_window=None,
                                  disable_auto_update=False,
                                  log_level=DEFAULT_LOG_LEVEL,
                                  sync_message_ttl=DEFAULT_MESSAGE_TTL,
                                  disable_sync_audit_logs=False):

    registry, resource_group_name = get_registry_by_name(
        cmd.cli_ctx, registry_name, resource_group_name)
    subscription_id = get_subscription_id(cmd.cli_ctx)

    SyncProperties, ParentProperties = cmd.get_models(
            'SyncProperties', 'ParentProperties')
    sync_properties = SyncProperties(
        TokenId=None, #Create Token? The resource ID of the ACR token used to authenticate the connected registry to its parent during sync. 
        Schedule=sync_schedule,
        MessageTtl=sync_message_ttl,
        SyncWindow=sync_window,
        LastSyncTime=None,
        GatewayEndpoint=None
    )
    parent_properties = ParentProperties(
        Id=registry.Id,
        SyncProperties=sync_properties
    )

    TlsCertificateProperties, TlsProperties, LoginServerProperties = cmd.get_models(
            'TlsCertificateProperties', 'TlsProperties', 'LoginServerProperties')
    tls_certificate_properties = TlsCertificateProperties(
        Type=None,
        Location=None
    )
    tls_properties = TlsProperties(
        Status=None,
        Certificate=tls_certificate_properties
    )
    login_server_properties = LoginServerProperties(
        Host=None,
        Tls=tls_properties
    )

    ConnectedRegistry, LoggingProperties = cmd.get_models(
            'ConnectedRegistry', 'LoggingProperties')
    logging_properties = LoggingProperties(
        LogLevel=log_level,
        AuditLogStatus='Enabled' if disable_sync_audit_logs else 'Disabled'
    )

    connected_registry_create_parameters = ConnectedRegistry(
        ProvisioningState=None,
        Mode=mode,
        Version=None,
        LastVersionUpdateTime=None,
        ConnectionState=None,
        LastActivityTime=None,
        Parent=parent_properties,
        ClientTokenIds=None,
        LoginServer=login_server_properties,
        Logging=logging_properties,
        StatusDetails=None
    )

    try:
        return client.create(subscriptionId=subscription_id,
                             resourceGroupName=resource_group_name,
                             registryName=registry_name,
                             connectedRegistryName=connected_registry_name,
                             connected_registry=connected_registry_create_parameters)
    except ValidationError as e:
        raise CLIError(e)


def acr_connected_registry_update(cmd,
                                  client,
                                  registry_name,
                                  connected_registry_name,
                                  repositories,
                                  resource_group_name=None,
                                  mode=DEFAULT_MODE,
                                  sync_schedule=None,
                                  sync_window=None,
                                  disable_auto_update=False,
                                  next_update=None,
                                  log_level=DEFAULT_LOG_LEVEL,
                                  sync_message_ttl=DEFAULT_MESSAGE_TTL,
                                  disable_sync_audit_logs=False):

    _, resource_group_name = validate_managed_registry(
        cmd, registry_name, resource_group_name)
    subscription_id = get_subscription_id(cmd.cli_ctx)

    ConnectedRegistryUpdateProperties, SyncProperties, LoggingProperties = cmd.get_models(
            'ConnectedRegistryUpdateProperties', 'SyncProperties', 'LoggingProperties')

    sync_properties = SyncProperties(
        Schedule=sync_schedule,
        MessageTtl=sync_message_ttl,
        SyncWindow=sync_window
    )

    logging_properties = LoggingProperties(
        LogLevel=log_level,
        AuditLogStatus='Enabled' if disable_sync_audit_logs else 'Disabled'
    )

    connected_registry_update_parameters = ConnectedRegistryUpdateProperties(
        SyncProperties=sync_properties,
        Logging=mode,
        ClientTokenIds=None
    )

    try:
        return client.update(subscriptionId=subscription_id,
                             resourceGroupName=resource_group_name,
                             registryName=registry_name,
                             connectedRegistryName=connected_registry_name,
                             connected_registry=connected_registry_update_parameters)
    except ValidationError as e:
        raise CLIError(e)


def acr_connected_registry_delete(cmd,
                                  client,
                                  connected_registry_name,
                                  registry_name,
                                  yes=False,
                                  resource_group_name=None):

    _, resource_group_name = validate_managed_registry(
        cmd, registry_name, resource_group_name)
    subscription_id = get_subscription_id(cmd.cli_ctx)

    user_confirmation("Are you sure you want to delete the ConnectedRegistry '{}' from '{}'?".format(
        connected_registry_name, registry_name), yes)
    try:
        return client.delete(subscriptionId=subscription_id,
                             resource_group_name=resource_group_name,
                             registry_name=registry_name,
                             connected_registry_name=connected_registry_name)
    except ValidationError as e:
        raise CLIError(e)


def acr_connected_registry_list(cmd,
                                client,
                                registry_name,
                                parent=None,
                                cascading=False,
                                resource_group_name=None):
    _, resource_group_name = validate_managed_registry(
        cmd, registry_name, resource_group_name)
    subscription_id = get_subscription_id(cmd.cli_ctx)
    #TODO Cascading logic and different formattings.
    return client.list(subscription_id, resource_group_name, registry_name)


def acr_connected_registry_show(cmd,
                                client,
                                connected_registry_name,
                                registry_name,
                                resource_group_name=None):
    _, resource_group_name = validate_managed_registry(
        cmd, registry_name, resource_group_name)
    subscription_id = get_subscription_id(cmd.cli_ctx)
    return client.get(subscription_id, resource_group_name, registry_name, connected_registry_name)
