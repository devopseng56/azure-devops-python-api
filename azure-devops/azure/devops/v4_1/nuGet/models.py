﻿# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class BatchOperationData(Model):
    """BatchOperationData.

    """

    _attribute_map = {
    }

    def __init__(self):
        super(BatchOperationData, self).__init__()


class JsonPatchOperation(Model):
    """JsonPatchOperation.

    :param from_: The path to copy from for the Move/Copy operation.
    :type from_: str
    :param op: The patch operation
    :type op: object
    :param path: The path for the operation
    :type path: str
    :param value: The value for the operation. This is either a primitive or a JToken.
    :type value: object
    """

    _attribute_map = {
        'from_': {'key': 'from', 'type': 'str'},
        'op': {'key': 'op', 'type': 'object'},
        'path': {'key': 'path', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'}
    }

    def __init__(self, from_=None, op=None, path=None, value=None):
        super(JsonPatchOperation, self).__init__()
        self.from_ = from_
        self.op = op
        self.path = path
        self.value = value


class MinimalPackageDetails(Model):
    """MinimalPackageDetails.

    :param id: Package name.
    :type id: str
    :param version: Package version.
    :type version: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, id=None, version=None):
        super(MinimalPackageDetails, self).__init__()
        self.id = id
        self.version = version


class NuGetPackagesBatchRequest(Model):
    """NuGetPackagesBatchRequest.

    :param data: Data required to perform the operation. This is optional based on the type of the operation. Use BatchPromoteData if performing a promote operation.
    :type data: :class:`BatchOperationData <azure.devops.v4_1.nuGet.models.BatchOperationData>`
    :param operation: Type of operation that needs to be performed on packages.
    :type operation: object
    :param packages: The packages onto which the operation will be performed.
    :type packages: list of :class:`MinimalPackageDetails <azure.devops.v4_1.nuGet.models.MinimalPackageDetails>`
    """

    _attribute_map = {
        'data': {'key': 'data', 'type': 'BatchOperationData'},
        'operation': {'key': 'operation', 'type': 'object'},
        'packages': {'key': 'packages', 'type': '[MinimalPackageDetails]'}
    }

    def __init__(self, data=None, operation=None, packages=None):
        super(NuGetPackagesBatchRequest, self).__init__()
        self.data = data
        self.operation = operation
        self.packages = packages


class NuGetPackageVersionDeletionState(Model):
    """NuGetPackageVersionDeletionState.

    :param deleted_date:
    :type deleted_date: datetime
    :param name:
    :type name: str
    :param version:
    :type version: str
    """

    _attribute_map = {
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, deleted_date=None, name=None, version=None):
        super(NuGetPackageVersionDeletionState, self).__init__()
        self.deleted_date = deleted_date
        self.name = name
        self.version = version


class NuGetRecycleBinPackageVersionDetails(Model):
    """NuGetRecycleBinPackageVersionDetails.

    :param deleted: Setting to false will undo earlier deletion and restore the package to feed.
    :type deleted: bool
    """

    _attribute_map = {
        'deleted': {'key': 'deleted', 'type': 'bool'}
    }

    def __init__(self, deleted=None):
        super(NuGetRecycleBinPackageVersionDetails, self).__init__()
        self.deleted = deleted


class Package(Model):
    """Package.

    :param _links:
    :type _links: :class:`ReferenceLinks <azure.devops.v4_1.nuGet.models.ReferenceLinks>`
    :param deleted_date: If and when the package was deleted
    :type deleted_date: datetime
    :param id:
    :type id: str
    :param name: The display name of the package
    :type name: str
    :param permanently_deleted_date: If and when the package was permanently deleted.
    :type permanently_deleted_date: datetime
    :param version: The version of the package
    :type version: str
    """

    _attribute_map = {
        '_links': {'key': '_links', 'type': 'ReferenceLinks'},
        'deleted_date': {'key': 'deletedDate', 'type': 'iso-8601'},
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'permanently_deleted_date': {'key': 'permanentlyDeletedDate', 'type': 'iso-8601'},
        'version': {'key': 'version', 'type': 'str'}
    }

    def __init__(self, _links=None, deleted_date=None, id=None, name=None, permanently_deleted_date=None, version=None):
        super(Package, self).__init__()
        self._links = _links
        self.deleted_date = deleted_date
        self.id = id
        self.name = name
        self.permanently_deleted_date = permanently_deleted_date
        self.version = version


class PackageVersionDetails(Model):
    """PackageVersionDetails.

    :param listed: Indicates the listing state of a package
    :type listed: bool
    :param views: The view to which the package version will be added
    :type views: :class:`JsonPatchOperation <azure.devops.v4_1.nuGet.models.JsonPatchOperation>`
    """

    _attribute_map = {
        'listed': {'key': 'listed', 'type': 'bool'},
        'views': {'key': 'views', 'type': 'JsonPatchOperation'}
    }

    def __init__(self, listed=None, views=None):
        super(PackageVersionDetails, self).__init__()
        self.listed = listed
        self.views = views


class ReferenceLinks(Model):
    """ReferenceLinks.

    :param links: The readonly view of the links.  Because Reference links are readonly, we only want to expose them as read only.
    :type links: dict
    """

    _attribute_map = {
        'links': {'key': 'links', 'type': '{object}'}
    }

    def __init__(self, links=None):
        super(ReferenceLinks, self).__init__()
        self.links = links


class BatchListData(BatchOperationData):
    """BatchListData.

    :param listed: The desired listed status for the package versions.
    :type listed: bool
    """

    _attribute_map = {
        'listed': {'key': 'listed', 'type': 'bool'}
    }

    def __init__(self, listed=None):
        super(BatchListData, self).__init__()
        self.listed = listed


__all__ = [
    'BatchOperationData',
    'JsonPatchOperation',
    'MinimalPackageDetails',
    'NuGetPackagesBatchRequest',
    'NuGetPackageVersionDeletionState',
    'NuGetRecycleBinPackageVersionDetails',
    'Package',
    'PackageVersionDetails',
    'ReferenceLinks',
    'BatchListData',
]
