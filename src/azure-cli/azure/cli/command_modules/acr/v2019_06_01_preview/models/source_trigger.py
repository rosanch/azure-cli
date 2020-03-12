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


class SourceTrigger(Model):
    """The properties of a source based trigger.

    All required parameters must be populated in order to send to Azure.

    :param source_repository: Required. The properties that describes the
     source(code) for the task.
    :type source_repository:
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.SourceProperties
    :param source_trigger_events: Required. The source event corresponding to
     the trigger.
    :type source_trigger_events: list[str or
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.SourceTriggerEvent]
    :param status: The current status of trigger. Possible values include:
     'Disabled', 'Enabled'. Default value: "Enabled" .
    :type status: str or
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.TriggerStatus
    :param name: Required. The name of the trigger.
    :type name: str
    """

    _validation = {
        'source_repository': {'required': True},
        'source_trigger_events': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'source_repository': {'key': 'sourceRepository', 'type': 'SourceProperties'},
        'source_trigger_events': {'key': 'sourceTriggerEvents', 'type': '[str]'},
        'status': {'key': 'status', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SourceTrigger, self).__init__(**kwargs)
        self.source_repository = kwargs.get('source_repository', None)
        self.source_trigger_events = kwargs.get('source_trigger_events', None)
        self.status = kwargs.get('status', "Enabled")
        self.name = kwargs.get('name', None)
