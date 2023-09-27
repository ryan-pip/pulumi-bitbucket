# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetGroupMembersResult',
    'AwaitableGetGroupMembersResult',
    'get_group_members',
    'get_group_members_output',
]

@pulumi.output_type
class GetGroupMembersResult:
    """
    A collection of values returned by getGroupMembers.
    """
    def __init__(__self__, id=None, members=None, slug=None, workspace=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if members and not isinstance(members, list):
            raise TypeError("Expected argument 'members' to be a list")
        pulumi.set(__self__, "members", members)
        if slug and not isinstance(slug, str):
            raise TypeError("Expected argument 'slug' to be a str")
        pulumi.set(__self__, "slug", slug)
        if workspace and not isinstance(workspace, str):
            raise TypeError("Expected argument 'workspace' to be a str")
        pulumi.set(__self__, "workspace", workspace)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def members(self) -> Sequence[str]:
        return pulumi.get(self, "members")

    @property
    @pulumi.getter
    def slug(self) -> str:
        return pulumi.get(self, "slug")

    @property
    @pulumi.getter
    def workspace(self) -> str:
        return pulumi.get(self, "workspace")


class AwaitableGetGroupMembersResult(GetGroupMembersResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGroupMembersResult(
            id=self.id,
            members=self.members,
            slug=self.slug,
            workspace=self.workspace)


def get_group_members(slug: Optional[str] = None,
                      workspace: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGroupMembersResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['slug'] = slug
    __args__['workspace'] = workspace
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('bitbucket:index/getGroupMembers:getGroupMembers', __args__, opts=opts, typ=GetGroupMembersResult).value

    return AwaitableGetGroupMembersResult(
        id=pulumi.get(__ret__, 'id'),
        members=pulumi.get(__ret__, 'members'),
        slug=pulumi.get(__ret__, 'slug'),
        workspace=pulumi.get(__ret__, 'workspace'))


@_utilities.lift_output_func(get_group_members)
def get_group_members_output(slug: Optional[pulumi.Input[str]] = None,
                             workspace: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGroupMembersResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...
