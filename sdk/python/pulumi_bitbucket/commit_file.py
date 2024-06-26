# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['CommitFileArgs', 'CommitFile']

@pulumi.input_type
class CommitFileArgs:
    def __init__(__self__, *,
                 branch: pulumi.Input[str],
                 commit_author: pulumi.Input[str],
                 commit_message: pulumi.Input[str],
                 content: pulumi.Input[str],
                 filename: pulumi.Input[str],
                 repo_slug: pulumi.Input[str],
                 workspace: pulumi.Input[str]):
        """
        The set of arguments for constructing a CommitFile resource.
        :param pulumi.Input[str] branch: Git branch.
        :param pulumi.Input[str] commit_author: Committer author to use.
        :param pulumi.Input[str] commit_message: The message of the commit.
        :param pulumi.Input[str] content: The file content.
        :param pulumi.Input[str] filename: The path of the file to manage.
        :param pulumi.Input[str] repo_slug: The repository slug.
        :param pulumi.Input[str] workspace: The workspace id.
        """
        pulumi.set(__self__, "branch", branch)
        pulumi.set(__self__, "commit_author", commit_author)
        pulumi.set(__self__, "commit_message", commit_message)
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "filename", filename)
        pulumi.set(__self__, "repo_slug", repo_slug)
        pulumi.set(__self__, "workspace", workspace)

    @property
    @pulumi.getter
    def branch(self) -> pulumi.Input[str]:
        """
        Git branch.
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: pulumi.Input[str]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter(name="commitAuthor")
    def commit_author(self) -> pulumi.Input[str]:
        """
        Committer author to use.
        """
        return pulumi.get(self, "commit_author")

    @commit_author.setter
    def commit_author(self, value: pulumi.Input[str]):
        pulumi.set(self, "commit_author", value)

    @property
    @pulumi.getter(name="commitMessage")
    def commit_message(self) -> pulumi.Input[str]:
        """
        The message of the commit.
        """
        return pulumi.get(self, "commit_message")

    @commit_message.setter
    def commit_message(self, value: pulumi.Input[str]):
        pulumi.set(self, "commit_message", value)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        The file content.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def filename(self) -> pulumi.Input[str]:
        """
        The path of the file to manage.
        """
        return pulumi.get(self, "filename")

    @filename.setter
    def filename(self, value: pulumi.Input[str]):
        pulumi.set(self, "filename", value)

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
class _CommitFileState:
    def __init__(__self__, *,
                 branch: Optional[pulumi.Input[str]] = None,
                 commit_author: Optional[pulumi.Input[str]] = None,
                 commit_message: Optional[pulumi.Input[str]] = None,
                 commit_sha: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 filename: Optional[pulumi.Input[str]] = None,
                 repo_slug: Optional[pulumi.Input[str]] = None,
                 workspace: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering CommitFile resources.
        :param pulumi.Input[str] branch: Git branch.
        :param pulumi.Input[str] commit_author: Committer author to use.
        :param pulumi.Input[str] commit_message: The message of the commit.
        :param pulumi.Input[str] commit_sha: The SHA of the commit that modified the file
        :param pulumi.Input[str] content: The file content.
        :param pulumi.Input[str] filename: The path of the file to manage.
        :param pulumi.Input[str] repo_slug: The repository slug.
        :param pulumi.Input[str] workspace: The workspace id.
        """
        if branch is not None:
            pulumi.set(__self__, "branch", branch)
        if commit_author is not None:
            pulumi.set(__self__, "commit_author", commit_author)
        if commit_message is not None:
            pulumi.set(__self__, "commit_message", commit_message)
        if commit_sha is not None:
            pulumi.set(__self__, "commit_sha", commit_sha)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if filename is not None:
            pulumi.set(__self__, "filename", filename)
        if repo_slug is not None:
            pulumi.set(__self__, "repo_slug", repo_slug)
        if workspace is not None:
            pulumi.set(__self__, "workspace", workspace)

    @property
    @pulumi.getter
    def branch(self) -> Optional[pulumi.Input[str]]:
        """
        Git branch.
        """
        return pulumi.get(self, "branch")

    @branch.setter
    def branch(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch", value)

    @property
    @pulumi.getter(name="commitAuthor")
    def commit_author(self) -> Optional[pulumi.Input[str]]:
        """
        Committer author to use.
        """
        return pulumi.get(self, "commit_author")

    @commit_author.setter
    def commit_author(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "commit_author", value)

    @property
    @pulumi.getter(name="commitMessage")
    def commit_message(self) -> Optional[pulumi.Input[str]]:
        """
        The message of the commit.
        """
        return pulumi.get(self, "commit_message")

    @commit_message.setter
    def commit_message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "commit_message", value)

    @property
    @pulumi.getter(name="commitSha")
    def commit_sha(self) -> Optional[pulumi.Input[str]]:
        """
        The SHA of the commit that modified the file
        """
        return pulumi.get(self, "commit_sha")

    @commit_sha.setter
    def commit_sha(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "commit_sha", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        The file content.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def filename(self) -> Optional[pulumi.Input[str]]:
        """
        The path of the file to manage.
        """
        return pulumi.get(self, "filename")

    @filename.setter
    def filename(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filename", value)

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
    @pulumi.getter
    def workspace(self) -> Optional[pulumi.Input[str]]:
        """
        The workspace id.
        """
        return pulumi.get(self, "workspace")

    @workspace.setter
    def workspace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace", value)


class CommitFile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 commit_author: Optional[pulumi.Input[str]] = None,
                 commit_message: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 filename: Optional[pulumi.Input[str]] = None,
                 repo_slug: Optional[pulumi.Input[str]] = None,
                 workspace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Commit a file.

        This resource allows you to create a commit within a Bitbucket repository.

        OAuth2 Scopes: `repository:write`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_bitbucket as bitbucket

        test = bitbucket.CommitFile("test",
            branch="main",
            commit_author="Test <test@test.local>",
            commit_message="test",
            content="abc",
            filename="README.md",
            repo_slug="test",
            workspace="test")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch: Git branch.
        :param pulumi.Input[str] commit_author: Committer author to use.
        :param pulumi.Input[str] commit_message: The message of the commit.
        :param pulumi.Input[str] content: The file content.
        :param pulumi.Input[str] filename: The path of the file to manage.
        :param pulumi.Input[str] repo_slug: The repository slug.
        :param pulumi.Input[str] workspace: The workspace id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CommitFileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Commit a file.

        This resource allows you to create a commit within a Bitbucket repository.

        OAuth2 Scopes: `repository:write`

        ## Example Usage

        ```python
        import pulumi
        import pulumi_bitbucket as bitbucket

        test = bitbucket.CommitFile("test",
            branch="main",
            commit_author="Test <test@test.local>",
            commit_message="test",
            content="abc",
            filename="README.md",
            repo_slug="test",
            workspace="test")
        ```

        :param str resource_name: The name of the resource.
        :param CommitFileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CommitFileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 branch: Optional[pulumi.Input[str]] = None,
                 commit_author: Optional[pulumi.Input[str]] = None,
                 commit_message: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 filename: Optional[pulumi.Input[str]] = None,
                 repo_slug: Optional[pulumi.Input[str]] = None,
                 workspace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CommitFileArgs.__new__(CommitFileArgs)

            if branch is None and not opts.urn:
                raise TypeError("Missing required property 'branch'")
            __props__.__dict__["branch"] = branch
            if commit_author is None and not opts.urn:
                raise TypeError("Missing required property 'commit_author'")
            __props__.__dict__["commit_author"] = commit_author
            if commit_message is None and not opts.urn:
                raise TypeError("Missing required property 'commit_message'")
            __props__.__dict__["commit_message"] = commit_message
            if content is None and not opts.urn:
                raise TypeError("Missing required property 'content'")
            __props__.__dict__["content"] = content
            if filename is None and not opts.urn:
                raise TypeError("Missing required property 'filename'")
            __props__.__dict__["filename"] = filename
            if repo_slug is None and not opts.urn:
                raise TypeError("Missing required property 'repo_slug'")
            __props__.__dict__["repo_slug"] = repo_slug
            if workspace is None and not opts.urn:
                raise TypeError("Missing required property 'workspace'")
            __props__.__dict__["workspace"] = workspace
            __props__.__dict__["commit_sha"] = None
        super(CommitFile, __self__).__init__(
            'bitbucket:index/commitFile:CommitFile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            branch: Optional[pulumi.Input[str]] = None,
            commit_author: Optional[pulumi.Input[str]] = None,
            commit_message: Optional[pulumi.Input[str]] = None,
            commit_sha: Optional[pulumi.Input[str]] = None,
            content: Optional[pulumi.Input[str]] = None,
            filename: Optional[pulumi.Input[str]] = None,
            repo_slug: Optional[pulumi.Input[str]] = None,
            workspace: Optional[pulumi.Input[str]] = None) -> 'CommitFile':
        """
        Get an existing CommitFile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] branch: Git branch.
        :param pulumi.Input[str] commit_author: Committer author to use.
        :param pulumi.Input[str] commit_message: The message of the commit.
        :param pulumi.Input[str] commit_sha: The SHA of the commit that modified the file
        :param pulumi.Input[str] content: The file content.
        :param pulumi.Input[str] filename: The path of the file to manage.
        :param pulumi.Input[str] repo_slug: The repository slug.
        :param pulumi.Input[str] workspace: The workspace id.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CommitFileState.__new__(_CommitFileState)

        __props__.__dict__["branch"] = branch
        __props__.__dict__["commit_author"] = commit_author
        __props__.__dict__["commit_message"] = commit_message
        __props__.__dict__["commit_sha"] = commit_sha
        __props__.__dict__["content"] = content
        __props__.__dict__["filename"] = filename
        __props__.__dict__["repo_slug"] = repo_slug
        __props__.__dict__["workspace"] = workspace
        return CommitFile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def branch(self) -> pulumi.Output[str]:
        """
        Git branch.
        """
        return pulumi.get(self, "branch")

    @property
    @pulumi.getter(name="commitAuthor")
    def commit_author(self) -> pulumi.Output[str]:
        """
        Committer author to use.
        """
        return pulumi.get(self, "commit_author")

    @property
    @pulumi.getter(name="commitMessage")
    def commit_message(self) -> pulumi.Output[str]:
        """
        The message of the commit.
        """
        return pulumi.get(self, "commit_message")

    @property
    @pulumi.getter(name="commitSha")
    def commit_sha(self) -> pulumi.Output[str]:
        """
        The SHA of the commit that modified the file
        """
        return pulumi.get(self, "commit_sha")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[str]:
        """
        The file content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter
    def filename(self) -> pulumi.Output[str]:
        """
        The path of the file to manage.
        """
        return pulumi.get(self, "filename")

    @property
    @pulumi.getter(name="repoSlug")
    def repo_slug(self) -> pulumi.Output[str]:
        """
        The repository slug.
        """
        return pulumi.get(self, "repo_slug")

    @property
    @pulumi.getter
    def workspace(self) -> pulumi.Output[str]:
        """
        The workspace id.
        """
        return pulumi.get(self, "workspace")

