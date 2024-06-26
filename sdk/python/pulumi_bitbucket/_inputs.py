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
    'BranchRestrictionGroupArgs',
    'BranchingModelBranchTypeArgs',
    'BranchingModelDevelopmentArgs',
    'BranchingModelProductionArgs',
    'DeploymentRestrictionsArgs',
    'ForkedRepositoryLinkArgs',
    'ForkedRepositoryLinkAvatarArgs',
    'PipelineScheduleTargetArgs',
    'PipelineScheduleTargetSelectorArgs',
    'PipelineSshKnownHostPublicKeyArgs',
    'ProjectBranchingModelBranchTypeArgs',
    'ProjectBranchingModelDevelopmentArgs',
    'ProjectBranchingModelProductionArgs',
    'ProjectLinkArgs',
    'ProjectLinkAvatarArgs',
    'RepositoryLinkArgs',
    'RepositoryLinkAvatarArgs',
]

@pulumi.input_type
class BranchRestrictionGroupArgs:
    def __init__(__self__, *,
                 owner: pulumi.Input[str],
                 slug: pulumi.Input[str]):
        """
        :param pulumi.Input[str] owner: The owner of this repository. Can be you or any team you
               have write access to.
        """
        pulumi.set(__self__, "owner", owner)
        pulumi.set(__self__, "slug", slug)

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
    def slug(self) -> pulumi.Input[str]:
        return pulumi.get(self, "slug")

    @slug.setter
    def slug(self, value: pulumi.Input[str]):
        pulumi.set(self, "slug", value)


@pulumi.input_type
class BranchingModelBranchTypeArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 prefix: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] kind: The kind of the branch type. Valid values are `feature`, `bugfix`, `release`, `hotfix`.
        :param pulumi.Input[bool] enabled: Whether the branch type is enabled or not. A disabled branch type may contain an invalid `prefix`.
        :param pulumi.Input[str] prefix: The prefix for this branch type. A branch with this prefix will be classified as per kind. The prefix of an enabled branch type must be a valid branch prefix. Additionally, it cannot be blank, empty or null. The prefix for a disabled branch type can be empty or invalid.
        """
        pulumi.set(__self__, "kind", kind)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of the branch type. Valid values are `feature`, `bugfix`, `release`, `hotfix`.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the branch type is enabled or not. A disabled branch type may contain an invalid `prefix`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The prefix for this branch type. A branch with this prefix will be classified as per kind. The prefix of an enabled branch type must be a valid branch prefix. Additionally, it cannot be blank, empty or null. The prefix for a disabled branch type can be empty or invalid.
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)


@pulumi.input_type
class BranchingModelDevelopmentArgs:
    def __init__(__self__, *,
                 branch_does_not_exist: Optional[pulumi.Input[bool]] = None,
                 is_valid: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 use_mainbranch: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] branch_does_not_exist: Optional and only returned for a repository's branching model. Indicates if the indicated branch exists on the repository (`false`) or not (`true`). This is useful for determining a fallback to the mainbranch when a repository is inheriting its project's branching model.
        :param pulumi.Input[str] name: The configured branch. It must be null when `use_mainbranch` is true. Otherwise it must be a non-empty value. It is possible for the configured branch to not exist (e.g. it was deleted after the settings are set).
        :param pulumi.Input[bool] use_mainbranch: Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). When `true` the name must be null or not provided. When `false` the name must contain a non-empty branch name.
        """
        if branch_does_not_exist is not None:
            pulumi.set(__self__, "branch_does_not_exist", branch_does_not_exist)
        if is_valid is not None:
            pulumi.set(__self__, "is_valid", is_valid)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if use_mainbranch is not None:
            pulumi.set(__self__, "use_mainbranch", use_mainbranch)

    @property
    @pulumi.getter(name="branchDoesNotExist")
    def branch_does_not_exist(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional and only returned for a repository's branching model. Indicates if the indicated branch exists on the repository (`false`) or not (`true`). This is useful for determining a fallback to the mainbranch when a repository is inheriting its project's branching model.
        """
        return pulumi.get(self, "branch_does_not_exist")

    @branch_does_not_exist.setter
    def branch_does_not_exist(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "branch_does_not_exist", value)

    @property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_valid")

    @is_valid.setter
    def is_valid(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_valid", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The configured branch. It must be null when `use_mainbranch` is true. Otherwise it must be a non-empty value. It is possible for the configured branch to not exist (e.g. it was deleted after the settings are set).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="useMainbranch")
    def use_mainbranch(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). When `true` the name must be null or not provided. When `false` the name must contain a non-empty branch name.
        """
        return pulumi.get(self, "use_mainbranch")

    @use_mainbranch.setter
    def use_mainbranch(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_mainbranch", value)


@pulumi.input_type
class BranchingModelProductionArgs:
    def __init__(__self__, *,
                 branch_does_not_exist: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 is_valid: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 use_mainbranch: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] branch_does_not_exist: Optional and only returned for a repository's branching model. Indicates if the indicated branch exists on the repository (`false`) or not (`true`). This is useful for determining a fallback to the mainbranch when a repository is inheriting its project's branching model.
        :param pulumi.Input[bool] enabled: Indicates if branch is enabled or not.
        :param pulumi.Input[str] name: The configured branch. It must be null when `use_mainbranch` is true. Otherwise it must be a non-empty value. It is possible for the configured branch to not exist (e.g. it was deleted after the settings are set).
        :param pulumi.Input[bool] use_mainbranch: Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). When `true` the name must be null or not provided. When `false` the name must contain a non-empty branch name.
        """
        if branch_does_not_exist is not None:
            pulumi.set(__self__, "branch_does_not_exist", branch_does_not_exist)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if is_valid is not None:
            pulumi.set(__self__, "is_valid", is_valid)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if use_mainbranch is not None:
            pulumi.set(__self__, "use_mainbranch", use_mainbranch)

    @property
    @pulumi.getter(name="branchDoesNotExist")
    def branch_does_not_exist(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional and only returned for a repository's branching model. Indicates if the indicated branch exists on the repository (`false`) or not (`true`). This is useful for determining a fallback to the mainbranch when a repository is inheriting its project's branching model.
        """
        return pulumi.get(self, "branch_does_not_exist")

    @branch_does_not_exist.setter
    def branch_does_not_exist(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "branch_does_not_exist", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if branch is enabled or not.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_valid")

    @is_valid.setter
    def is_valid(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_valid", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The configured branch. It must be null when `use_mainbranch` is true. Otherwise it must be a non-empty value. It is possible for the configured branch to not exist (e.g. it was deleted after the settings are set).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="useMainbranch")
    def use_mainbranch(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). When `true` the name must be null or not provided. When `false` the name must contain a non-empty branch name.
        """
        return pulumi.get(self, "use_mainbranch")

    @use_mainbranch.setter
    def use_mainbranch(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_mainbranch", value)


@pulumi.input_type
class DeploymentRestrictionsArgs:
    def __init__(__self__, *,
                 admin_only: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] admin_only: Only Admins can deploy this deployment stage.
        """
        if admin_only is not None:
            pulumi.set(__self__, "admin_only", admin_only)

    @property
    @pulumi.getter(name="adminOnly")
    def admin_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Only Admins can deploy this deployment stage.
        """
        return pulumi.get(self, "admin_only")

    @admin_only.setter
    def admin_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "admin_only", value)


@pulumi.input_type
class ForkedRepositoryLinkArgs:
    def __init__(__self__, *,
                 avatar: Optional[pulumi.Input['ForkedRepositoryLinkAvatarArgs']] = None):
        """
        :param pulumi.Input['ForkedRepositoryLinkAvatarArgs'] avatar: An avatar link to a resource related to this object. See Avatar Below.
        """
        if avatar is not None:
            pulumi.set(__self__, "avatar", avatar)

    @property
    @pulumi.getter
    def avatar(self) -> Optional[pulumi.Input['ForkedRepositoryLinkAvatarArgs']]:
        """
        An avatar link to a resource related to this object. See Avatar Below.
        """
        return pulumi.get(self, "avatar")

    @avatar.setter
    def avatar(self, value: Optional[pulumi.Input['ForkedRepositoryLinkAvatarArgs']]):
        pulumi.set(self, "avatar", value)


@pulumi.input_type
class ForkedRepositoryLinkAvatarArgs:
    def __init__(__self__, *,
                 href: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] href: href of the avatar.
        """
        if href is not None:
            pulumi.set(__self__, "href", href)

    @property
    @pulumi.getter
    def href(self) -> Optional[pulumi.Input[str]]:
        """
        href of the avatar.
        """
        return pulumi.get(self, "href")

    @href.setter
    def href(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "href", value)


@pulumi.input_type
class PipelineScheduleTargetArgs:
    def __init__(__self__, *,
                 ref_name: pulumi.Input[str],
                 ref_type: pulumi.Input[str],
                 selector: pulumi.Input['PipelineScheduleTargetSelectorArgs']):
        """
        :param pulumi.Input[str] ref_name: The name of the reference.
        :param pulumi.Input[str] ref_type: The type of reference. Valid values are `branch` and `tag`.
        :param pulumi.Input['PipelineScheduleTargetSelectorArgs'] selector: Selector spec. See Selector below.
        """
        pulumi.set(__self__, "ref_name", ref_name)
        pulumi.set(__self__, "ref_type", ref_type)
        pulumi.set(__self__, "selector", selector)

    @property
    @pulumi.getter(name="refName")
    def ref_name(self) -> pulumi.Input[str]:
        """
        The name of the reference.
        """
        return pulumi.get(self, "ref_name")

    @ref_name.setter
    def ref_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "ref_name", value)

    @property
    @pulumi.getter(name="refType")
    def ref_type(self) -> pulumi.Input[str]:
        """
        The type of reference. Valid values are `branch` and `tag`.
        """
        return pulumi.get(self, "ref_type")

    @ref_type.setter
    def ref_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "ref_type", value)

    @property
    @pulumi.getter
    def selector(self) -> pulumi.Input['PipelineScheduleTargetSelectorArgs']:
        """
        Selector spec. See Selector below.
        """
        return pulumi.get(self, "selector")

    @selector.setter
    def selector(self, value: pulumi.Input['PipelineScheduleTargetSelectorArgs']):
        pulumi.set(self, "selector", value)


@pulumi.input_type
class PipelineScheduleTargetSelectorArgs:
    def __init__(__self__, *,
                 pattern: pulumi.Input[str],
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] pattern: The name of the matching pipeline definition.
        :param pulumi.Input[str] type: Selector type. Default value is `branches`.
        """
        pulumi.set(__self__, "pattern", pattern)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def pattern(self) -> pulumi.Input[str]:
        """
        The name of the matching pipeline definition.
        """
        return pulumi.get(self, "pattern")

    @pattern.setter
    def pattern(self, value: pulumi.Input[str]):
        pulumi.set(self, "pattern", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Selector type. Default value is `branches`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class PipelineSshKnownHostPublicKeyArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 key_type: pulumi.Input[str],
                 md5_fingerprint: Optional[pulumi.Input[str]] = None,
                 sha256_fingerprint: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] key: The plain public key.
        :param pulumi.Input[str] key_type: The type of the public key. Valid values are `ssh-ed25519`, `ecdsa-sha2-nistp256`, `ssh-rsa`, and `ssh-dss`.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "key_type", key_type)
        if md5_fingerprint is not None:
            pulumi.set(__self__, "md5_fingerprint", md5_fingerprint)
        if sha256_fingerprint is not None:
            pulumi.set(__self__, "sha256_fingerprint", sha256_fingerprint)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The plain public key.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="keyType")
    def key_type(self) -> pulumi.Input[str]:
        """
        The type of the public key. Valid values are `ssh-ed25519`, `ecdsa-sha2-nistp256`, `ssh-rsa`, and `ssh-dss`.
        """
        return pulumi.get(self, "key_type")

    @key_type.setter
    def key_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_type", value)

    @property
    @pulumi.getter(name="md5Fingerprint")
    def md5_fingerprint(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "md5_fingerprint")

    @md5_fingerprint.setter
    def md5_fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "md5_fingerprint", value)

    @property
    @pulumi.getter(name="sha256Fingerprint")
    def sha256_fingerprint(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sha256_fingerprint")

    @sha256_fingerprint.setter
    def sha256_fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sha256_fingerprint", value)


@pulumi.input_type
class ProjectBranchingModelBranchTypeArgs:
    def __init__(__self__, *,
                 kind: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 prefix: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] kind: The kind of the branch type. Valid values are `feature`, `bugfix`, `release`, `hotfix`.
        :param pulumi.Input[bool] enabled: Whether the branch type is enabled or not. A disabled branch type may contain an invalid `prefix`.
        :param pulumi.Input[str] prefix: The prefix for this branch type. A branch with this prefix will be classified as per kind. The prefix of an enabled branch type must be a valid branch prefix. Additionally, it cannot be blank, empty or null. The prefix for a disabled branch type can be empty or invalid.
        """
        pulumi.set(__self__, "kind", kind)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        The kind of the branch type. Valid values are `feature`, `bugfix`, `release`, `hotfix`.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the branch type is enabled or not. A disabled branch type may contain an invalid `prefix`.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter
    def prefix(self) -> Optional[pulumi.Input[str]]:
        """
        The prefix for this branch type. A branch with this prefix will be classified as per kind. The prefix of an enabled branch type must be a valid branch prefix. Additionally, it cannot be blank, empty or null. The prefix for a disabled branch type can be empty or invalid.
        """
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix", value)


@pulumi.input_type
class ProjectBranchingModelDevelopmentArgs:
    def __init__(__self__, *,
                 branch_does_not_exist: Optional[pulumi.Input[bool]] = None,
                 is_valid: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 use_mainbranch: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] branch_does_not_exist: Optional and only returned for a project's branching model. Indicates if the indicated branch exists on the project (`false`) or not (`true`). This is useful for determining a fallback to the mainbranch when a project is inheriting its project's branching model.
        :param pulumi.Input[str] name: The configured branch. It must be null when `use_mainbranch` is true. Otherwise it must be a non-empty value. It is possible for the configured branch to not exist (e.g. it was deleted after the settings are set).
        :param pulumi.Input[bool] use_mainbranch: Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). When `true` the name must be null or not provided. When `false` the name must contain a non-empty branch name.
        """
        if branch_does_not_exist is not None:
            pulumi.set(__self__, "branch_does_not_exist", branch_does_not_exist)
        if is_valid is not None:
            pulumi.set(__self__, "is_valid", is_valid)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if use_mainbranch is not None:
            pulumi.set(__self__, "use_mainbranch", use_mainbranch)

    @property
    @pulumi.getter(name="branchDoesNotExist")
    def branch_does_not_exist(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional and only returned for a project's branching model. Indicates if the indicated branch exists on the project (`false`) or not (`true`). This is useful for determining a fallback to the mainbranch when a project is inheriting its project's branching model.
        """
        return pulumi.get(self, "branch_does_not_exist")

    @branch_does_not_exist.setter
    def branch_does_not_exist(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "branch_does_not_exist", value)

    @property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_valid")

    @is_valid.setter
    def is_valid(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_valid", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The configured branch. It must be null when `use_mainbranch` is true. Otherwise it must be a non-empty value. It is possible for the configured branch to not exist (e.g. it was deleted after the settings are set).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="useMainbranch")
    def use_mainbranch(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). When `true` the name must be null or not provided. When `false` the name must contain a non-empty branch name.
        """
        return pulumi.get(self, "use_mainbranch")

    @use_mainbranch.setter
    def use_mainbranch(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_mainbranch", value)


@pulumi.input_type
class ProjectBranchingModelProductionArgs:
    def __init__(__self__, *,
                 branch_does_not_exist: Optional[pulumi.Input[bool]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 is_valid: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 use_mainbranch: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] branch_does_not_exist: Optional and only returned for a project's branching model. Indicates if the indicated branch exists on the project (`false`) or not (`true`). This is useful for determining a fallback to the mainbranch when a project is inheriting its project's branching model.
        :param pulumi.Input[bool] enabled: Indicates if branch is enabled or not.
        :param pulumi.Input[str] name: The configured branch. It must be null when `use_mainbranch` is true. Otherwise it must be a non-empty value. It is possible for the configured branch to not exist (e.g. it was deleted after the settings are set).
        :param pulumi.Input[bool] use_mainbranch: Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). When `true` the name must be null or not provided. When `false` the name must contain a non-empty branch name.
        """
        if branch_does_not_exist is not None:
            pulumi.set(__self__, "branch_does_not_exist", branch_does_not_exist)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if is_valid is not None:
            pulumi.set(__self__, "is_valid", is_valid)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if use_mainbranch is not None:
            pulumi.set(__self__, "use_mainbranch", use_mainbranch)

    @property
    @pulumi.getter(name="branchDoesNotExist")
    def branch_does_not_exist(self) -> Optional[pulumi.Input[bool]]:
        """
        Optional and only returned for a project's branching model. Indicates if the indicated branch exists on the project (`false`) or not (`true`). This is useful for determining a fallback to the mainbranch when a project is inheriting its project's branching model.
        """
        return pulumi.get(self, "branch_does_not_exist")

    @branch_does_not_exist.setter
    def branch_does_not_exist(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "branch_does_not_exist", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if branch is enabled or not.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "is_valid")

    @is_valid.setter
    def is_valid(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_valid", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The configured branch. It must be null when `use_mainbranch` is true. Otherwise it must be a non-empty value. It is possible for the configured branch to not exist (e.g. it was deleted after the settings are set).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="useMainbranch")
    def use_mainbranch(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). When `true` the name must be null or not provided. When `false` the name must contain a non-empty branch name.
        """
        return pulumi.get(self, "use_mainbranch")

    @use_mainbranch.setter
    def use_mainbranch(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_mainbranch", value)


@pulumi.input_type
class ProjectLinkArgs:
    def __init__(__self__, *,
                 avatar: Optional[pulumi.Input['ProjectLinkAvatarArgs']] = None):
        """
        :param pulumi.Input['ProjectLinkAvatarArgs'] avatar: An avatar link to a resource related to this object. See Avatar Below.
        """
        if avatar is not None:
            pulumi.set(__self__, "avatar", avatar)

    @property
    @pulumi.getter
    def avatar(self) -> Optional[pulumi.Input['ProjectLinkAvatarArgs']]:
        """
        An avatar link to a resource related to this object. See Avatar Below.
        """
        return pulumi.get(self, "avatar")

    @avatar.setter
    def avatar(self, value: Optional[pulumi.Input['ProjectLinkAvatarArgs']]):
        pulumi.set(self, "avatar", value)


@pulumi.input_type
class ProjectLinkAvatarArgs:
    def __init__(__self__, *,
                 href: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] href: href of the avatar.
        """
        if href is not None:
            pulumi.set(__self__, "href", href)

    @property
    @pulumi.getter
    def href(self) -> Optional[pulumi.Input[str]]:
        """
        href of the avatar.
        """
        return pulumi.get(self, "href")

    @href.setter
    def href(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "href", value)


@pulumi.input_type
class RepositoryLinkArgs:
    def __init__(__self__, *,
                 avatar: Optional[pulumi.Input['RepositoryLinkAvatarArgs']] = None):
        """
        :param pulumi.Input['RepositoryLinkAvatarArgs'] avatar: An avatar link to a resource related to this object. See Avatar Below.
        """
        if avatar is not None:
            pulumi.set(__self__, "avatar", avatar)

    @property
    @pulumi.getter
    def avatar(self) -> Optional[pulumi.Input['RepositoryLinkAvatarArgs']]:
        """
        An avatar link to a resource related to this object. See Avatar Below.
        """
        return pulumi.get(self, "avatar")

    @avatar.setter
    def avatar(self, value: Optional[pulumi.Input['RepositoryLinkAvatarArgs']]):
        pulumi.set(self, "avatar", value)


@pulumi.input_type
class RepositoryLinkAvatarArgs:
    def __init__(__self__, *,
                 href: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] href: href of the avatar.
        """
        if href is not None:
            pulumi.set(__self__, "href", href)

    @property
    @pulumi.getter
    def href(self) -> Optional[pulumi.Input[str]]:
        """
        href of the avatar.
        """
        return pulumi.get(self, "href")

    @href.setter
    def href(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "href", value)


