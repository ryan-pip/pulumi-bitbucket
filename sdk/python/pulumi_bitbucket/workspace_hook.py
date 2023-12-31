# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['WorkspaceHookArgs', 'WorkspaceHook']

@pulumi.input_type
class WorkspaceHookArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 events: pulumi.Input[Sequence[pulumi.Input[str]]],
                 url: pulumi.Input[str],
                 workspace: pulumi.Input[str],
                 active: Optional[pulumi.Input[bool]] = None,
                 skip_cert_verification: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a WorkspaceHook resource.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "events", events)
        pulumi.set(__self__, "url", url)
        pulumi.set(__self__, "workspace", workspace)
        if active is not None:
            pulumi.set(__self__, "active", active)
        if skip_cert_verification is not None:
            pulumi.set(__self__, "skip_cert_verification", skip_cert_verification)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def events(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "events")

    @events.setter
    def events(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "events", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def workspace(self) -> pulumi.Input[str]:
        return pulumi.get(self, "workspace")

    @workspace.setter
    def workspace(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace", value)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter(name="skipCertVerification")
    def skip_cert_verification(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "skip_cert_verification")

    @skip_cert_verification.setter
    def skip_cert_verification(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_cert_verification", value)


@pulumi.input_type
class _WorkspaceHookState:
    def __init__(__self__, *,
                 active: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 skip_cert_verification: Optional[pulumi.Input[bool]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 uuid: Optional[pulumi.Input[str]] = None,
                 workspace: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WorkspaceHook resources.
        """
        if active is not None:
            pulumi.set(__self__, "active", active)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if events is not None:
            pulumi.set(__self__, "events", events)
        if skip_cert_verification is not None:
            pulumi.set(__self__, "skip_cert_verification", skip_cert_verification)
        if url is not None:
            pulumi.set(__self__, "url", url)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)
        if workspace is not None:
            pulumi.set(__self__, "workspace", workspace)

    @property
    @pulumi.getter
    def active(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "active")

    @active.setter
    def active(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "active", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def events(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "events")

    @events.setter
    def events(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "events", value)

    @property
    @pulumi.getter(name="skipCertVerification")
    def skip_cert_verification(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "skip_cert_verification")

    @skip_cert_verification.setter
    def skip_cert_verification(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_cert_verification", value)

    @property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)

    @property
    @pulumi.getter
    def workspace(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "workspace")

    @workspace.setter
    def workspace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace", value)


class WorkspaceHook(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 skip_cert_verification: Optional[pulumi.Input[bool]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 workspace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a WorkspaceHook resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceHookArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a WorkspaceHook resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param WorkspaceHookArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceHookArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 active: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 events: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 skip_cert_verification: Optional[pulumi.Input[bool]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 workspace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceHookArgs.__new__(WorkspaceHookArgs)

            __props__.__dict__["active"] = active
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            if events is None and not opts.urn:
                raise TypeError("Missing required property 'events'")
            __props__.__dict__["events"] = events
            __props__.__dict__["skip_cert_verification"] = skip_cert_verification
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            if workspace is None and not opts.urn:
                raise TypeError("Missing required property 'workspace'")
            __props__.__dict__["workspace"] = workspace
            __props__.__dict__["uuid"] = None
        super(WorkspaceHook, __self__).__init__(
            'bitbucket:index/workspaceHook:WorkspaceHook',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            active: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            events: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            skip_cert_verification: Optional[pulumi.Input[bool]] = None,
            url: Optional[pulumi.Input[str]] = None,
            uuid: Optional[pulumi.Input[str]] = None,
            workspace: Optional[pulumi.Input[str]] = None) -> 'WorkspaceHook':
        """
        Get an existing WorkspaceHook resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkspaceHookState.__new__(_WorkspaceHookState)

        __props__.__dict__["active"] = active
        __props__.__dict__["description"] = description
        __props__.__dict__["events"] = events
        __props__.__dict__["skip_cert_verification"] = skip_cert_verification
        __props__.__dict__["url"] = url
        __props__.__dict__["uuid"] = uuid
        __props__.__dict__["workspace"] = workspace
        return WorkspaceHook(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def active(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "active")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def events(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "events")

    @property
    @pulumi.getter(name="skipCertVerification")
    def skip_cert_verification(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "skip_cert_verification")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        return pulumi.get(self, "url")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def workspace(self) -> pulumi.Output[str]:
        return pulumi.get(self, "workspace")

