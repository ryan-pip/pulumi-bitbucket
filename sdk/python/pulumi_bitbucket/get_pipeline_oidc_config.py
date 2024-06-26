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
    'GetPipelineOidcConfigResult',
    'AwaitableGetPipelineOidcConfigResult',
    'get_pipeline_oidc_config',
    'get_pipeline_oidc_config_output',
]

@pulumi.output_type
class GetPipelineOidcConfigResult:
    """
    A collection of values returned by getPipelineOidcConfig.
    """
    def __init__(__self__, id=None, oidc_config=None, workspace=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if oidc_config and not isinstance(oidc_config, str):
            raise TypeError("Expected argument 'oidc_config' to be a str")
        pulumi.set(__self__, "oidc_config", oidc_config)
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
    @pulumi.getter(name="oidcConfig")
    def oidc_config(self) -> str:
        """
        The Json representing the OIDC config.
        """
        return pulumi.get(self, "oidc_config")

    @property
    @pulumi.getter
    def workspace(self) -> str:
        return pulumi.get(self, "workspace")


class AwaitableGetPipelineOidcConfigResult(GetPipelineOidcConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPipelineOidcConfigResult(
            id=self.id,
            oidc_config=self.oidc_config,
            workspace=self.workspace)


def get_pipeline_oidc_config(workspace: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPipelineOidcConfigResult:
    """
    Provides a way to fetch data on a pipeline OIDC Config.

    OAuth2 Scopes: `none`

    ## Example Usage

    ```python
    import pulumi
    import pulumi_bitbucket as bitbucket

    example = bitbucket.get_pipeline_oidc_config(workspace="example")
    ```


    :param str workspace: The workspace to fetch pipeline oidc config.
    """
    __args__ = dict()
    __args__['workspace'] = workspace
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('bitbucket:index/getPipelineOidcConfig:getPipelineOidcConfig', __args__, opts=opts, typ=GetPipelineOidcConfigResult).value

    return AwaitableGetPipelineOidcConfigResult(
        id=pulumi.get(__ret__, 'id'),
        oidc_config=pulumi.get(__ret__, 'oidc_config'),
        workspace=pulumi.get(__ret__, 'workspace'))


@_utilities.lift_output_func(get_pipeline_oidc_config)
def get_pipeline_oidc_config_output(workspace: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPipelineOidcConfigResult]:
    """
    Provides a way to fetch data on a pipeline OIDC Config.

    OAuth2 Scopes: `none`

    ## Example Usage

    ```python
    import pulumi
    import pulumi_bitbucket as bitbucket

    example = bitbucket.get_pipeline_oidc_config(workspace="example")
    ```


    :param str workspace: The workspace to fetch pipeline oidc config.
    """
    ...
