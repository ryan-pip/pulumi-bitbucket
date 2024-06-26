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
    /// Provides a Bitbucket Deploy Key resource.
    /// 
    /// This allows you to manage your Deploy Keys for a repository.
    /// 
    /// OAuth2 Scopes: `repository` and `repository:admin`
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
    ///     var test = new Bitbucket.DeployKey("test", new()
    ///     {
    ///         Key = "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKqP3Cr632C2dNhhgKVcon4ldUSAeKiku2yP9O9/bDtY",
    ///         Label = "test-key",
    ///         Repository = "example",
    ///         Workspace = "example",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Deploy Keys can be imported using their `workspace/repo-slug/key-id` ID, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import bitbucket:index/deployKey:DeployKey key workspace/repo-slug/key-id
    /// ```
    /// </summary>
    [BitbucketResourceType("bitbucket:index/deployKey:DeployKey")]
    public partial class DeployKey : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The comment parsed from the Deploy key (if present)
        /// </summary>
        [Output("comment")]
        public Output<string> Comment { get; private set; } = null!;

        /// <summary>
        /// The SSH public key value in OpenSSH format.
        /// </summary>
        [Output("key")]
        public Output<string?> Key { get; private set; } = null!;

        /// <summary>
        /// The Deploy key's ID.
        /// </summary>
        [Output("keyId")]
        public Output<string> KeyId { get; private set; } = null!;

        /// <summary>
        /// The user-defined label for the Deploy key
        /// </summary>
        [Output("label")]
        public Output<string?> Label { get; private set; } = null!;

        /// <summary>
        /// The Repository to create deploy key in.
        /// </summary>
        [Output("repository")]
        public Output<string> Repository { get; private set; } = null!;

        /// <summary>
        /// The Workspace where the repository resides.
        /// </summary>
        [Output("workspace")]
        public Output<string> Workspace { get; private set; } = null!;


        /// <summary>
        /// Create a DeployKey resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DeployKey(string name, DeployKeyArgs args, CustomResourceOptions? options = null)
            : base("bitbucket:index/deployKey:DeployKey", name, args ?? new DeployKeyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DeployKey(string name, Input<string> id, DeployKeyState? state = null, CustomResourceOptions? options = null)
            : base("bitbucket:index/deployKey:DeployKey", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing DeployKey resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DeployKey Get(string name, Input<string> id, DeployKeyState? state = null, CustomResourceOptions? options = null)
        {
            return new DeployKey(name, id, state, options);
        }
    }

    public sealed class DeployKeyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The SSH public key value in OpenSSH format.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        /// <summary>
        /// The user-defined label for the Deploy key
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The Repository to create deploy key in.
        /// </summary>
        [Input("repository", required: true)]
        public Input<string> Repository { get; set; } = null!;

        /// <summary>
        /// The Workspace where the repository resides.
        /// </summary>
        [Input("workspace", required: true)]
        public Input<string> Workspace { get; set; } = null!;

        public DeployKeyArgs()
        {
        }
        public static new DeployKeyArgs Empty => new DeployKeyArgs();
    }

    public sealed class DeployKeyState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The comment parsed from the Deploy key (if present)
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// The SSH public key value in OpenSSH format.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        /// <summary>
        /// The Deploy key's ID.
        /// </summary>
        [Input("keyId")]
        public Input<string>? KeyId { get; set; }

        /// <summary>
        /// The user-defined label for the Deploy key
        /// </summary>
        [Input("label")]
        public Input<string>? Label { get; set; }

        /// <summary>
        /// The Repository to create deploy key in.
        /// </summary>
        [Input("repository")]
        public Input<string>? Repository { get; set; }

        /// <summary>
        /// The Workspace where the repository resides.
        /// </summary>
        [Input("workspace")]
        public Input<string>? Workspace { get; set; }

        public DeployKeyState()
        {
        }
        public static new DeployKeyState Empty => new DeployKeyState();
    }
}
