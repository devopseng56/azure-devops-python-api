﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class WorkItemTrackingClient(Client):
    """WorkItemTracking
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(WorkItemTrackingClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_behavior(self, process_id, behavior_ref_name, expand=None):
        """GetBehavior.
        [Preview API] Returns a behavior of the process.
        :param str process_id: The ID of the process
        :param str behavior_ref_name: Reference name of the behavior
        :param str expand:
        :rtype: :class:`<WorkItemBehavior> <azure.devops.v4_1.work-item-tracking.models.WorkItemBehavior>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if behavior_ref_name is not None:
            route_values['behaviorRefName'] = self._serialize.url('behavior_ref_name', behavior_ref_name, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='d1800200-f184-4e75-a5f2-ad0b04b4373e',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemBehavior', response)

    def get_behaviors(self, process_id, expand=None):
        """GetBehaviors.
        [Preview API] Returns a list of all behaviors in the process.
        :param str process_id: The ID of the process
        :param str expand:
        :rtype: [WorkItemBehavior]
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='d1800200-f184-4e75-a5f2-ad0b04b4373e',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemBehavior]', self._unwrap_collection(response))

    def get_fields(self, process_id):
        """GetFields.
        [Preview API] Returns a list of all fields in a process.
        :param str process_id: The ID of the process
        :rtype: [FieldModel]
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        response = self._send(http_method='GET',
                              location_id='7a0e7a1a-0b34-4ae0-9744-0aaffb7d0ed1',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[FieldModel]', self._unwrap_collection(response))

    def get_work_item_type_fields(self, process_id, wit_ref_name):
        """GetWorkItemTypeFields.
        [Preview API] Returns a list of all fields in a work item type.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :rtype: [FieldModel]
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='bc0ad8dc-e3f3-46b0-b06c-5bf861793196',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[FieldModel]', self._unwrap_collection(response))

    def create_process(self, create_request):
        """CreateProcess.
        [Preview API] Creates a process.
        :param :class:`<CreateProcessModel> <azure.devops.v4_1.work-item-tracking.models.CreateProcessModel>` create_request:
        :rtype: :class:`<ProcessModel> <azure.devops.v4_1.work-item-tracking.models.ProcessModel>`
        """
        content = self._serialize.body(create_request, 'CreateProcessModel')
        response = self._send(http_method='POST',
                              location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                              version='4.1-preview.1',
                              content=content)
        return self._deserialize('ProcessModel', response)

    def delete_process(self, process_type_id):
        """DeleteProcess.
        [Preview API] Removes a process of a specific ID.
        :param str process_type_id:
        """
        route_values = {}
        if process_type_id is not None:
            route_values['processTypeId'] = self._serialize.url('process_type_id', process_type_id, 'str')
        self._send(http_method='DELETE',
                   location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_process_by_id(self, process_type_id, expand=None):
        """GetProcessById.
        [Preview API] Returns a single process of a specified ID.
        :param str process_type_id:
        :param str expand:
        :rtype: :class:`<ProcessModel> <azure.devops.v4_1.work-item-tracking.models.ProcessModel>`
        """
        route_values = {}
        if process_type_id is not None:
            route_values['processTypeId'] = self._serialize.url('process_type_id', process_type_id, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ProcessModel', response)

    def get_processes(self, expand=None):
        """GetProcesses.
        [Preview API] Returns a list of all processes.
        :param str expand:
        :rtype: [ProcessModel]
        """
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                              version='4.1-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[ProcessModel]', self._unwrap_collection(response))

    def update_process(self, update_request, process_type_id):
        """UpdateProcess.
        [Preview API] Updates a process of a specific ID.
        :param :class:`<UpdateProcessModel> <azure.devops.v4_1.work-item-tracking.models.UpdateProcessModel>` update_request:
        :param str process_type_id:
        :rtype: :class:`<ProcessModel> <azure.devops.v4_1.work-item-tracking.models.ProcessModel>`
        """
        route_values = {}
        if process_type_id is not None:
            route_values['processTypeId'] = self._serialize.url('process_type_id', process_type_id, 'str')
        content = self._serialize.body(update_request, 'UpdateProcessModel')
        response = self._send(http_method='PATCH',
                              location_id='02cc6a73-5cfb-427d-8c8e-b49fb086e8af',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessModel', response)

    def add_work_item_type_rule(self, field_rule, process_id, wit_ref_name):
        """AddWorkItemTypeRule.
        [Preview API] Adds a rule to work item type in the process.
        :param :class:`<FieldRuleModel> <azure.devops.v4_1.work-item-tracking.models.FieldRuleModel>` field_rule:
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :rtype: :class:`<FieldRuleModel> <azure.devops.v4_1.work-item-tracking.models.FieldRuleModel>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        content = self._serialize.body(field_rule, 'FieldRuleModel')
        response = self._send(http_method='POST',
                              location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('FieldRuleModel', response)

    def delete_work_item_type_rule(self, process_id, wit_ref_name, rule_id):
        """DeleteWorkItemTypeRule.
        [Preview API] Removes a rule from the work item type in the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str rule_id: The ID of the rule
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if rule_id is not None:
            route_values['ruleId'] = self._serialize.url('rule_id', rule_id, 'str')
        self._send(http_method='DELETE',
                   location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                   version='4.1-preview.1',
                   route_values=route_values)

    def get_work_item_type_rule(self, process_id, wit_ref_name, rule_id):
        """GetWorkItemTypeRule.
        [Preview API] Returns a single rule in the work item type of the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str rule_id: The ID of the rule
        :rtype: :class:`<FieldRuleModel> <azure.devops.v4_1.work-item-tracking.models.FieldRuleModel>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if rule_id is not None:
            route_values['ruleId'] = self._serialize.url('rule_id', rule_id, 'str')
        response = self._send(http_method='GET',
                              location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('FieldRuleModel', response)

    def get_work_item_type_rules(self, process_id, wit_ref_name):
        """GetWorkItemTypeRules.
        [Preview API] Returns a list of all rules in the work item type of the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :rtype: [FieldRuleModel]
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[FieldRuleModel]', self._unwrap_collection(response))

    def update_work_item_type_rule(self, field_rule, process_id, wit_ref_name, rule_id):
        """UpdateWorkItemTypeRule.
        [Preview API] Updates a rule in the work item type of the process.
        :param :class:`<FieldRuleModel> <azure.devops.v4_1.work-item-tracking.models.FieldRuleModel>` field_rule:
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str rule_id: The ID of the rule
        :rtype: :class:`<FieldRuleModel> <azure.devops.v4_1.work-item-tracking.models.FieldRuleModel>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if rule_id is not None:
            route_values['ruleId'] = self._serialize.url('rule_id', rule_id, 'str')
        content = self._serialize.body(field_rule, 'FieldRuleModel')
        response = self._send(http_method='PUT',
                              location_id='76fe3432-d825-479d-a5f6-983bbb78b4f3',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('FieldRuleModel', response)

    def get_state_definition(self, process_id, wit_ref_name, state_id):
        """GetStateDefinition.
        [Preview API] Returns a single state definition in a work item type of the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str state_id: The ID of the state
        :rtype: :class:`<WorkItemStateResultModel> <azure.devops.v4_1.work-item-tracking.models.WorkItemStateResultModel>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        if state_id is not None:
            route_values['stateId'] = self._serialize.url('state_id', state_id, 'str')
        response = self._send(http_method='GET',
                              location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('WorkItemStateResultModel', response)

    def get_state_definitions(self, process_id, wit_ref_name):
        """GetStateDefinitions.
        [Preview API] Returns a list of all state definitions in a work item type of the process.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :rtype: [WorkItemStateResultModel]
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='31015d57-2dff-4a46-adb3-2fb4ee3dcec9',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemStateResultModel]', self._unwrap_collection(response))

    def get_work_item_type(self, process_id, wit_ref_name, expand=None):
        """GetWorkItemType.
        [Preview API] Returns a single work item type in a process.
        :param str process_id: The ID of the process
        :param str wit_ref_name: The reference name of the work item type
        :param str expand:
        :rtype: :class:`<WorkItemTypeModel> <azure.devops.v4_1.work-item-tracking.models.WorkItemTypeModel>`
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        if wit_ref_name is not None:
            route_values['witRefName'] = self._serialize.url('wit_ref_name', wit_ref_name, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='e2e9d1a6-432d-4062-8870-bfcb8c324ad7',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemTypeModel', response)

    def get_work_item_types(self, process_id, expand=None):
        """GetWorkItemTypes.
        [Preview API] Returns a list of all work item types in a process.
        :param str process_id: The ID of the process
        :param str expand:
        :rtype: [WorkItemTypeModel]
        """
        route_values = {}
        if process_id is not None:
            route_values['processId'] = self._serialize.url('process_id', process_id, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='e2e9d1a6-432d-4062-8870-bfcb8c324ad7',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemTypeModel]', self._unwrap_collection(response))

