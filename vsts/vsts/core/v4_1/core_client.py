# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...vss_client import VssClient
from . import models


class CoreClient(VssClient):
    """Core
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(CoreClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '79134c72-4a58-4b42-976c-04e7115f32bf'

    def create_connected_service(self, connected_service_creation_data, project_id):
        """CreateConnectedService.
        [Preview API]
        :param :class:`<WebApiConnectedServiceDetails> <core.models.WebApiConnectedServiceDetails>` connected_service_creation_data:
        :param str project_id:
        :rtype: :class:`<WebApiConnectedService> <core.models.WebApiConnectedService>`
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str')
        }
        content = self._serialize.body(connected_service_creation_data, 'WebApiConnectedServiceDetails')
        response = self._send(http_method='POST',
                              location_id='b4f70219-e18b-42c5-abe3-98b07d35525e',
                              version='4.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WebApiConnectedService', response)

    def get_connected_service_details(self, project_id, name):
        """GetConnectedServiceDetails.
        [Preview API]
        :param str project_id:
        :param str name:
        :rtype: :class:`<WebApiConnectedServiceDetails> <core.models.WebApiConnectedServiceDetails>`
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str'),
            'name': self._serialize.url('name', name, 'str')
        }
        response = self._send(http_method='GET',
                              location_id='b4f70219-e18b-42c5-abe3-98b07d35525e',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('WebApiConnectedServiceDetails', response)

    def get_connected_services(self, project_id, kind=None):
        """GetConnectedServices.
        [Preview API]
        :param str project_id:
        :param ConnectedServiceKind kind:
        :rtype: [WebApiConnectedService]
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str')
        }
        query_parameters = {}
        if kind is not None:
            query_parameters['kind'] = self._serialize.query('kind', kind, 'ConnectedServiceKind')
        response = self._send(http_method='GET',
                              location_id='b4f70219-e18b-42c5-abe3-98b07d35525e',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[WebApiConnectedService]', response)

    def create_identity_mru(self, mru_data, mru_name):
        """CreateIdentityMru.
        [Preview API]
        :param :class:`<IdentityData> <core.models.IdentityData>` mru_data:
        :param str mru_name:
        """
        route_values = {
            'mruName': self._serialize.url('mru_name', mru_name, 'str')
        }
        content = self._serialize.body(mru_data, 'IdentityData')
        self._send(http_method='POST',
                   location_id='5ead0b70-2572-4697-97e9-f341069a783a',
                   version='4.1-preview.1',
                   route_values=route_values,
                   content=content)

    def get_identity_mru(self, mru_name):
        """GetIdentityMru.
        [Preview API]
        :param str mru_name:
        :rtype: [IdentityRef]
        """
        route_values = {
            'mruName': self._serialize.url('mru_name', mru_name, 'str')
        }
        response = self._send(http_method='GET',
                              location_id='5ead0b70-2572-4697-97e9-f341069a783a',
                              version='4.1-preview.1',
                              route_values=route_values,
                              returns_collection=True)
        return self._deserialize('[IdentityRef]', response)

    def update_identity_mru(self, mru_data, mru_name):
        """UpdateIdentityMru.
        [Preview API]
        :param :class:`<IdentityData> <core.models.IdentityData>` mru_data:
        :param str mru_name:
        """
        route_values = {
            'mruName': self._serialize.url('mru_name', mru_name, 'str')
        }
        content = self._serialize.body(mru_data, 'IdentityData')
        self._send(http_method='PATCH',
                   location_id='5ead0b70-2572-4697-97e9-f341069a783a',
                   version='4.1-preview.1',
                   route_values=route_values,
                   content=content)

    def get_team_members_with_extended_properties(self, project_id, team_id, top=None, skip=None):
        """GetTeamMembersWithExtendedProperties.
        [Preview API] Get a list of members for a specific team.
        :param str project_id: The name or ID (GUID) of the team project the team belongs to.
        :param str team_id: The name or ID (GUID) of the team .
        :param int top:
        :param int skip:
        :rtype: [TeamMember]
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str'),
            'teamId': self._serialize.url('team_id', team_id, 'str')
        }
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='294c494c-2600-4d7e-b76c-3dd50c3c95be',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TeamMember]', response)

    def get_process_by_id(self, process_id):
        """GetProcessById.
        [Preview API] Get a process by ID.
        :param str process_id: ID for a process.
        :rtype: :class:`<Process> <core.models.Process>`
        """
        route_values = {
            'processId': self._serialize.url('process_id', process_id, 'str')
        }
        response = self._send(http_method='GET',
                              location_id='93878975-88c5-4e6a-8abb-7ddd77a8a7d8',
                              version='4.1-preview.1',
                              route_values=route_values)
        return self._deserialize('Process', response)

    def get_processes(self):
        """GetProcesses.
        [Preview API] Get a list of processes.
        :rtype: [Process]
        """
        response = self._send(http_method='GET',
                              location_id='93878975-88c5-4e6a-8abb-7ddd77a8a7d8',
                              version='4.1-preview.1',
                              returns_collection=True)
        return self._deserialize('[Process]', response)

    def get_project_collection(self, collection_id):
        """GetProjectCollection.
        [Preview API] Get project collection with the specified id or name.
        :param str collection_id:
        :rtype: :class:`<TeamProjectCollection> <core.models.TeamProjectCollection>`
        """
        route_values = {
            'collectionId': self._serialize.url('collection_id', collection_id, 'str')
        }
        response = self._send(http_method='GET',
                              location_id='8031090f-ef1d-4af6-85fc-698cd75d42bf',
                              version='4.1-preview.2',
                              route_values=route_values)
        return self._deserialize('TeamProjectCollection', response)

    def get_project_collections(self, top=None, skip=None):
        """GetProjectCollections.
        [Preview API] Get project collection references for this application.
        :param int top:
        :param int skip:
        :rtype: [TeamProjectCollectionReference]
        """
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='8031090f-ef1d-4af6-85fc-698cd75d42bf',
                              version='4.1-preview.2',
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TeamProjectCollectionReference]', response)

    def get_project_history_entries(self, min_revision=None):
        """GetProjectHistoryEntries.
        [Preview API]
        :param long min_revision:
        :rtype: [ProjectInfo]
        """
        query_parameters = {}
        if min_revision is not None:
            query_parameters['minRevision'] = self._serialize.query('min_revision', min_revision, 'long')
        response = self._send(http_method='GET',
                              location_id='6488a877-4749-4954-82ea-7340d36be9f2',
                              version='4.1-preview.2',
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[ProjectInfo]', response)

    def get_project(self, project_id, include_capabilities=None, include_history=None):
        """GetProject.
        [Preview API] Get project with the specified id or name, optionally including capabilities.
        :param str project_id:
        :param bool include_capabilities: Include capabilities (such as source control) in the team project result (default: false).
        :param bool include_history: Search within renamed projects (that had such name in the past).
        :rtype: :class:`<TeamProject> <core.models.TeamProject>`
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str')
        }
        query_parameters = {}
        if include_capabilities is not None:
            query_parameters['includeCapabilities'] = self._serialize.query('include_capabilities', include_capabilities, 'bool')
        if include_history is not None:
            query_parameters['includeHistory'] = self._serialize.query('include_history', include_history, 'bool')
        response = self._send(http_method='GET',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='4.1-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TeamProject', response)

    def get_projects(self, state_filter=None, top=None, skip=None, continuation_token=None):
        """GetProjects.
        [Preview API] Get project references with the specified state
        :param object state_filter: Filter on team projects in a specific team project state (default: WellFormed).
        :param int top:
        :param int skip:
        :param str continuation_token:
        :rtype: [TeamProjectReference]
        """
        query_parameters = {}
        if state_filter is not None:
            query_parameters['stateFilter'] = self._serialize.query('state_filter', state_filter, 'object')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='4.1-preview.3',
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[TeamProjectReference]', response)

    def queue_create_project(self, project_to_create):
        """QueueCreateProject.
        [Preview API] Queue a project creation.
        :param :class:`<TeamProject> <core.models.TeamProject>` project_to_create: The project to create.
        :rtype: :class:`<OperationReference> <core.models.OperationReference>`
        """
        content = self._serialize.body(project_to_create, 'TeamProject')
        response = self._send(http_method='POST',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='4.1-preview.3',
                              content=content)
        return self._deserialize('OperationReference', response)

    def queue_delete_project(self, project_id):
        """QueueDeleteProject.
        [Preview API] Queue a project deletion.
        :param str project_id: The project id of the project to delete.
        :rtype: :class:`<OperationReference> <core.models.OperationReference>`
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str')
        }
        response = self._send(http_method='DELETE',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='4.1-preview.3',
                              route_values=route_values)
        return self._deserialize('OperationReference', response)

    def update_project(self, project_update, project_id):
        """UpdateProject.
        [Preview API] Update an existing project's name, abbreviation, or description.
        :param :class:`<TeamProject> <core.models.TeamProject>` project_update: The updates for the project.
        :param str project_id: The project id of the project to update.
        :rtype: :class:`<OperationReference> <core.models.OperationReference>`
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str')
        }
        content = self._serialize.body(project_update, 'TeamProject')
        response = self._send(http_method='PATCH',
                              location_id='603fe2ac-9723-48b9-88ad-09305aa6c6e1',
                              version='4.1-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('OperationReference', response)

    def get_project_properties(self, project_id, keys=None):
        """GetProjectProperties.
        [Preview API] Get a collection of team project properties.
        :param str project_id: The team project ID.
        :param [str] keys: A comma-delimited string of team project property names. Wildcard characters ("?" and "*") are supported. If no key is specified, all properties will be returned.
        :rtype: [ProjectProperty]
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str')
        }
        query_parameters = {}
        if keys is not None:
            keys = ",".join(keys)
            query_parameters['keys'] = self._serialize.query('keys', keys, 'str')
        response = self._send(http_method='GET',
                              location_id='4976a71a-4487-49aa-8aab-a1eda469037a',
                              version='4.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[ProjectProperty]', response)

    def set_project_properties(self, project_id, patch_document):
        """SetProjectProperties.
        [Preview API] Create, update, and delete team project properties.
        :param str project_id: The team project ID.
        :param :class:`<[JsonPatchOperation]> <core.models.[JsonPatchOperation]>` patch_document: A JSON Patch document that represents an array of property operations. See RFC 6902 for more details on JSON Patch. The accepted operation verbs are Add and Remove, where Add is used for both creating and updating properties. The path consists of a forward slash and a property name.
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str')
        }
        content = self._serialize.body(patch_document, '[JsonPatchOperation]')
        self._send(http_method='PATCH',
                   location_id='4976a71a-4487-49aa-8aab-a1eda469037a',
                   version='4.1-preview.1',
                   route_values=route_values,
                   content=content,
                   media_type='application/json-patch+json')

    def create_or_update_proxy(self, proxy):
        """CreateOrUpdateProxy.
        [Preview API]
        :param :class:`<Proxy> <core.models.Proxy>` proxy:
        :rtype: :class:`<Proxy> <core.models.Proxy>`
        """
        content = self._serialize.body(proxy, 'Proxy')
        response = self._send(http_method='PUT',
                              location_id='ec1f4311-f2b4-4c15-b2b8-8990b80d2908',
                              version='4.1-preview.2',
                              content=content)
        return self._deserialize('Proxy', response)

    def delete_proxy(self, proxy_url, site=None):
        """DeleteProxy.
        [Preview API]
        :param str proxy_url:
        :param str site:
        """
        query_parameters = {}
        if proxy_url is not None:
            query_parameters['proxyUrl'] = self._serialize.query('proxy_url', proxy_url, 'str')
        if site is not None:
            query_parameters['site'] = self._serialize.query('site', site, 'str')
        self._send(http_method='DELETE',
                   location_id='ec1f4311-f2b4-4c15-b2b8-8990b80d2908',
                   version='4.1-preview.2',
                   query_parameters=query_parameters)

    def get_proxies(self, proxy_url=None):
        """GetProxies.
        [Preview API]
        :param str proxy_url:
        :rtype: [Proxy]
        """
        query_parameters = {}
        if proxy_url is not None:
            query_parameters['proxyUrl'] = self._serialize.query('proxy_url', proxy_url, 'str')
        response = self._send(http_method='GET',
                              location_id='ec1f4311-f2b4-4c15-b2b8-8990b80d2908',
                              version='4.1-preview.2',
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[Proxy]', response)

    def get_all_teams(self, mine=None, top=None, skip=None):
        """GetAllTeams.
        [Preview API] Get a list of all teams.
        :param bool mine: If true return all the teams requesting user is member, otherwise return all the teams user has read access
        :param int top: Maximum number of teams to return.
        :param int skip: Number of teams to skip.
        :rtype: [WebApiTeam]
        """
        query_parameters = {}
        if mine is not None:
            query_parameters['$mine'] = self._serialize.query('mine', mine, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='7a4d9ee9-3433-4347-b47a-7a80f1cf307e',
                              version='4.1-preview.2',
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[WebApiTeam]', response)

    def create_team(self, team, project_id):
        """CreateTeam.
        [Preview API] Create a team in a team project.
        :param :class:`<WebApiTeam> <core.models.WebApiTeam>` team: The team data used to create the team.
        :param str project_id: The name or ID (GUID) of the team project in which to create the team.
        :rtype: :class:`<WebApiTeam> <core.models.WebApiTeam>`
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str')
        }
        content = self._serialize.body(team, 'WebApiTeam')
        response = self._send(http_method='POST',
                              location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                              version='4.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WebApiTeam', response)

    def delete_team(self, project_id, team_id):
        """DeleteTeam.
        [Preview API] Delete a team.
        :param str project_id: The name or ID (GUID) of the team project containing the team to delete.
        :param str team_id: The name of ID of the team to delete.
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str'),
            'teamId': self._serialize.url('team_id', team_id, 'str')
        }
        self._send(http_method='DELETE',
                   location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                   version='4.1-preview.2',
                   route_values=route_values)

    def get_team(self, project_id, team_id):
        """GetTeam.
        [Preview API] Get a specific team.
        :param str project_id: The name or ID (GUID) of the team project containing the team.
        :param str team_id: The name or ID (GUID) of the team.
        :rtype: :class:`<WebApiTeam> <core.models.WebApiTeam>`
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str'),
            'teamId': self._serialize.url('team_id', team_id, 'str')
        }
        response = self._send(http_method='GET',
                              location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                              version='4.1-preview.2',
                              route_values=route_values)
        return self._deserialize('WebApiTeam', response)

    def get_teams(self, project_id, mine=None, top=None, skip=None):
        """GetTeams.
        [Preview API] Get a list of teams.
        :param str project_id:
        :param bool mine: If true return all the teams requesting user is member, otherwise return all the teams user has read access
        :param int top: Maximum number of teams to return.
        :param int skip: Number of teams to skip.
        :rtype: [WebApiTeam]
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str')
        }
        query_parameters = {}
        if mine is not None:
            query_parameters['$mine'] = self._serialize.query('mine', mine, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                              version='4.1-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              returns_collection=True)
        return self._deserialize('[WebApiTeam]', response)

    def update_team(self, team_data, project_id, team_id):
        """UpdateTeam.
        [Preview API] Update a team's name and/or description.
        :param :class:`<WebApiTeam> <core.models.WebApiTeam>` team_data:
        :param str project_id: The name or ID (GUID) of the team project containing the team to update.
        :param str team_id: The name of ID of the team to update.
        :rtype: :class:`<WebApiTeam> <core.models.WebApiTeam>`
        """
        route_values = {
            'projectId': self._serialize.url('project_id', project_id, 'str'),
            'teamId': self._serialize.url('team_id', team_id, 'str')
        }
        content = self._serialize.body(team_data, 'WebApiTeam')
        response = self._send(http_method='PATCH',
                              location_id='d30a3dd1-f8ba-442a-b86a-bd0c0c383e59',
                              version='4.1-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WebApiTeam', response)

