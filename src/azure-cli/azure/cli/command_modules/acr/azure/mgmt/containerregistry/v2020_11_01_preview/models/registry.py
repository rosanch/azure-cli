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

from .resource import Resource


class Registry(Resource):
    """An object that represents a container registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: Required. The location of the resource. This cannot be
     changed after the resource is created.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :ivar system_data: Metadata pertaining to creation and last modification
     of the resource.
    :vartype system_data: ~containerregistry.models.SystemData
    :param sku: Required. The SKU of the container registry.
    :type sku: ~containerregistry.models.Sku
    :param identity: The identity of the container registry.
    :type identity: ~containerregistry.models.IdentityProperties
    :ivar login_server: The URL that can be used to log into the container
     registry.
    :vartype login_server: str
    :ivar creation_date: The creation date of the container registry in
     ISO8601 format.
    :vartype creation_date: datetime
    :ivar provisioning_state: The provisioning state of the container registry
     at the time the operation was called. Possible values include: 'Creating',
     'Updating', 'Deleting', 'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~containerregistry.models.ProvisioningState
    :ivar status: The status of the container registry at the time the
     operation was called.
    :vartype status: ~containerregistry.models.Status
    :param admin_user_enabled: The value that indicates whether the admin user
     is enabled. Default value: False .
    :type admin_user_enabled: bool
    :param storage_account: The properties of the storage account for the
     container registry. Only applicable to Classic SKU.
    :type storage_account: ~containerregistry.models.StorageAccountProperties
    :param network_rule_set: The network rule set for a container registry.
    :type network_rule_set: ~containerregistry.models.NetworkRuleSet
    :param policies: The policies for a container registry.
    :type policies: ~containerregistry.models.Policies
    :param encryption: The encryption settings of container registry.
    :type encryption: ~containerregistry.models.EncryptionProperty
    :param data_endpoint_enabled: Enable a single data endpoint per region for
     serving data.
    :type data_endpoint_enabled: bool
    :ivar data_endpoint_host_names: List of host names that will serve data
     when dataEndpointEnabled is true.
    :vartype data_endpoint_host_names: list[str]
    :ivar private_endpoint_connections: List of private endpoint connections
     for a container registry.
    :vartype private_endpoint_connections:
     list[~containerregistry.models.PrivateEndpointConnection]
    :param public_network_access: Whether or not public network access is
     allowed for the container registry. Possible values include: 'Enabled',
     'Disabled'. Default value: "Enabled" .
    :type public_network_access: str or
     ~containerregistry.models.PublicNetworkAccess
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'system_data': {'readonly': True},
        'sku': {'required': True},
        'login_server': {'readonly': True},
        'creation_date': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'status': {'readonly': True},
        'data_endpoint_host_names': {'readonly': True},
        'private_endpoint_connections': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'system_data': {'key': 'systemData', 'type': 'SystemData'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'identity': {'key': 'identity', 'type': 'IdentityProperties'},
        'login_server': {'key': 'properties.loginServer', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'status': {'key': 'properties.status', 'type': 'Status'},
        'admin_user_enabled': {'key': 'properties.adminUserEnabled', 'type': 'bool'},
        'storage_account': {'key': 'properties.storageAccount', 'type': 'StorageAccountProperties'},
        'network_rule_set': {'key': 'properties.networkRuleSet', 'type': 'NetworkRuleSet'},
        'policies': {'key': 'properties.policies', 'type': 'Policies'},
        'encryption': {'key': 'properties.encryption', 'type': 'EncryptionProperty'},
        'data_endpoint_enabled': {'key': 'properties.dataEndpointEnabled', 'type': 'bool'},
        'data_endpoint_host_names': {'key': 'properties.dataEndpointHostNames', 'type': '[str]'},
        'private_endpoint_connections': {'key': 'properties.privateEndpointConnections', 'type': '[PrivateEndpointConnection]'},
        'public_network_access': {'key': 'properties.publicNetworkAccess', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Registry, self).__init__(**kwargs)
        self.sku = kwargs.get('sku', None)
        self.identity = kwargs.get('identity', None)
        self.login_server = None
        self.creation_date = None
        self.provisioning_state = None
        self.status = None
        self.admin_user_enabled = kwargs.get('admin_user_enabled', False)
        self.storage_account = kwargs.get('storage_account', None)
        self.network_rule_set = kwargs.get('network_rule_set', None)
        self.policies = kwargs.get('policies', None)
        self.encryption = kwargs.get('encryption', None)
        self.data_endpoint_enabled = kwargs.get('data_endpoint_enabled', None)
        self.data_endpoint_host_names = None
        self.private_endpoint_connections = None
        self.public_network_access = kwargs.get('public_network_access', "Enabled")
