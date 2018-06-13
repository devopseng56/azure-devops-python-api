# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class GraphDescriptorResult(Model):
    """GraphDescriptorResult.

    :param _links: This field contains zero or more interesting links about the graph descriptor. These links may be invoked to obtain additional relationships or more detailed information about this graph descriptor.
    :type _links: :class:`ReferenceLinks <graph.v4_1.models.ReferenceLinks>`
    :param value:
    :type value: :class:`str <graph.v4_1.models.str>`
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'value': {'key': 'value', 'type': 'str'}
    }

    def __init__(self, _links=None, value=None):
        super(GraphDescriptorResult, self).__init__()
        self._links = _links
        self.value = value
