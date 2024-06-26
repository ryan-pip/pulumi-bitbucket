# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 owner: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 is_private: Optional[pulumi.Input[bool]] = None,
                 link: Optional[pulumi.Input['ProjectLinkArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Project resource.
        :param pulumi.Input[str] key: The key used for this project
        :param pulumi.Input[str] owner: The owner of this project. Can be you or any team you have write access to.
        :param pulumi.Input[str] description: The description of the project
        :param pulumi.Input[bool] is_private: If you want to keep the project private - defaults to `true`
        :param pulumi.Input['ProjectLinkArgs'] link: A set of links to a resource related to this object. See Link Below.
        :param pulumi.Input[str] name: The name of the project
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "owner", owner)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if is_private is not None:
            pulumi.set(__self__, "is_private", is_private)
        if link is not None:
            pulumi.set(__self__, "link", link)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The key used for this project
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Input[str]:
        """
        The owner of this project. Can be you or any team you have write access to.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: pulumi.Input[str]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the project
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="isPrivate")
    def is_private(self) -> Optional[pulumi.Input[bool]]:
        """
        If you want to keep the project private - defaults to `true`
        """
        return pulumi.get(self, "is_private")

    @is_private.setter
    def is_private(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_private", value)

    @property
    @pulumi.getter
    def link(self) -> Optional[pulumi.Input['ProjectLinkArgs']]:
        """
        A set of links to a resource related to this object. See Link Below.
        """
        return pulumi.get(self, "link")

    @link.setter
    def link(self, value: Optional[pulumi.Input['ProjectLinkArgs']]):
        pulumi.set(self, "link", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the project
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _ProjectState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 has_publicly_visible_repos: Optional[pulumi.Input[bool]] = None,
                 is_private: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 link: Optional[pulumi.Input['ProjectLinkArgs']] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 uuid: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Project resources.
        :param pulumi.Input[str] description: The description of the project
        :param pulumi.Input[bool] has_publicly_visible_repos: Indicates whether the project contains publicly visible repositories. Note that private projects cannot contain public repositories.
        :param pulumi.Input[bool] is_private: If you want to keep the project private - defaults to `true`
        :param pulumi.Input[str] key: The key used for this project
        :param pulumi.Input['ProjectLinkArgs'] link: A set of links to a resource related to this object. See Link Below.
        :param pulumi.Input[str] name: The name of the project
        :param pulumi.Input[str] owner: The owner of this project. Can be you or any team you have write access to.
        :param pulumi.Input[str] uuid: The project's immutable id.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if has_publicly_visible_repos is not None:
            pulumi.set(__self__, "has_publicly_visible_repos", has_publicly_visible_repos)
        if is_private is not None:
            pulumi.set(__self__, "is_private", is_private)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if link is not None:
            pulumi.set(__self__, "link", link)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the project
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="hasPubliclyVisibleRepos")
    def has_publicly_visible_repos(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the project contains publicly visible repositories. Note that private projects cannot contain public repositories.
        """
        return pulumi.get(self, "has_publicly_visible_repos")

    @has_publicly_visible_repos.setter
    def has_publicly_visible_repos(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "has_publicly_visible_repos", value)

    @property
    @pulumi.getter(name="isPrivate")
    def is_private(self) -> Optional[pulumi.Input[bool]]:
        """
        If you want to keep the project private - defaults to `true`
        """
        return pulumi.get(self, "is_private")

    @is_private.setter
    def is_private(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_private", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The key used for this project
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def link(self) -> Optional[pulumi.Input['ProjectLinkArgs']]:
        """
        A set of links to a resource related to this object. See Link Below.
        """
        return pulumi.get(self, "link")

    @link.setter
    def link(self, value: Optional[pulumi.Input['ProjectLinkArgs']]):
        pulumi.set(self, "link", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the project
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        The owner of this project. Can be you or any team you have write access to.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        """
        The project's immutable id.
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)


class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_private: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 link: Optional[pulumi.Input[pulumi.InputType['ProjectLinkArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource allows you to manage your projects in your bitbucket team.

        OAuth2 Scopes: `project` and `project:admin`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_bitbucket as bitbucket

        devops = bitbucket.Project("devops",
            key="DEVOPS",
            owner="my-team")
        ```

        ## Import

        Repositories can be imported using their `owner/key` ID, e.g.

        ```sh
         $ pulumi import bitbucket:index/project:Project my_project my-account/project_key
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the project
        :param pulumi.Input[bool] is_private: If you want to keep the project private - defaults to `true`
        :param pulumi.Input[str] key: The key used for this project
        :param pulumi.Input[pulumi.InputType['ProjectLinkArgs']] link: A set of links to a resource related to this object. See Link Below.
        :param pulumi.Input[str] name: The name of the project
        :param pulumi.Input[str] owner: The owner of this project. Can be you or any team you have write access to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to manage your projects in your bitbucket team.

        OAuth2 Scopes: `project` and `project:admin`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_bitbucket as bitbucket

        devops = bitbucket.Project("devops",
            key="DEVOPS",
            owner="my-team")
        ```

        ## Import

        Repositories can be imported using their `owner/key` ID, e.g.

        ```sh
         $ pulumi import bitbucket:index/project:Project my_project my-account/project_key
        ```

        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_private: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 link: Optional[pulumi.Input[pulumi.InputType['ProjectLinkArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectArgs.__new__(ProjectArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["is_private"] = is_private
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            __props__.__dict__["link"] = link
            __props__.__dict__["name"] = name
            if owner is None and not opts.urn:
                raise TypeError("Missing required property 'owner'")
            __props__.__dict__["owner"] = owner
            __props__.__dict__["has_publicly_visible_repos"] = None
            __props__.__dict__["uuid"] = None
        super(Project, __self__).__init__(
            'bitbucket:index/project:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            has_publicly_visible_repos: Optional[pulumi.Input[bool]] = None,
            is_private: Optional[pulumi.Input[bool]] = None,
            key: Optional[pulumi.Input[str]] = None,
            link: Optional[pulumi.Input[pulumi.InputType['ProjectLinkArgs']]] = None,
            name: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            uuid: Optional[pulumi.Input[str]] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the project
        :param pulumi.Input[bool] has_publicly_visible_repos: Indicates whether the project contains publicly visible repositories. Note that private projects cannot contain public repositories.
        :param pulumi.Input[bool] is_private: If you want to keep the project private - defaults to `true`
        :param pulumi.Input[str] key: The key used for this project
        :param pulumi.Input[pulumi.InputType['ProjectLinkArgs']] link: A set of links to a resource related to this object. See Link Below.
        :param pulumi.Input[str] name: The name of the project
        :param pulumi.Input[str] owner: The owner of this project. Can be you or any team you have write access to.
        :param pulumi.Input[str] uuid: The project's immutable id.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ProjectState.__new__(_ProjectState)

        __props__.__dict__["description"] = description
        __props__.__dict__["has_publicly_visible_repos"] = has_publicly_visible_repos
        __props__.__dict__["is_private"] = is_private
        __props__.__dict__["key"] = key
        __props__.__dict__["link"] = link
        __props__.__dict__["name"] = name
        __props__.__dict__["owner"] = owner
        __props__.__dict__["uuid"] = uuid
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the project
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="hasPubliclyVisibleRepos")
    def has_publicly_visible_repos(self) -> pulumi.Output[bool]:
        """
        Indicates whether the project contains publicly visible repositories. Note that private projects cannot contain public repositories.
        """
        return pulumi.get(self, "has_publicly_visible_repos")

    @property
    @pulumi.getter(name="isPrivate")
    def is_private(self) -> pulumi.Output[Optional[bool]]:
        """
        If you want to keep the project private - defaults to `true`
        """
        return pulumi.get(self, "is_private")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The key used for this project
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def link(self) -> pulumi.Output['outputs.ProjectLink']:
        """
        A set of links to a resource related to this object. See Link Below.
        """
        return pulumi.get(self, "link")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the project
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        The owner of this project. Can be you or any team you have write access to.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        The project's immutable id.
        """
        return pulumi.get(self, "uuid")

