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


class SourceRegistryCredentials(Model):
    """Describes the credential parameters for accessing the source registry.

    :param login_mode: The authentication mode which determines the source
     registry login scope. The credentials for the source registry
     will be generated using the given scope. These credentials will be used to
     login to
     the source registry during the run. Possible values include: 'None',
     'Default'
    :type login_mode: str or
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.SourceRegistryLoginMode
    """

    _attribute_map = {
        'login_mode': {'key': 'loginMode', 'type': 'str'},
    }

    def __init__(self, *, login_mode=None, **kwargs) -> None:
        super(SourceRegistryCredentials, self).__init__(**kwargs)
        self.login_mode = login_mode
