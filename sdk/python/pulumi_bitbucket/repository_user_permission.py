# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['RepositoryUserPermissionArgs', 'RepositoryUserPermission']

@pulumi.input_type
class RepositoryUserPermissionArgs:
    def __init__(__self__, *,
                 permission: pulumi.Input[str],
                 repo_slug: pulumi.Input[str],
                 user_id: pulumi.Input[str],
                 workspace: pulumi.Input[str]):
        """
        The set of arguments for constructing a RepositoryUserPermission resource.
        :param pulumi.Input[str] permission: Permissions can be one of `read`, `write`, `none`, and `admin`.
        :param pulumi.Input[str] repo_slug: The repository slug.
        :param pulumi.Input[str] user_id: The UUID of the user.
        :param pulumi.Input[str] workspace: The workspace id.
        """
        pulumi.set(__self__, "permission", permission)
        pulumi.set(__self__, "repo_slug", repo_slug)
        pulumi.set(__self__, "user_id", user_id)
        pulumi.set(__self__, "workspace", workspace)

    @property
    @pulumi.getter
    def permission(self) -> pulumi.Input[str]:
        """
        Permissions can be one of `read`, `write`, `none`, and `admin`.
        """
        return pulumi.get(self, "permission")

    @permission.setter
    def permission(self, value: pulumi.Input[str]):
        pulumi.set(self, "permission", value)

    @property
    @pulumi.getter(name="repoSlug")
    def repo_slug(self) -> pulumi.Input[str]:
        """
        The repository slug.
        """
        return pulumi.get(self, "repo_slug")

    @repo_slug.setter
    def repo_slug(self, value: pulumi.Input[str]):
        pulumi.set(self, "repo_slug", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        """
        The UUID of the user.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter
    def workspace(self) -> pulumi.Input[str]:
        """
        The workspace id.
        """
        return pulumi.get(self, "workspace")

    @workspace.setter
    def workspace(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace", value)


@pulumi.input_type
class _RepositoryUserPermissionState:
    def __init__(__self__, *,
                 permission: Optional[pulumi.Input[str]] = None,
                 repo_slug: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 workspace: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RepositoryUserPermission resources.
        :param pulumi.Input[str] permission: Permissions can be one of `read`, `write`, `none`, and `admin`.
        :param pulumi.Input[str] repo_slug: The repository slug.
        :param pulumi.Input[str] user_id: The UUID of the user.
        :param pulumi.Input[str] workspace: The workspace id.
        """
        if permission is not None:
            pulumi.set(__self__, "permission", permission)
        if repo_slug is not None:
            pulumi.set(__self__, "repo_slug", repo_slug)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)
        if workspace is not None:
            pulumi.set(__self__, "workspace", workspace)

    @property
    @pulumi.getter
    def permission(self) -> Optional[pulumi.Input[str]]:
        """
        Permissions can be one of `read`, `write`, `none`, and `admin`.
        """
        return pulumi.get(self, "permission")

    @permission.setter
    def permission(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "permission", value)

    @property
    @pulumi.getter(name="repoSlug")
    def repo_slug(self) -> Optional[pulumi.Input[str]]:
        """
        The repository slug.
        """
        return pulumi.get(self, "repo_slug")

    @repo_slug.setter
    def repo_slug(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repo_slug", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[str]]:
        """
        The UUID of the user.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter
    def workspace(self) -> Optional[pulumi.Input[str]]:
        """
        The workspace id.
        """
        return pulumi.get(self, "workspace")

    @workspace.setter
    def workspace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace", value)


class RepositoryUserPermission(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 permission: Optional[pulumi.Input[str]] = None,
                 repo_slug: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 workspace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Bitbucket Repository User Permission Resource.

        This allows you set explicit user permission for a repository.

        OAuth2 Scopes: `repository:admin`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_bitbucket as bitbucket

        example = bitbucket.RepositoryUserPermission("example",
            workspace="example",
            repo_slug=bitbucket_repository["example"]["name"],
            user_id="user-id",
            permission="read")
        ```

        ## Import

        Repository User Permissions can be imported using their `workspace:repo-slug:user-id` ID, e.g.

        ```sh
         $ pulumi import bitbucket:index/repositoryUserPermission:RepositoryUserPermission example workspace:repo-slug:user-id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] permission: Permissions can be one of `read`, `write`, `none`, and `admin`.
        :param pulumi.Input[str] repo_slug: The repository slug.
        :param pulumi.Input[str] user_id: The UUID of the user.
        :param pulumi.Input[str] workspace: The workspace id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RepositoryUserPermissionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Bitbucket Repository User Permission Resource.

        This allows you set explicit user permission for a repository.

        OAuth2 Scopes: `repository:admin`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_bitbucket as bitbucket

        example = bitbucket.RepositoryUserPermission("example",
            workspace="example",
            repo_slug=bitbucket_repository["example"]["name"],
            user_id="user-id",
            permission="read")
        ```

        ## Import

        Repository User Permissions can be imported using their `workspace:repo-slug:user-id` ID, e.g.

        ```sh
         $ pulumi import bitbucket:index/repositoryUserPermission:RepositoryUserPermission example workspace:repo-slug:user-id
        ```

        :param str resource_name: The name of the resource.
        :param RepositoryUserPermissionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepositoryUserPermissionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 permission: Optional[pulumi.Input[str]] = None,
                 repo_slug: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 workspace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RepositoryUserPermissionArgs.__new__(RepositoryUserPermissionArgs)

            if permission is None and not opts.urn:
                raise TypeError("Missing required property 'permission'")
            __props__.__dict__["permission"] = permission
            if repo_slug is None and not opts.urn:
                raise TypeError("Missing required property 'repo_slug'")
            __props__.__dict__["repo_slug"] = repo_slug
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
            if workspace is None and not opts.urn:
                raise TypeError("Missing required property 'workspace'")
            __props__.__dict__["workspace"] = workspace
        super(RepositoryUserPermission, __self__).__init__(
            'bitbucket:index/repositoryUserPermission:RepositoryUserPermission',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            permission: Optional[pulumi.Input[str]] = None,
            repo_slug: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None,
            workspace: Optional[pulumi.Input[str]] = None) -> 'RepositoryUserPermission':
        """
        Get an existing RepositoryUserPermission resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] permission: Permissions can be one of `read`, `write`, `none`, and `admin`.
        :param pulumi.Input[str] repo_slug: The repository slug.
        :param pulumi.Input[str] user_id: The UUID of the user.
        :param pulumi.Input[str] workspace: The workspace id.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RepositoryUserPermissionState.__new__(_RepositoryUserPermissionState)

        __props__.__dict__["permission"] = permission
        __props__.__dict__["repo_slug"] = repo_slug
        __props__.__dict__["user_id"] = user_id
        __props__.__dict__["workspace"] = workspace
        return RepositoryUserPermission(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def permission(self) -> pulumi.Output[str]:
        """
        Permissions can be one of `read`, `write`, `none`, and `admin`.
        """
        return pulumi.get(self, "permission")

    @property
    @pulumi.getter(name="repoSlug")
    def repo_slug(self) -> pulumi.Output[str]:
        """
        The repository slug.
        """
        return pulumi.get(self, "repo_slug")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        The UUID of the user.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter
    def workspace(self) -> pulumi.Output[str]:
        """
        The workspace id.
        """
        return pulumi.get(self, "workspace")

