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

__all__ = [
    'GetCurrentUserResult',
    'AwaitableGetCurrentUserResult',
    'get_current_user',
    'get_current_user_output',
]

@pulumi.output_type
class GetCurrentUserResult:
    """
    A collection of values returned by getCurrentUser.
    """
    def __init__(__self__, display_name=None, emails=None, id=None, username=None, uuid=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if emails and not isinstance(emails, list):
            raise TypeError("Expected argument 'emails' to be a list")
        pulumi.set(__self__, "emails", emails)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if username and not isinstance(username, str):
            raise TypeError("Expected argument 'username' to be a str")
        pulumi.set(__self__, "username", username)
        if uuid and not isinstance(uuid, str):
            raise TypeError("Expected argument 'uuid' to be a str")
        pulumi.set(__self__, "uuid", uuid)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        the display name that the user wants to use for GDPR
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def emails(self) -> Sequence['outputs.GetCurrentUserEmailResult']:
        """
        The email address.
        """
        return pulumi.get(self, "emails")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        The Username.
        """
        return pulumi.get(self, "username")

    @property
    @pulumi.getter
    def uuid(self) -> str:
        """
        the uuid that bitbucket users to connect a user to various objects
        """
        return pulumi.get(self, "uuid")


class AwaitableGetCurrentUserResult(GetCurrentUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCurrentUserResult(
            display_name=self.display_name,
            emails=self.emails,
            id=self.id,
            username=self.username,
            uuid=self.uuid)


def get_current_user(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCurrentUserResult:
    """
    Provides a way to fetch data of the current user.

    OAuth2 Scopes: `account`

    ## Example Usage

    ```python
    import pulumi
    import pulumi_bitbucket as bitbucket

    example = bitbucket.get_current_user()
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('bitbucket:index/getCurrentUser:getCurrentUser', __args__, opts=opts, typ=GetCurrentUserResult).value

    return AwaitableGetCurrentUserResult(
        display_name=pulumi.get(__ret__, 'display_name'),
        emails=pulumi.get(__ret__, 'emails'),
        id=pulumi.get(__ret__, 'id'),
        username=pulumi.get(__ret__, 'username'),
        uuid=pulumi.get(__ret__, 'uuid'))


@_utilities.lift_output_func(get_current_user)
def get_current_user_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCurrentUserResult]:
    """
    Provides a way to fetch data of the current user.

    OAuth2 Scopes: `account`

    ## Example Usage

    ```python
    import pulumi
    import pulumi_bitbucket as bitbucket

    example = bitbucket.get_current_user()
    ```
    """
    ...
