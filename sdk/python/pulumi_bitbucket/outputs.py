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
    'BranchRestrictionGroup',
    'BranchingModelBranchType',
    'BranchingModelDevelopment',
    'BranchingModelProduction',
    'DeploymentRestrictions',
    'ForkedRepositoryLink',
    'ForkedRepositoryLinkAvatar',
    'PipelineScheduleTarget',
    'PipelineScheduleTargetSelector',
    'PipelineSshKnownHostPublicKey',
    'ProjectBranchingModelBranchType',
    'ProjectBranchingModelDevelopment',
    'ProjectBranchingModelProduction',
    'ProjectLink',
    'ProjectLinkAvatar',
    'RepositoryLink',
    'RepositoryLinkAvatar',
    'GetCurrentUserEmailResult',
    'GetGroupsGroupResult',
    'GetHookTypesHookTypeResult',
    'GetIpRangesRangeResult',
]

@pulumi.output_type
class BranchRestrictionGroup(dict):
    def __init__(__self__, *,
                 owner: str,
                 slug: str):
        pulumi.set(__self__, "owner", owner)
        pulumi.set(__self__, "slug", slug)

    @property
    @pulumi.getter
    def owner(self) -> str:
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def slug(self) -> str:
        return pulumi.get(self, "slug")


@pulumi.output_type
class BranchingModelBranchType(dict):
    def __init__(__self__, *,
                 kind: str,
                 enabled: Optional[bool] = None,
                 prefix: Optional[str] = None):
        pulumi.set(__self__, "kind", kind)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter
    def kind(self) -> str:
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        return pulumi.get(self, "prefix")


@pulumi.output_type
class BranchingModelDevelopment(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "branchDoesNotExist":
            suggest = "branch_does_not_exist"
        elif key == "isValid":
            suggest = "is_valid"
        elif key == "useMainbranch":
            suggest = "use_mainbranch"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BranchingModelDevelopment. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BranchingModelDevelopment.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BranchingModelDevelopment.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 branch_does_not_exist: Optional[bool] = None,
                 is_valid: Optional[bool] = None,
                 name: Optional[str] = None,
                 use_mainbranch: Optional[bool] = None):
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
    def branch_does_not_exist(self) -> Optional[bool]:
        return pulumi.get(self, "branch_does_not_exist")

    @property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> Optional[bool]:
        return pulumi.get(self, "is_valid")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="useMainbranch")
    def use_mainbranch(self) -> Optional[bool]:
        return pulumi.get(self, "use_mainbranch")


@pulumi.output_type
class BranchingModelProduction(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "branchDoesNotExist":
            suggest = "branch_does_not_exist"
        elif key == "isValid":
            suggest = "is_valid"
        elif key == "useMainbranch":
            suggest = "use_mainbranch"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BranchingModelProduction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BranchingModelProduction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BranchingModelProduction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 branch_does_not_exist: Optional[bool] = None,
                 enabled: Optional[bool] = None,
                 is_valid: Optional[bool] = None,
                 name: Optional[str] = None,
                 use_mainbranch: Optional[bool] = None):
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
    def branch_does_not_exist(self) -> Optional[bool]:
        return pulumi.get(self, "branch_does_not_exist")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> Optional[bool]:
        return pulumi.get(self, "is_valid")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="useMainbranch")
    def use_mainbranch(self) -> Optional[bool]:
        return pulumi.get(self, "use_mainbranch")


@pulumi.output_type
class DeploymentRestrictions(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "adminOnly":
            suggest = "admin_only"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DeploymentRestrictions. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DeploymentRestrictions.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DeploymentRestrictions.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 admin_only: Optional[bool] = None):
        if admin_only is not None:
            pulumi.set(__self__, "admin_only", admin_only)

    @property
    @pulumi.getter(name="adminOnly")
    def admin_only(self) -> Optional[bool]:
        return pulumi.get(self, "admin_only")


@pulumi.output_type
class ForkedRepositoryLink(dict):
    def __init__(__self__, *,
                 avatar: Optional['outputs.ForkedRepositoryLinkAvatar'] = None):
        if avatar is not None:
            pulumi.set(__self__, "avatar", avatar)

    @property
    @pulumi.getter
    def avatar(self) -> Optional['outputs.ForkedRepositoryLinkAvatar']:
        return pulumi.get(self, "avatar")


@pulumi.output_type
class ForkedRepositoryLinkAvatar(dict):
    def __init__(__self__, *,
                 href: Optional[str] = None):
        if href is not None:
            pulumi.set(__self__, "href", href)

    @property
    @pulumi.getter
    def href(self) -> Optional[str]:
        return pulumi.get(self, "href")


@pulumi.output_type
class PipelineScheduleTarget(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "refName":
            suggest = "ref_name"
        elif key == "refType":
            suggest = "ref_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PipelineScheduleTarget. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PipelineScheduleTarget.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PipelineScheduleTarget.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ref_name: str,
                 ref_type: str,
                 selector: 'outputs.PipelineScheduleTargetSelector'):
        pulumi.set(__self__, "ref_name", ref_name)
        pulumi.set(__self__, "ref_type", ref_type)
        pulumi.set(__self__, "selector", selector)

    @property
    @pulumi.getter(name="refName")
    def ref_name(self) -> str:
        return pulumi.get(self, "ref_name")

    @property
    @pulumi.getter(name="refType")
    def ref_type(self) -> str:
        return pulumi.get(self, "ref_type")

    @property
    @pulumi.getter
    def selector(self) -> 'outputs.PipelineScheduleTargetSelector':
        return pulumi.get(self, "selector")


@pulumi.output_type
class PipelineScheduleTargetSelector(dict):
    def __init__(__self__, *,
                 pattern: str,
                 type: Optional[str] = None):
        pulumi.set(__self__, "pattern", pattern)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def pattern(self) -> str:
        return pulumi.get(self, "pattern")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


@pulumi.output_type
class PipelineSshKnownHostPublicKey(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyType":
            suggest = "key_type"
        elif key == "md5Fingerprint":
            suggest = "md5_fingerprint"
        elif key == "sha256Fingerprint":
            suggest = "sha256_fingerprint"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PipelineSshKnownHostPublicKey. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PipelineSshKnownHostPublicKey.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PipelineSshKnownHostPublicKey.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key: str,
                 key_type: str,
                 md5_fingerprint: Optional[str] = None,
                 sha256_fingerprint: Optional[str] = None):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "key_type", key_type)
        if md5_fingerprint is not None:
            pulumi.set(__self__, "md5_fingerprint", md5_fingerprint)
        if sha256_fingerprint is not None:
            pulumi.set(__self__, "sha256_fingerprint", sha256_fingerprint)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="keyType")
    def key_type(self) -> str:
        return pulumi.get(self, "key_type")

    @property
    @pulumi.getter(name="md5Fingerprint")
    def md5_fingerprint(self) -> Optional[str]:
        return pulumi.get(self, "md5_fingerprint")

    @property
    @pulumi.getter(name="sha256Fingerprint")
    def sha256_fingerprint(self) -> Optional[str]:
        return pulumi.get(self, "sha256_fingerprint")


@pulumi.output_type
class ProjectBranchingModelBranchType(dict):
    def __init__(__self__, *,
                 kind: str,
                 enabled: Optional[bool] = None,
                 prefix: Optional[str] = None):
        pulumi.set(__self__, "kind", kind)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if prefix is not None:
            pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter
    def kind(self) -> str:
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        return pulumi.get(self, "prefix")


@pulumi.output_type
class ProjectBranchingModelDevelopment(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "branchDoesNotExist":
            suggest = "branch_does_not_exist"
        elif key == "isValid":
            suggest = "is_valid"
        elif key == "useMainbranch":
            suggest = "use_mainbranch"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectBranchingModelDevelopment. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectBranchingModelDevelopment.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectBranchingModelDevelopment.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 branch_does_not_exist: Optional[bool] = None,
                 is_valid: Optional[bool] = None,
                 name: Optional[str] = None,
                 use_mainbranch: Optional[bool] = None):
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
    def branch_does_not_exist(self) -> Optional[bool]:
        return pulumi.get(self, "branch_does_not_exist")

    @property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> Optional[bool]:
        return pulumi.get(self, "is_valid")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="useMainbranch")
    def use_mainbranch(self) -> Optional[bool]:
        return pulumi.get(self, "use_mainbranch")


@pulumi.output_type
class ProjectBranchingModelProduction(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "branchDoesNotExist":
            suggest = "branch_does_not_exist"
        elif key == "isValid":
            suggest = "is_valid"
        elif key == "useMainbranch":
            suggest = "use_mainbranch"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ProjectBranchingModelProduction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ProjectBranchingModelProduction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ProjectBranchingModelProduction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 branch_does_not_exist: Optional[bool] = None,
                 enabled: Optional[bool] = None,
                 is_valid: Optional[bool] = None,
                 name: Optional[str] = None,
                 use_mainbranch: Optional[bool] = None):
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
    def branch_does_not_exist(self) -> Optional[bool]:
        return pulumi.get(self, "branch_does_not_exist")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="isValid")
    def is_valid(self) -> Optional[bool]:
        return pulumi.get(self, "is_valid")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="useMainbranch")
    def use_mainbranch(self) -> Optional[bool]:
        return pulumi.get(self, "use_mainbranch")


@pulumi.output_type
class ProjectLink(dict):
    def __init__(__self__, *,
                 avatar: Optional['outputs.ProjectLinkAvatar'] = None):
        if avatar is not None:
            pulumi.set(__self__, "avatar", avatar)

    @property
    @pulumi.getter
    def avatar(self) -> Optional['outputs.ProjectLinkAvatar']:
        return pulumi.get(self, "avatar")


@pulumi.output_type
class ProjectLinkAvatar(dict):
    def __init__(__self__, *,
                 href: Optional[str] = None):
        if href is not None:
            pulumi.set(__self__, "href", href)

    @property
    @pulumi.getter
    def href(self) -> Optional[str]:
        return pulumi.get(self, "href")


@pulumi.output_type
class RepositoryLink(dict):
    def __init__(__self__, *,
                 avatar: Optional['outputs.RepositoryLinkAvatar'] = None):
        if avatar is not None:
            pulumi.set(__self__, "avatar", avatar)

    @property
    @pulumi.getter
    def avatar(self) -> Optional['outputs.RepositoryLinkAvatar']:
        return pulumi.get(self, "avatar")


@pulumi.output_type
class RepositoryLinkAvatar(dict):
    def __init__(__self__, *,
                 href: Optional[str] = None):
        if href is not None:
            pulumi.set(__self__, "href", href)

    @property
    @pulumi.getter
    def href(self) -> Optional[str]:
        return pulumi.get(self, "href")


@pulumi.output_type
class GetCurrentUserEmailResult(dict):
    def __init__(__self__, *,
                 email: str,
                 is_confirmed: bool,
                 is_primary: bool):
        pulumi.set(__self__, "email", email)
        pulumi.set(__self__, "is_confirmed", is_confirmed)
        pulumi.set(__self__, "is_primary", is_primary)

    @property
    @pulumi.getter
    def email(self) -> str:
        return pulumi.get(self, "email")

    @property
    @pulumi.getter(name="isConfirmed")
    def is_confirmed(self) -> bool:
        return pulumi.get(self, "is_confirmed")

    @property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> bool:
        return pulumi.get(self, "is_primary")


@pulumi.output_type
class GetGroupsGroupResult(dict):
    def __init__(__self__, *,
                 auto_add: bool,
                 email_forwarding_disabled: bool,
                 name: str,
                 permission: str,
                 slug: str):
        pulumi.set(__self__, "auto_add", auto_add)
        pulumi.set(__self__, "email_forwarding_disabled", email_forwarding_disabled)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "permission", permission)
        pulumi.set(__self__, "slug", slug)

    @property
    @pulumi.getter(name="autoAdd")
    def auto_add(self) -> bool:
        return pulumi.get(self, "auto_add")

    @property
    @pulumi.getter(name="emailForwardingDisabled")
    def email_forwarding_disabled(self) -> bool:
        return pulumi.get(self, "email_forwarding_disabled")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def permission(self) -> str:
        return pulumi.get(self, "permission")

    @property
    @pulumi.getter
    def slug(self) -> str:
        return pulumi.get(self, "slug")


@pulumi.output_type
class GetHookTypesHookTypeResult(dict):
    def __init__(__self__, *,
                 category: str,
                 description: str,
                 event: str,
                 label: str):
        pulumi.set(__self__, "category", category)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "event", event)
        pulumi.set(__self__, "label", label)

    @property
    @pulumi.getter
    def category(self) -> str:
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def event(self) -> str:
        return pulumi.get(self, "event")

    @property
    @pulumi.getter
    def label(self) -> str:
        return pulumi.get(self, "label")


@pulumi.output_type
class GetIpRangesRangeResult(dict):
    def __init__(__self__, *,
                 cidr: str,
                 directions: Sequence[str],
                 mask: str,
                 mask_len: int,
                 network: str,
                 products: Sequence[str],
                 regions: Sequence[str]):
        pulumi.set(__self__, "cidr", cidr)
        pulumi.set(__self__, "directions", directions)
        pulumi.set(__self__, "mask", mask)
        pulumi.set(__self__, "mask_len", mask_len)
        pulumi.set(__self__, "network", network)
        pulumi.set(__self__, "products", products)
        pulumi.set(__self__, "regions", regions)

    @property
    @pulumi.getter
    def cidr(self) -> str:
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter
    def directions(self) -> Sequence[str]:
        return pulumi.get(self, "directions")

    @property
    @pulumi.getter
    def mask(self) -> str:
        return pulumi.get(self, "mask")

    @property
    @pulumi.getter(name="maskLen")
    def mask_len(self) -> int:
        return pulumi.get(self, "mask_len")

    @property
    @pulumi.getter
    def network(self) -> str:
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def products(self) -> Sequence[str]:
        return pulumi.get(self, "products")

    @property
    @pulumi.getter
    def regions(self) -> Sequence[str]:
        return pulumi.get(self, "regions")


