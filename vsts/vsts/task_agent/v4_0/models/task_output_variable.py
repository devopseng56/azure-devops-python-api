# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class TaskOutputVariable(Model):
    """TaskOutputVariable.

    :param description:
    :type description: str
    :param name:
    :type name: str
    """

    _attribute_map = {
        'description': {'key': 'description', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'}
    }

    def __init__(self, description=None, name=None):
        super(TaskOutputVariable, self).__init__()
        self.description = description
        self.name = name
