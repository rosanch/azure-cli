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


class WebhookUpdateParameters(Model):
    """The parameters for updating a webhook.

    :param tags: The tags for the webhook.
    :type tags: dict[str, str]
    :param service_uri: The service URI for the webhook to post notifications.
    :type service_uri: str
    :param custom_headers: Custom headers that will be added to the webhook
     notifications.
    :type custom_headers: dict[str, str]
    :param status: The status of the webhook at the time the operation was
     called. Possible values include: 'enabled', 'disabled'
    :type status: str or
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.WebhookStatus
    :param scope: The scope of repositories where the event can be triggered.
     For example, 'foo:*' means events for all tags under repository 'foo'.
     'foo:bar' means events for 'foo:bar' only. 'foo' is equivalent to
     'foo:latest'. Empty means all events.
    :type scope: str
    :param actions: The list of actions that trigger the webhook to post
     notifications.
    :type actions: list[str or
     ~azure.mgmt.containerregistry.v2019_06_01_preview.models.WebhookAction]
    """

    _attribute_map = {
        'tags': {'key': 'tags', 'type': '{str}'},
        'service_uri': {'key': 'properties.serviceUri', 'type': 'str'},
        'custom_headers': {'key': 'properties.customHeaders', 'type': '{str}'},
        'status': {'key': 'properties.status', 'type': 'str'},
        'scope': {'key': 'properties.scope', 'type': 'str'},
        'actions': {'key': 'properties.actions', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(WebhookUpdateParameters, self).__init__(**kwargs)
        self.tags = kwargs.get('tags', None)
        self.service_uri = kwargs.get('service_uri', None)
        self.custom_headers = kwargs.get('custom_headers', None)
        self.status = kwargs.get('status', None)
        self.scope = kwargs.get('scope', None)
        self.actions = kwargs.get('actions', None)
