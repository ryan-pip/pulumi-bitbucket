# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['RepositoryVariableArgs', 'RepositoryVariable']

@pulumi.input_type
class RepositoryVariableArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 repository: pulumi.Input[str],
                 value: pulumi.Input[str],
                 secured: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a RepositoryVariable resource.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "repository", repository)
        pulumi.set(__self__, "value", value)
        if secured is not None:
            pulumi.set(__self__, "secured", secured)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Input[str]:
        return pulumi.get(self, "repository")

    @repository.setter
    def repository(self, value: pulumi.Input[str]):
        pulumi.set(self, "repository", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter
    def secured(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "secured")

    @secured.setter
    def secured(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "secured", value)


@pulumi.input_type
class _RepositoryVariableState:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 secured: Optional[pulumi.Input[bool]] = None,
                 uuid: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RepositoryVariable resources.
        """
        if key is not None:
            pulumi.set(__self__, "key", key)
        if repository is not None:
            pulumi.set(__self__, "repository", repository)
        if secured is not None:
            pulumi.set(__self__, "secured", secured)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "repository")

    @repository.setter
    def repository(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository", value)

    @property
    @pulumi.getter
    def secured(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "secured")

    @secured.setter
    def secured(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "secured", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class RepositoryVariable(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 secured: Optional[pulumi.Input[bool]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a RepositoryVariable resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RepositoryVariableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a RepositoryVariable resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param RepositoryVariableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RepositoryVariableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 secured: Optional[pulumi.Input[bool]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RepositoryVariableArgs.__new__(RepositoryVariableArgs)

            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            if repository is None and not opts.urn:
                raise TypeError("Missing required property 'repository'")
            __props__.__dict__["repository"] = repository
            __props__.__dict__["secured"] = secured
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = None if value is None else pulumi.Output.secret(value)
            __props__.__dict__["uuid"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["value"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(RepositoryVariable, __self__).__init__(
            'bitbucket:index/repositoryVariable:RepositoryVariable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            key: Optional[pulumi.Input[str]] = None,
            repository: Optional[pulumi.Input[str]] = None,
            secured: Optional[pulumi.Input[bool]] = None,
            uuid: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'RepositoryVariable':
        """
        Get an existing RepositoryVariable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RepositoryVariableState.__new__(_RepositoryVariableState)

        __props__.__dict__["key"] = key
        __props__.__dict__["repository"] = repository
        __props__.__dict__["secured"] = secured
        __props__.__dict__["uuid"] = uuid
        __props__.__dict__["value"] = value
        return RepositoryVariable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Output[str]:
        return pulumi.get(self, "repository")

    @property
    @pulumi.getter
    def secured(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "secured")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        return pulumi.get(self, "value")

