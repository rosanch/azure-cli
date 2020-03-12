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


class RunRequest(Model):
    """The request parameters for scheduling a run.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: DockerBuildRequest, FileTaskRunRequest, TaskRunRequest,
    EncodedTaskRunRequest

    All required parameters must be populated in order to send to Azure.

    :param is_archive_enabled: The value that indicates whether archiving is
     enabled for the run or not. Default value: False .
    :type is_archive_enabled: bool
    :param agent_pool_name: The dedicated agent pool for the run.
    :type agent_pool_name: str
    :param type: Required. Constant filled by server.
    :type type: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'is_archive_enabled': {'key': 'isArchiveEnabled', 'type': 'bool'},
        'agent_pool_name': {'key': 'agentPoolName', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    _subtype_map = {
        'type': {'DockerBuildRequest': 'DockerBuildRequest', 'FileTaskRunRequest': 'FileTaskRunRequest', 'TaskRunRequest': 'TaskRunRequest', 'EncodedTaskRunRequest': 'EncodedTaskRunRequest'}
    }

    def __init__(self, *, is_archive_enabled: bool=False, agent_pool_name: str=None, **kwargs) -> None:
        super(RunRequest, self).__init__(**kwargs)
        self.is_archive_enabled = is_archive_enabled
        self.agent_pool_name = agent_pool_name
        self.type = None
