# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .proxy_resource_py3 import ProxyResource


class ConnectedRegistry(ProxyResource):
    """An object that represents a connected registry for a container registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar provisioning_state: Provisioning state of the resource. Possible
     values include: 'Creating', 'Updating', 'Deleting', 'Succeeded', 'Failed',
     'Canceled'
    :vartype provisioning_state: str or
     ~containerregistry.models.ProvisioningState
    :param mode: Required. The mode of the connected registry resource that
     indicates the permissions of the registry. Possible values include:
     'Registry', 'Mirror'
    :type mode: str or ~containerregistry.models.ConnectedRegistryMode
    :ivar version: The current version of ACR runtime on the connected
     registry.
    :vartype version: str
    :ivar last_version_update_time: The last time that the ACR runtime version
     was updated on the connected registry.
    :vartype last_version_update_time: datetime
    :ivar connection_state: The current connection state of the connected
     registry. Possible values include: 'Online', 'Offline', 'Syncing',
     'Unhealthy'
    :vartype connection_state: str or
     ~containerregistry.models.ConnectionState
    :ivar last_activity_time: The last activity time of the connected
     registry.
    :vartype last_activity_time: datetime
    :param parent: Required. The parent of the connected registry.
    :type parent: ~containerregistry.models.ParentProperties
    :param client_token_ids: The list of the ACR token resource IDs used to
     authenticate clients to the connected registry.
    :type client_token_ids: list[str]
    :param login_server: The login server properties of the connected
     registry.
    :type login_server: ~containerregistry.models.LoginServerProperties
    :param logging: The logging properties of the connected registry.
    :type logging: ~containerregistry.models.LoggingProperties
    :ivar status_details: The list of current statuses of the connected
     registry.
    :vartype status_details:
     list[~containerregistry.models.StatusDetailProperties]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'mode': {'required': True},
        'version': {'readonly': True},
        'last_version_update_time': {'readonly': True},
        'connection_state': {'readonly': True},
        'last_activity_time': {'readonly': True},
        'parent': {'required': True},
        'status_details': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'mode': {'key': 'properties.mode', 'type': 'str'},
        'version': {'key': 'properties.version', 'type': 'str'},
        'last_version_update_time': {'key': 'properties.lastVersionUpdateTime', 'type': 'iso-8601'},
        'connection_state': {'key': 'properties.connectionState', 'type': 'str'},
        'last_activity_time': {'key': 'properties.lastActivityTime', 'type': 'iso-8601'},
        'parent': {'key': 'properties.parent', 'type': 'ParentProperties'},
        'client_token_ids': {'key': 'properties.clientTokenIds', 'type': '[str]'},
        'login_server': {'key': 'properties.loginServer', 'type': 'LoginServerProperties'},
        'logging': {'key': 'properties.logging', 'type': 'LoggingProperties'},
        'status_details': {'key': 'properties.statusDetails', 'type': '[StatusDetailProperties]'},
    }

    def __init__(self, *, mode, parent, client_token_ids=None, login_server=None, logging=None, **kwargs) -> None:
        super(ConnectedRegistry, self).__init__(**kwargs)
        self.provisioning_state = None
        self.mode = mode
        self.version = None
        self.last_version_update_time = None
        self.connection_state = None
        self.last_activity_time = None
        self.parent = parent
        self.client_token_ids = client_token_ids
        self.login_server = login_server
        self.logging = logging
        self.status_details = None
