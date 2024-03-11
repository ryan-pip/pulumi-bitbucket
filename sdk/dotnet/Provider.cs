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
    /// The provider type for the bitbucket package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [BitbucketResourceType("pulumi:providers:bitbucket")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        [Output("oauthClientId")]
        public Output<string?> OauthClientId { get; private set; } = null!;

        [Output("oauthClientSecret")]
        public Output<string?> OauthClientSecret { get; private set; } = null!;

        [Output("oauthToken")]
        public Output<string?> OauthToken { get; private set; } = null!;

        [Output("password")]
        public Output<string?> Password { get; private set; } = null!;

        [Output("username")]
        public Output<string?> Username { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, CustomResourceOptions? options = null)
            : base("bitbucket", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
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
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        [Input("oauthClientId")]
        public Input<string>? OauthClientId { get; set; }

        [Input("oauthClientSecret")]
        public Input<string>? OauthClientSecret { get; set; }

        [Input("oauthToken")]
        public Input<string>? OauthToken { get; set; }

        [Input("password")]
        public Input<string>? Password { get; set; }

        [Input("username")]
        public Input<string>? Username { get; set; }

        public ProviderArgs()
        {
            OauthClientId = Utilities.GetEnv("BITBUCKET_OAUTH_CLIENT_ID");
            OauthClientSecret = Utilities.GetEnv("BITBUCKET_OAUTH_CLIENT_SECRET");
            OauthToken = Utilities.GetEnv("BITBUCKET_OAUTH_TOKEN");
            Password = Utilities.GetEnv("BITBUCKET_PASSWORD");
            Username = Utilities.GetEnv("BITBUCKET_USERNAME");
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
