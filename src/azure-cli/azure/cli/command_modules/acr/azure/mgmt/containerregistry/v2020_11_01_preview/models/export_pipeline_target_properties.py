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


class ExportPipelineTargetProperties(Model):
    """The properties of the export pipeline target.

    All required parameters must be populated in order to send to Azure.

    :param type: The type of target for the export pipeline.
    :type type: str
    :param uri: The target uri of the export pipeline.
     When 'AzureStorageBlob':
     "https://accountName.blob.core.windows.net/containerName/blobName"
     When 'AzureStorageBlobContainer':
     "https://accountName.blob.core.windows.net/containerName"
    :type uri: str
    :param key_vault_uri: Required. They key vault secret uri to obtain the
     target storage SAS token.
    :type key_vault_uri: str
    """

    _validation = {
        'key_vault_uri': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
        'key_vault_uri': {'key': 'keyVaultUri', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ExportPipelineTargetProperties, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.uri = kwargs.get('uri', None)
        self.key_vault_uri = kwargs.get('key_vault_uri', None)
