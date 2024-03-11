# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['DeploymentVariableArgs', 'DeploymentVariable']

@pulumi.input_type
class DeploymentVariableArgs:
    def __init__(__self__, *,
                 deployment: pulumi.Input[str],
                 key: pulumi.Input[str],
                 value: pulumi.Input[str],
                 secured: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a DeploymentVariable resource.
        :param pulumi.Input[str] deployment: The deployment ID you want to assign this variable to.
        :param pulumi.Input[str] key: The unique name of the variable.
        :param pulumi.Input[str] value: The value of the variable.
        :param pulumi.Input[bool] secured: If true, this variable will be treated as secured. The value will never be exposed in the logs or the REST API.
        """
        pulumi.set(__self__, "deployment", deployment)
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)
        if secured is not None:
            pulumi.set(__self__, "secured", secured)

    @property
    @pulumi.getter
    def deployment(self) -> pulumi.Input[str]:
        """
        The deployment ID you want to assign this variable to.
        """
        return pulumi.get(self, "deployment")

    @deployment.setter
    def deployment(self, value: pulumi.Input[str]):
        pulumi.set(self, "deployment", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The unique name of the variable.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the variable.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter
    def secured(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, this variable will be treated as secured. The value will never be exposed in the logs or the REST API.
        """
        return pulumi.get(self, "secured")

    @secured.setter
    def secured(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "secured", value)


@pulumi.input_type
class _DeploymentVariableState:
    def __init__(__self__, *,
                 deployment: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 secured: Optional[pulumi.Input[bool]] = None,
                 uuid: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering DeploymentVariable resources.
        :param pulumi.Input[str] deployment: The deployment ID you want to assign this variable to.
        :param pulumi.Input[str] key: The unique name of the variable.
        :param pulumi.Input[bool] secured: If true, this variable will be treated as secured. The value will never be exposed in the logs or the REST API.
        :param pulumi.Input[str] uuid: (Computed) The UUID identifying the variable.
        :param pulumi.Input[str] value: The value of the variable.
        """
        if deployment is not None:
            pulumi.set(__self__, "deployment", deployment)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if secured is not None:
            pulumi.set(__self__, "secured", secured)
        if uuid is not None:
            pulumi.set(__self__, "uuid", uuid)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def deployment(self) -> Optional[pulumi.Input[str]]:
        """
        The deployment ID you want to assign this variable to.
        """
        return pulumi.get(self, "deployment")

    @deployment.setter
    def deployment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The unique name of the variable.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def secured(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, this variable will be treated as secured. The value will never be exposed in the logs or the REST API.
        """
        return pulumi.get(self, "secured")

    @secured.setter
    def secured(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "secured", value)

    @property
    @pulumi.getter
    def uuid(self) -> Optional[pulumi.Input[str]]:
        """
        (Computed) The UUID identifying the variable.
        """
        return pulumi.get(self, "uuid")

    @uuid.setter
    def uuid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uuid", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the variable.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class DeploymentVariable(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 secured: Optional[pulumi.Input[bool]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        This resource allows you to configure deployment variables.

        OAuth2 Scopes: `none`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_bitbucket as bitbucket

        monorepo = bitbucket.Repository("monorepo",
            owner="gob",
            pipelines_enabled=True)
        test = bitbucket.Deployment("test",
            repository=monorepo.id,
            stage="Test")
        country = bitbucket.DeploymentVariable("country",
            deployment=test.id,
            key="COUNTRY",
            value="Kenya",
            secured=False)
        ```

        ## Import

        Deployment Variables can be imported using their `deployment-id/uuid` ID, e.g.

        ```sh
         $ pulumi import bitbucket:index/deploymentVariable:DeploymentVariable example deployment-id/uuid
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment: The deployment ID you want to assign this variable to.
        :param pulumi.Input[str] key: The unique name of the variable.
        :param pulumi.Input[bool] secured: If true, this variable will be treated as secured. The value will never be exposed in the logs or the REST API.
        :param pulumi.Input[str] value: The value of the variable.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentVariableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        This resource allows you to configure deployment variables.

        OAuth2 Scopes: `none`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_bitbucket as bitbucket

        monorepo = bitbucket.Repository("monorepo",
            owner="gob",
            pipelines_enabled=True)
        test = bitbucket.Deployment("test",
            repository=monorepo.id,
            stage="Test")
        country = bitbucket.DeploymentVariable("country",
            deployment=test.id,
            key="COUNTRY",
            value="Kenya",
            secured=False)
        ```

        ## Import

        Deployment Variables can be imported using their `deployment-id/uuid` ID, e.g.

        ```sh
         $ pulumi import bitbucket:index/deploymentVariable:DeploymentVariable example deployment-id/uuid
        ```

        :param str resource_name: The name of the resource.
        :param DeploymentVariableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentVariableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 secured: Optional[pulumi.Input[bool]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentVariableArgs.__new__(DeploymentVariableArgs)

            if deployment is None and not opts.urn:
                raise TypeError("Missing required property 'deployment'")
            __props__.__dict__["deployment"] = deployment
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            __props__.__dict__["secured"] = secured
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = None if value is None else pulumi.Output.secret(value)
            __props__.__dict__["uuid"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["value"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(DeploymentVariable, __self__).__init__(
            'bitbucket:index/deploymentVariable:DeploymentVariable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            deployment: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            secured: Optional[pulumi.Input[bool]] = None,
            uuid: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'DeploymentVariable':
        """
        Get an existing DeploymentVariable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment: The deployment ID you want to assign this variable to.
        :param pulumi.Input[str] key: The unique name of the variable.
        :param pulumi.Input[bool] secured: If true, this variable will be treated as secured. The value will never be exposed in the logs or the REST API.
        :param pulumi.Input[str] uuid: (Computed) The UUID identifying the variable.
        :param pulumi.Input[str] value: The value of the variable.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DeploymentVariableState.__new__(_DeploymentVariableState)

        __props__.__dict__["deployment"] = deployment
        __props__.__dict__["key"] = key
        __props__.__dict__["secured"] = secured
        __props__.__dict__["uuid"] = uuid
        __props__.__dict__["value"] = value
        return DeploymentVariable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def deployment(self) -> pulumi.Output[str]:
        """
        The deployment ID you want to assign this variable to.
        """
        return pulumi.get(self, "deployment")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The unique name of the variable.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def secured(self) -> pulumi.Output[Optional[bool]]:
        """
        If true, this variable will be treated as secured. The value will never be exposed in the logs or the REST API.
        """
        return pulumi.get(self, "secured")

    @property
    @pulumi.getter
    def uuid(self) -> pulumi.Output[str]:
        """
        (Computed) The UUID identifying the variable.
        """
        return pulumi.get(self, "uuid")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The value of the variable.
        """
        return pulumi.get(self, "value")

