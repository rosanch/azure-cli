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


class StatusDetailProperties(Model):
    """The status detail properties of the connected registry.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar type: The component of the connected registry corresponding to the
     status.
    :vartype type: str
    :ivar code: The code of the status.
    :vartype code: str
    :ivar description: The description of the status.
    :vartype description: str
    :ivar timestamp: The timestamp of the status.
    :vartype timestamp: datetime
    :ivar correlation_id: The correlation id of the status.
    :vartype correlation_id: str
    """

    _validation = {
        'type': {'readonly': True},
        'code': {'readonly': True},
        'description': {'readonly': True},
        'timestamp': {'readonly': True},
        'correlation_id': {'readonly': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'code': {'key': 'code', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'correlation_id': {'key': 'correlationId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(StatusDetailProperties, self).__init__(**kwargs)
        self.type = None
        self.code = None
        self.description = None
        self.timestamp = None
        self.correlation_id = None
