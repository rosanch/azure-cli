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


class PipelineRun(ProxyResource):
    """An object that represents a pipeline run for a container registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :ivar provisioning_state: The provisioning state of a pipeline run.
     Possible values include: 'Creating', 'Updating', 'Deleting', 'Succeeded',
     'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~containerregistry.models.ProvisioningState
    :param request: The request parameters for a pipeline run.
    :type request: ~containerregistry.models.PipelineRunRequest
    :ivar response: The response of a pipeline run.
    :vartype response: ~containerregistry.models.PipelineRunResponse
    :param force_update_tag: How the pipeline run should be forced to recreate
     even if the pipeline run configuration has not changed.
    :type force_update_tag: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'response': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'request': {'key': 'properties.request', 'type': 'PipelineRunRequest'},
        'response': {'key': 'properties.response', 'type': 'PipelineRunResponse'},
        'force_update_tag': {'key': 'properties.forceUpdateTag', 'type': 'str'},
    }

    def __init__(self, *, request=None, force_update_tag: str=None, **kwargs) -> None:
        super(PipelineRun, self).__init__(**kwargs)
        self.provisioning_state = None
        self.request = request
        self.response = None
        self.force_update_tag = force_update_tag
