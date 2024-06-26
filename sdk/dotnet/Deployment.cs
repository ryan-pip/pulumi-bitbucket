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
    /// This resource allows you to setup pipelines deployment environments.
    /// 
    /// OAuth2 Scopes: `none`
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
    ///     var monorepo = new Bitbucket.Repository("monorepo", new()
    ///     {
    ///         Owner = "gob",
    ///         PipelinesEnabled = true,
    ///     });
    /// 
    ///     var test = new Bitbucket.Deployment("test", new()
    ///     {
    ///         Repository = monorepo.Id,
    ///         Stage = "Test",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Deployments can be imported using their `repository/uuid` ID, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import bitbucket:index/deployment:Deployment example repository/uuid
    /// ```
    /// </summary>
    [BitbucketResourceType("bitbucket:index/deployment:Deployment")]
    public partial class Deployment : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the deployment environment
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The repository ID to which you want to assign this deployment environment to
        /// </summary>
        [Output("repository")]
        public Output<string> Repository { get; private set; } = null!;

        /// <summary>
        /// Deployment restrictions. See Restrictions below.
        /// </summary>
        [Output("restrictions")]
        public Output<Outputs.DeploymentRestrictions> Restrictions { get; private set; } = null!;

        /// <summary>
        /// The stage (Test, Staging, Production)
        /// </summary>
        [Output("stage")]
        public Output<string> Stage { get; private set; } = null!;

        /// <summary>
        /// (Computed) The UUID identifying the deployment.
        /// </summary>
        [Output("uuid")]
        public Output<string> Uuid { get; private set; } = null!;


        /// <summary>
        /// Create a Deployment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Deployment(string name, DeploymentArgs args, CustomResourceOptions? options = null)
            : base("bitbucket:index/deployment:Deployment", name, args ?? new DeploymentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Deployment(string name, Input<string> id, DeploymentState? state = null, CustomResourceOptions? options = null)
            : base("bitbucket:index/deployment:Deployment", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Deployment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Deployment Get(string name, Input<string> id, DeploymentState? state = null, CustomResourceOptions? options = null)
        {
            return new Deployment(name, id, state, options);
        }
    }

    public sealed class DeploymentArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the deployment environment
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The repository ID to which you want to assign this deployment environment to
        /// </summary>
        [Input("repository", required: true)]
        public Input<string> Repository { get; set; } = null!;

        /// <summary>
        /// Deployment restrictions. See Restrictions below.
        /// </summary>
        [Input("restrictions")]
        public Input<Inputs.DeploymentRestrictionsArgs>? Restrictions { get; set; }

        /// <summary>
        /// The stage (Test, Staging, Production)
        /// </summary>
        [Input("stage", required: true)]
        public Input<string> Stage { get; set; } = null!;

        public DeploymentArgs()
        {
        }
        public static new DeploymentArgs Empty => new DeploymentArgs();
    }

    public sealed class DeploymentState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the deployment environment
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The repository ID to which you want to assign this deployment environment to
        /// </summary>
        [Input("repository")]
        public Input<string>? Repository { get; set; }

        /// <summary>
        /// Deployment restrictions. See Restrictions below.
        /// </summary>
        [Input("restrictions")]
        public Input<Inputs.DeploymentRestrictionsGetArgs>? Restrictions { get; set; }

        /// <summary>
        /// The stage (Test, Staging, Production)
        /// </summary>
        [Input("stage")]
        public Input<string>? Stage { get; set; }

        /// <summary>
        /// (Computed) The UUID identifying the deployment.
        /// </summary>
        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        public DeploymentState()
        {
        }
        public static new DeploymentState Empty => new DeploymentState();
    }
}
