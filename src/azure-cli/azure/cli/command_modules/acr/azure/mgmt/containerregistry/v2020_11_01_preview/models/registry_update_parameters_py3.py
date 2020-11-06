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

from msrest.serialization import Model


class RegistryUpdateParameters(Model):
    """The parameters for updating a container registry.

    :param tags: The tags for the container registry.
    :type tags: dict[str, str]
    :param sku: The SKU of the container registry.
    :type sku: ~containerregistry.models.Sku
    :param identity: The identity of the container registry.
    :type identity: ~containerregistry.models.IdentityProperties
    :param admin_user_enabled: The value that indicates whether the admin user
     is enabled.
    :type admin_user_enabled: bool
    :param network_rule_set: The network rule set for a container registry.
    :type network_rule_set: ~containerregistry.models.NetworkRuleSet
    :param policies: The policies for a container registry.
    :type policies: ~containerregistry.models.Policies
    :param encryption: The encryption settings of container registry.
    :type encryption: ~containerregistry.models.EncryptionProperty
    :param data_endpoint_enabled: Enable a single data endpoint per region for
     serving data.
    :type data_endpoint_enabled: bool
    :param public_network_access: Whether or not public network access is
     allowed for the container registry. Possible values include: 'Enabled',
     'Disabled'
    :type public_network_access: str or
     ~containerregistry.models.PublicNetworkAccess
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'identity': {'key': 'identity', 'type': 'IdentityProperties'},
        'admin_user_enabled': {'key': 'properties.adminUserEnabled', 'type': 'bool'},
        'network_rule_set': {'key': 'properties.networkRuleSet', 'type': 'NetworkRuleSet'},
        'policies': {'key': 'properties.policies', 'type': 'Policies'},
        'encryption': {'key': 'properties.encryption', 'type': 'EncryptionProperty'},
        'data_endpoint_enabled': {'key': 'properties.dataEndpointEnabled', 'type': 'bool'},
        'public_network_access': {'key': 'properties.publicNetworkAccess', 'type': 'str'},
    }

    def __init__(self, *, tags=None, sku=None, identity=None, admin_user_enabled: bool=None, network_rule_set=None, policies=None, encryption=None, data_endpoint_enabled: bool=None, public_network_access=None, **kwargs) -> None:
        super(RegistryUpdateParameters, self).__init__(**kwargs)
        self.tags = tags
        self.sku = sku
        self.identity = identity
        self.admin_user_enabled = admin_user_enabled
        self.network_rule_set = network_rule_set
        self.policies = policies
        self.encryption = encryption
        self.data_endpoint_enabled = data_endpoint_enabled
        self.public_network_access = public_network_access
