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

__all__ = ['BranchRestrictionArgs', 'BranchRestriction']

@pulumi.input_type
class BranchRestrictionArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 owner: pulumi.Input[str],
                 repository: pulumi.Input[str],
                 branch_match_kind: Optional[pulumi.Input[str]] = None,
                 branch_type: Optional[pulumi.Input[str]] = None,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input['BranchRestrictionGroupArgs']]]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a BranchRestriction resource.
        :param pulumi.Input[str] kind: The type of restriction that is being applied. Valid values can be found in [docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-group-branch-restrictions).
        :param pulumi.Input[str] owner: The owner of this repository. Can be you or any team you
               have write access to.
        :param pulumi.Input[str] repository: The name of the repository.
        :param pulumi.Input[str] branch_match_kind: Indicates how the restriction is matched against a branch. The default is `glob`. Valid values: `branching_model`, `glob`.
        :param pulumi.Input[str] branch_type: Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The branch type will be calculated using the branching model configured for the repository. Valid values: `feature`, `bugfix`, `release`, `hotfix`, `development`, `production`.
        :param pulumi.Input[Sequence[pulumi.Input['BranchRestrictionGroupArgs']]] groups: A list of groups to use.
        :param pulumi.Input[str] pattern: Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will be empty when `branch_match_kind` is `branching_model`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] users: A list of users to use.
        :param pulumi.Input[int] value: A value applied to the restriction kind. Currently only applicable to `require_passing_builds_to_merge`, `require_default_reviewer_approvals_to_merge` and `require_approvals_to_merge`.
        """
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "owner", owner)
        pulumi.set(__self__, "repository", repository)
        if branch_match_kind is not None:
            pulumi.set(__self__, "branch_match_kind", branch_match_kind)
        if branch_type is not None:
            pulumi.set(__self__, "branch_type", branch_type)
        if groups is not None:
            pulumi.set(__self__, "groups", groups)
        if pattern is not None:
            pulumi.set(__self__, "pattern", pattern)
        if users is not None:
            pulumi.set(__self__, "users", users)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The type of restriction that is being applied. Valid values can be found in [docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-group-branch-restrictions).
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Input[str]:
        """
        The owner of this repository. Can be you or any team you
        have write access to.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: pulumi.Input[str]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Input[str]:
        """
        The name of the repository.
        """
        return pulumi.get(self, "repository")

    @repository.setter
    def repository(self, value: pulumi.Input[str]):
        pulumi.set(self, "repository", value)

    @property
    @pulumi.getter(name="branchMatchKind")
    def branch_match_kind(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates how the restriction is matched against a branch. The default is `glob`. Valid values: `branching_model`, `glob`.
        """
        return pulumi.get(self, "branch_match_kind")

    @branch_match_kind.setter
    def branch_match_kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch_match_kind", value)

    @property
    @pulumi.getter(name="branchType")
    def branch_type(self) -> Optional[pulumi.Input[str]]:
        """
        Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The branch type will be calculated using the branching model configured for the repository. Valid values: `feature`, `bugfix`, `release`, `hotfix`, `development`, `production`.
        """
        return pulumi.get(self, "branch_type")

    @branch_type.setter
    def branch_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch_type", value)

    @property
    @pulumi.getter
    def groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BranchRestrictionGroupArgs']]]]:
        """
        A list of groups to use.
        """
        return pulumi.get(self, "groups")

    @groups.setter
    def groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BranchRestrictionGroupArgs']]]]):
        pulumi.set(self, "groups", value)

    @property
    @pulumi.getter
    def pattern(self) -> Optional[pulumi.Input[str]]:
        """
        Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will be empty when `branch_match_kind` is `branching_model`.
        """
        return pulumi.get(self, "pattern")

    @pattern.setter
    def pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pattern", value)

    @property
    @pulumi.getter
    def users(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of users to use.
        """
        return pulumi.get(self, "users")

    @users.setter
    def users(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "users", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[int]]:
        """
        A value applied to the restriction kind. Currently only applicable to `require_passing_builds_to_merge`, `require_default_reviewer_approvals_to_merge` and `require_approvals_to_merge`.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class _BranchRestrictionState:
    def __init__(__self__, *,
                 branch_match_kind: Optional[pulumi.Input[str]] = None,
                 branch_type: Optional[pulumi.Input[str]] = None,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input['BranchRestrictionGroupArgs']]]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering BranchRestriction resources.
        :param pulumi.Input[str] branch_match_kind: Indicates how the restriction is matched against a branch. The default is `glob`. Valid values: `branching_model`, `glob`.
        :param pulumi.Input[str] branch_type: Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The branch type will be calculated using the branching model configured for the repository. Valid values: `feature`, `bugfix`, `release`, `hotfix`, `development`, `production`.
        :param pulumi.Input[Sequence[pulumi.Input['BranchRestrictionGroupArgs']]] groups: A list of groups to use.
        :param pulumi.Input[str] kind: The type of restriction that is being applied. Valid values can be found in [docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-group-branch-restrictions).
        :param pulumi.Input[str] owner: The owner of this repository. Can be you or any team you
               have write access to.
        :param pulumi.Input[str] pattern: Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will be empty when `branch_match_kind` is `branching_model`.
        :param pulumi.Input[str] repository: The name of the repository.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] users: A list of users to use.
        :param pulumi.Input[int] value: A value applied to the restriction kind. Currently only applicable to `require_passing_builds_to_merge`, `require_default_reviewer_approvals_to_merge` and `require_approvals_to_merge`.
        """
        if branch_match_kind is not None:
            pulumi.set(__self__, "branch_match_kind", branch_match_kind)
        if branch_type is not None:
            pulumi.set(__self__, "branch_type", branch_type)
        if groups is not None:
            pulumi.set(__self__, "groups", groups)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if pattern is not None:
            pulumi.set(__self__, "pattern", pattern)
        if repository is not None:
            pulumi.set(__self__, "repository", repository)
        if users is not None:
            pulumi.set(__self__, "users", users)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="branchMatchKind")
    def branch_match_kind(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates how the restriction is matched against a branch. The default is `glob`. Valid values: `branching_model`, `glob`.
        """
        return pulumi.get(self, "branch_match_kind")

    @branch_match_kind.setter
    def branch_match_kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch_match_kind", value)

    @property
    @pulumi.getter(name="branchType")
    def branch_type(self) -> Optional[pulumi.Input[str]]:
        """
        Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The branch type will be calculated using the branching model configured for the repository. Valid values: `feature`, `bugfix`, `release`, `hotfix`, `development`, `production`.
        """
        return pulumi.get(self, "branch_type")

    @branch_type.setter
    def branch_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch_type", value)

    @property
    @pulumi.getter
    def groups(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BranchRestrictionGroupArgs']]]]:
        """
        A list of groups to use.
        """
        return pulumi.get(self, "groups")

    @groups.setter
    def groups(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BranchRestrictionGroupArgs']]]]):
        pulumi.set(self, "groups", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        The type of restriction that is being applied. Valid values can be found in [docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-group-branch-restrictions).
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def owner(self) -> Optional[pulumi.Input[str]]:
        """
        The owner of this repository. Can be you or any team you
        have write access to.
        """
        return pulumi.get(self, "owner")

    @owner.setter
    def owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "owner", value)

    @property
    @pulumi.getter
    def pattern(self) -> Optional[pulumi.Input[str]]:
        """
        Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will be empty when `branch_match_kind` is `branching_model`.
        """
        return pulumi.get(self, "pattern")

    @pattern.setter
    def pattern(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pattern", value)

    @property
    @pulumi.getter
    def repository(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the repository.
        """
        return pulumi.get(self, "repository")

    @repository.setter
    def repository(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository", value)

    @property
    @pulumi.getter
    def users(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of users to use.
        """
        return pulumi.get(self, "users")

    @users.setter
    def users(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "users", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[int]]:
        """
        A value applied to the restriction kind. Currently only applicable to `require_passing_builds_to_merge`, `require_default_reviewer_approvals_to_merge` and `require_approvals_to_merge`.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "value", value)


class BranchRestriction(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch_match_kind: Optional[pulumi.Input[str]] = None,
                 branch_type: Optional[pulumi.Input[str]] = None,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchRestrictionGroupArgs']]]]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides a Bitbucket branch restriction resource.

        This allows you for setting up branch restrictions for your repository.

        OAuth2 Scopes: `repository:admin`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_bitbucket as bitbucket

        master = bitbucket.BranchRestriction("master",
            groups=[bitbucket.BranchRestrictionGroupArgs(
                owner="my-owner",
                slug="my-group",
            )],
            kind="push",
            owner="myteam",
            pattern="master",
            repository="terraform-code")
        ```

        ## Import

        Branch Restrictions can be imported using their `owner/repo-name/branch-restriction-id` ID, e.g.

        ```sh
         $ pulumi import bitbucket:index/branchRestriction:BranchRestriction example my-account/my-repo/branch-rest-id
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch_match_kind: Indicates how the restriction is matched against a branch. The default is `glob`. Valid values: `branching_model`, `glob`.
        :param pulumi.Input[str] branch_type: Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The branch type will be calculated using the branching model configured for the repository. Valid values: `feature`, `bugfix`, `release`, `hotfix`, `development`, `production`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchRestrictionGroupArgs']]]] groups: A list of groups to use.
        :param pulumi.Input[str] kind: The type of restriction that is being applied. Valid values can be found in [docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-group-branch-restrictions).
        :param pulumi.Input[str] owner: The owner of this repository. Can be you or any team you
               have write access to.
        :param pulumi.Input[str] pattern: Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will be empty when `branch_match_kind` is `branching_model`.
        :param pulumi.Input[str] repository: The name of the repository.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] users: A list of users to use.
        :param pulumi.Input[int] value: A value applied to the restriction kind. Currently only applicable to `require_passing_builds_to_merge`, `require_default_reviewer_approvals_to_merge` and `require_approvals_to_merge`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BranchRestrictionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Bitbucket branch restriction resource.

        This allows you for setting up branch restrictions for your repository.

        OAuth2 Scopes: `repository:admin`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_bitbucket as bitbucket

        master = bitbucket.BranchRestriction("master",
            groups=[bitbucket.BranchRestrictionGroupArgs(
                owner="my-owner",
                slug="my-group",
            )],
            kind="push",
            owner="myteam",
            pattern="master",
            repository="terraform-code")
        ```

        ## Import

        Branch Restrictions can be imported using their `owner/repo-name/branch-restriction-id` ID, e.g.

        ```sh
         $ pulumi import bitbucket:index/branchRestriction:BranchRestriction example my-account/my-repo/branch-rest-id
        ```

        :param str resource_name: The name of the resource.
        :param BranchRestrictionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BranchRestrictionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch_match_kind: Optional[pulumi.Input[str]] = None,
                 branch_type: Optional[pulumi.Input[str]] = None,
                 groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchRestrictionGroupArgs']]]]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 owner: Optional[pulumi.Input[str]] = None,
                 pattern: Optional[pulumi.Input[str]] = None,
                 repository: Optional[pulumi.Input[str]] = None,
                 users: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BranchRestrictionArgs.__new__(BranchRestrictionArgs)

            __props__.__dict__["branch_match_kind"] = branch_match_kind
            __props__.__dict__["branch_type"] = branch_type
            __props__.__dict__["groups"] = groups
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = kind
            if owner is None and not opts.urn:
                raise TypeError("Missing required property 'owner'")
            __props__.__dict__["owner"] = owner
            __props__.__dict__["pattern"] = pattern
            if repository is None and not opts.urn:
                raise TypeError("Missing required property 'repository'")
            __props__.__dict__["repository"] = repository
            __props__.__dict__["users"] = users
            __props__.__dict__["value"] = value
        super(BranchRestriction, __self__).__init__(
            'bitbucket:index/branchRestriction:BranchRestriction',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            branch_match_kind: Optional[pulumi.Input[str]] = None,
            branch_type: Optional[pulumi.Input[str]] = None,
            groups: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchRestrictionGroupArgs']]]]] = None,
            kind: Optional[pulumi.Input[str]] = None,
            owner: Optional[pulumi.Input[str]] = None,
            pattern: Optional[pulumi.Input[str]] = None,
            repository: Optional[pulumi.Input[str]] = None,
            users: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            value: Optional[pulumi.Input[int]] = None) -> 'BranchRestriction':
        """
        Get an existing BranchRestriction resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch_match_kind: Indicates how the restriction is matched against a branch. The default is `glob`. Valid values: `branching_model`, `glob`.
        :param pulumi.Input[str] branch_type: Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The branch type will be calculated using the branching model configured for the repository. Valid values: `feature`, `bugfix`, `release`, `hotfix`, `development`, `production`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchRestrictionGroupArgs']]]] groups: A list of groups to use.
        :param pulumi.Input[str] kind: The type of restriction that is being applied. Valid values can be found in [docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-group-branch-restrictions).
        :param pulumi.Input[str] owner: The owner of this repository. Can be you or any team you
               have write access to.
        :param pulumi.Input[str] pattern: Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will be empty when `branch_match_kind` is `branching_model`.
        :param pulumi.Input[str] repository: The name of the repository.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] users: A list of users to use.
        :param pulumi.Input[int] value: A value applied to the restriction kind. Currently only applicable to `require_passing_builds_to_merge`, `require_default_reviewer_approvals_to_merge` and `require_approvals_to_merge`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BranchRestrictionState.__new__(_BranchRestrictionState)

        __props__.__dict__["branch_match_kind"] = branch_match_kind
        __props__.__dict__["branch_type"] = branch_type
        __props__.__dict__["groups"] = groups
        __props__.__dict__["kind"] = kind
        __props__.__dict__["owner"] = owner
        __props__.__dict__["pattern"] = pattern
        __props__.__dict__["repository"] = repository
        __props__.__dict__["users"] = users
        __props__.__dict__["value"] = value
        return BranchRestriction(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="branchMatchKind")
    def branch_match_kind(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates how the restriction is matched against a branch. The default is `glob`. Valid values: `branching_model`, `glob`.
        """
        return pulumi.get(self, "branch_match_kind")

    @property
    @pulumi.getter(name="branchType")
    def branch_type(self) -> pulumi.Output[Optional[str]]:
        """
        Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The branch type will be calculated using the branching model configured for the repository. Valid values: `feature`, `bugfix`, `release`, `hotfix`, `development`, `production`.
        """
        return pulumi.get(self, "branch_type")

    @property
    @pulumi.getter
    def groups(self) -> pulumi.Output[Optional[Sequence['outputs.BranchRestrictionGroup']]]:
        """
        A list of groups to use.
        """
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        The type of restriction that is being applied. Valid values can be found in [docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-group-branch-restrictions).
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        The owner of this repository. Can be you or any team you
        have write access to.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def pattern(self) -> pulumi.Output[Optional[str]]:
        """
        Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will be empty when `branch_match_kind` is `branching_model`.
        """
        return pulumi.get(self, "pattern")

    @property
    @pulumi.getter
    def repository(self) -> pulumi.Output[str]:
        """
        The name of the repository.
        """
        return pulumi.get(self, "repository")

    @property
    @pulumi.getter
    def users(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of users to use.
        """
        return pulumi.get(self, "users")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[int]]:
        """
        A value applied to the restriction kind. Currently only applicable to `require_passing_builds_to_merge`, `require_default_reviewer_approvals_to_merge` and `require_approvals_to_merge`.
        """
        return pulumi.get(self, "value")

