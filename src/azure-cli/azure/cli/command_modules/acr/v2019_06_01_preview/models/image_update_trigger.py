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


class ImageUpdateTrigger(Model):
    """The image update trigger that caused a build.

    :param id: The unique ID of the trigger.
    :type id: str
    :param timestamp: The timestamp when the image update happened.
    :type timestamp: datetime
    :param images: The list of image updates that caused the build.
    :type images:
     list[~azure.mgmt.containerregistry.v2019_06_01_preview.models.ImageDescriptor]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'timestamp': {'key': 'timestamp', 'type': 'iso-8601'},
        'images': {'key': 'images', 'type': '[ImageDescriptor]'},
    }

    def __init__(self, **kwargs):
        super(ImageUpdateTrigger, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.timestamp = kwargs.get('timestamp', None)
        self.images = kwargs.get('images', None)
