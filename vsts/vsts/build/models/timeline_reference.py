# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class TimelineReference(Model):
    """TimelineReference.

    :param change_id:
    :type change_id: int
    :param id:
    :type id: str
    :param url:
    :type url: str
    """

    _attribute_map = {
        'change_id': {'key': 'changeId', 'type': 'int'},
        'id': {'key': 'id', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, change_id=None, id=None, url=None):
        super(TimelineReference, self).__init__()
        self.change_id = change_id
        self.id = id
        self.url = url
