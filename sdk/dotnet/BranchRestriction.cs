// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Bitbucket
{
    /// <summary>
    /// Provides a Bitbucket branch restriction resource.
    /// 
    /// This allows you for setting up branch restrictions for your repository.
    /// 
    /// OAuth2 Scopes: `repository:admin`
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Bitbucket = Pulumi.Bitbucket;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var master = new Bitbucket.BranchRestriction("master", new()
    ///     {
    ///         Groups = new[]
    ///         {
    ///             new Bitbucket.Inputs.BranchRestrictionGroupArgs
    ///             {
    ///                 Owner = "my-owner",
    ///                 Slug = "my-group",
    ///             },
    ///         },
    ///         Kind = "push",
    ///         Owner = "myteam",
    ///         Pattern = "master",
    ///         Repository = "terraform-code",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Branch Restrictions can be imported using their `owner/repo-name/branch-restriction-id` ID, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import bitbucket:index/branchRestriction:BranchRestriction example my-account/my-repo/branch-rest-id
    /// ```
    /// </summary>
    [BitbucketResourceType("bitbucket:index/branchRestriction:BranchRestriction")]
    public partial class BranchRestriction : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Indicates how the restriction is matched against a branch. The default is `glob`. Valid values: `branching_model`, `glob`.
        /// </summary>
        [Output("branchMatchKind")]
        public Output<string?> BranchMatchKind { get; private set; } = null!;

        /// <summary>
        /// Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The branch type will be calculated using the branching model configured for the repository. Valid values: `feature`, `bugfix`, `release`, `hotfix`, `development`, `production`.
        /// </summary>
        [Output("branchType")]
        public Output<string?> BranchType { get; private set; } = null!;

        /// <summary>
        /// A list of groups to use.
        /// </summary>
        [Output("groups")]
        public Output<ImmutableArray<Outputs.BranchRestrictionGroup>> Groups { get; private set; } = null!;

        /// <summary>
        /// The type of restriction that is being applied. Valid values can be found in [docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-group-branch-restrictions).
        /// </summary>
        [Output("kind")]
        public Output<string> Kind { get; private set; } = null!;

        /// <summary>
        /// The owner of this repository. Can be you or any team you
        /// have write access to.
        /// </summary>
        [Output("owner")]
        public Output<string> Owner { get; private set; } = null!;

        /// <summary>
        /// Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will be empty when `branch_match_kind` is `branching_model`.
        /// </summary>
        [Output("pattern")]
        public Output<string?> Pattern { get; private set; } = null!;

        /// <summary>
        /// The name of the repository.
        /// </summary>
        [Output("repository")]
        public Output<string> Repository { get; private set; } = null!;

        /// <summary>
        /// A list of users to use.
        /// </summary>
        [Output("users")]
        public Output<ImmutableArray<string>> Users { get; private set; } = null!;

        /// <summary>
        /// A value applied to the restriction kind. Currently only applicable to `require_passing_builds_to_merge`, `require_default_reviewer_approvals_to_merge` and `require_approvals_to_merge`.
        /// </summary>
        [Output("value")]
        public Output<int?> Value { get; private set; } = null!;


        /// <summary>
        /// Create a BranchRestriction resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BranchRestriction(string name, BranchRestrictionArgs args, CustomResourceOptions? options = null)
            : base("bitbucket:index/branchRestriction:BranchRestriction", name, args ?? new BranchRestrictionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BranchRestriction(string name, Input<string> id, BranchRestrictionState? state = null, CustomResourceOptions? options = null)
            : base("bitbucket:index/branchRestriction:BranchRestriction", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/ryan-pip",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BranchRestriction resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BranchRestriction Get(string name, Input<string> id, BranchRestrictionState? state = null, CustomResourceOptions? options = null)
        {
            return new BranchRestriction(name, id, state, options);
        }
    }

    public sealed class BranchRestrictionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates how the restriction is matched against a branch. The default is `glob`. Valid values: `branching_model`, `glob`.
        /// </summary>
        [Input("branchMatchKind")]
        public Input<string>? BranchMatchKind { get; set; }

        /// <summary>
        /// Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The branch type will be calculated using the branching model configured for the repository. Valid values: `feature`, `bugfix`, `release`, `hotfix`, `development`, `production`.
        /// </summary>
        [Input("branchType")]
        public Input<string>? BranchType { get; set; }

        [Input("groups")]
        private InputList<Inputs.BranchRestrictionGroupArgs>? _groups;

        /// <summary>
        /// A list of groups to use.
        /// </summary>
        public InputList<Inputs.BranchRestrictionGroupArgs> Groups
        {
            get => _groups ?? (_groups = new InputList<Inputs.BranchRestrictionGroupArgs>());
            set => _groups = value;
        }

        /// <summary>
        /// The type of restriction that is being applied. Valid values can be found in [docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-group-branch-restrictions).
        /// </summary>
        [Input("kind", required: true)]
        public Input<string> Kind { get; set; } = null!;

        /// <summary>
        /// The owner of this repository. Can be you or any team you
        /// have write access to.
        /// </summary>
        [Input("owner", required: true)]
        public Input<string> Owner { get; set; } = null!;

        /// <summary>
        /// Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will be empty when `branch_match_kind` is `branching_model`.
        /// </summary>
        [Input("pattern")]
        public Input<string>? Pattern { get; set; }

        /// <summary>
        /// The name of the repository.
        /// </summary>
        [Input("repository", required: true)]
        public Input<string> Repository { get; set; } = null!;

        [Input("users")]
        private InputList<string>? _users;

        /// <summary>
        /// A list of users to use.
        /// </summary>
        public InputList<string> Users
        {
            get => _users ?? (_users = new InputList<string>());
            set => _users = value;
        }

        /// <summary>
        /// A value applied to the restriction kind. Currently only applicable to `require_passing_builds_to_merge`, `require_default_reviewer_approvals_to_merge` and `require_approvals_to_merge`.
        /// </summary>
        [Input("value")]
        public Input<int>? Value { get; set; }

        public BranchRestrictionArgs()
        {
        }
        public static new BranchRestrictionArgs Empty => new BranchRestrictionArgs();
    }

    public sealed class BranchRestrictionState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates how the restriction is matched against a branch. The default is `glob`. Valid values: `branching_model`, `glob`.
        /// </summary>
        [Input("branchMatchKind")]
        public Input<string>? BranchMatchKind { get; set; }

        /// <summary>
        /// Apply the restriction to branches of this type. Active when `branch_match_kind` is `branching_model`. The branch type will be calculated using the branching model configured for the repository. Valid values: `feature`, `bugfix`, `release`, `hotfix`, `development`, `production`.
        /// </summary>
        [Input("branchType")]
        public Input<string>? BranchType { get; set; }

        [Input("groups")]
        private InputList<Inputs.BranchRestrictionGroupGetArgs>? _groups;

        /// <summary>
        /// A list of groups to use.
        /// </summary>
        public InputList<Inputs.BranchRestrictionGroupGetArgs> Groups
        {
            get => _groups ?? (_groups = new InputList<Inputs.BranchRestrictionGroupGetArgs>());
            set => _groups = value;
        }

        /// <summary>
        /// The type of restriction that is being applied. Valid values can be found in [docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-branch-restrictions/#api-group-branch-restrictions).
        /// </summary>
        [Input("kind")]
        public Input<string>? Kind { get; set; }

        /// <summary>
        /// The owner of this repository. Can be you or any team you
        /// have write access to.
        /// </summary>
        [Input("owner")]
        public Input<string>? Owner { get; set; }

        /// <summary>
        /// Apply the restriction to branches that match this pattern. Active when `branch_match_kind` is `glob`. Will be empty when `branch_match_kind` is `branching_model`.
        /// </summary>
        [Input("pattern")]
        public Input<string>? Pattern { get; set; }

        /// <summary>
        /// The name of the repository.
        /// </summary>
        [Input("repository")]
        public Input<string>? Repository { get; set; }

        [Input("users")]
        private InputList<string>? _users;

        /// <summary>
        /// A list of users to use.
        /// </summary>
        public InputList<string> Users
        {
            get => _users ?? (_users = new InputList<string>());
            set => _users = value;
        }

        /// <summary>
        /// A value applied to the restriction kind. Currently only applicable to `require_passing_builds_to_merge`, `require_default_reviewer_approvals_to_merge` and `require_approvals_to_merge`.
        /// </summary>
        [Input("value")]
        public Input<int>? Value { get; set; }

        public BranchRestrictionState()
        {
        }
        public static new BranchRestrictionState Empty => new BranchRestrictionState();
    }
}