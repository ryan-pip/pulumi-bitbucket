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
    /// Provides a Bitbucket hook resource.
    /// 
    /// This allows you to manage your webhooks on a repository.
    /// 
    /// OAuth2 Scopes: `webhook`
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
    ///     var deployOnPush = new Bitbucket.Hook("deployOnPush", new()
    ///     {
    ///         Description = "Deploy the code via my webhook",
    ///         Events = new[]
    ///         {
    ///             "repo:push",
    ///         },
    ///         Owner = "myteam",
    ///         Repository = "terraform-code",
    ///         Url = "https://mywebhookservice.mycompany.com/deploy-on-push",
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// Hooks can be imported using their `owner/repo-name/hook-id` ID, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import bitbucket:index/hook:Hook hook my-account/my-repo/hook-id
    /// ```
    /// </summary>
    [BitbucketResourceType("bitbucket:index/hook:Hook")]
    public partial class Hook : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Whether the webhook configuration is active or not (Default: `true`).
        /// </summary>
        [Output("active")]
        public Output<bool?> Active { get; private set; } = null!;

        /// <summary>
        /// The name / description to show in the UI.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The events this webhook is subscribed to. Valid values can be found at [Bitbucket Event Payloads Docs](https://support.atlassian.com/bitbucket-cloud/docs/event-payloads/).
        /// </summary>
        [Output("events")]
        public Output<ImmutableArray<string>> Events { get; private set; } = null!;

        /// <summary>
        /// Whether a webhook history is enabled.
        /// </summary>
        [Output("historyEnabled")]
        public Output<bool?> HistoryEnabled { get; private set; } = null!;

        /// <summary>
        /// The owner of this repository. Can be you or any team you
        /// have write access to.
        /// </summary>
        [Output("owner")]
        public Output<string> Owner { get; private set; } = null!;

        /// <summary>
        /// The name of the repository.
        /// </summary>
        [Output("repository")]
        public Output<string> Repository { get; private set; } = null!;

        /// <summary>
        /// A Webhook secret value. Passing a null or empty secret or not passing a secret will leave the webhook's secret unset. This value is not returned on read and cannot resolve diffs or be imported as its not returned back from bitbucket API.
        /// </summary>
        [Output("secret")]
        public Output<string?> Secret { get; private set; } = null!;

        /// <summary>
        /// Whether a webhook secret is set.
        /// </summary>
        [Output("secretSet")]
        public Output<bool> SecretSet { get; private set; } = null!;

        /// <summary>
        /// Whether to skip certificate verification or not (Default: `true`).
        /// </summary>
        [Output("skipCertVerification")]
        public Output<bool?> SkipCertVerification { get; private set; } = null!;

        /// <summary>
        /// Where to POST to.
        /// </summary>
        [Output("url")]
        public Output<string> Url { get; private set; } = null!;

        /// <summary>
        /// The UUID of the workspace webhook.
        /// </summary>
        [Output("uuid")]
        public Output<string> Uuid { get; private set; } = null!;


        /// <summary>
        /// Create a Hook resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Hook(string name, HookArgs args, CustomResourceOptions? options = null)
            : base("bitbucket:index/hook:Hook", name, args ?? new HookArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Hook(string name, Input<string> id, HookState? state = null, CustomResourceOptions? options = null)
            : base("bitbucket:index/hook:Hook", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/ryan-pip",
                AdditionalSecretOutputs =
                {
                    "secret",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Hook resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Hook Get(string name, Input<string> id, HookState? state = null, CustomResourceOptions? options = null)
        {
            return new Hook(name, id, state, options);
        }
    }

    public sealed class HookArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether the webhook configuration is active or not (Default: `true`).
        /// </summary>
        [Input("active")]
        public Input<bool>? Active { get; set; }

        /// <summary>
        /// The name / description to show in the UI.
        /// </summary>
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        [Input("events", required: true)]
        private InputList<string>? _events;

        /// <summary>
        /// The events this webhook is subscribed to. Valid values can be found at [Bitbucket Event Payloads Docs](https://support.atlassian.com/bitbucket-cloud/docs/event-payloads/).
        /// </summary>
        public InputList<string> Events
        {
            get => _events ?? (_events = new InputList<string>());
            set => _events = value;
        }

        /// <summary>
        /// Whether a webhook history is enabled.
        /// </summary>
        [Input("historyEnabled")]
        public Input<bool>? HistoryEnabled { get; set; }

        /// <summary>
        /// The owner of this repository. Can be you or any team you
        /// have write access to.
        /// </summary>
        [Input("owner", required: true)]
        public Input<string> Owner { get; set; } = null!;

        /// <summary>
        /// The name of the repository.
        /// </summary>
        [Input("repository", required: true)]
        public Input<string> Repository { get; set; } = null!;

        [Input("secret")]
        private Input<string>? _secret;

        /// <summary>
        /// A Webhook secret value. Passing a null or empty secret or not passing a secret will leave the webhook's secret unset. This value is not returned on read and cannot resolve diffs or be imported as its not returned back from bitbucket API.
        /// </summary>
        public Input<string>? Secret
        {
            get => _secret;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _secret = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Whether to skip certificate verification or not (Default: `true`).
        /// </summary>
        [Input("skipCertVerification")]
        public Input<bool>? SkipCertVerification { get; set; }

        /// <summary>
        /// Where to POST to.
        /// </summary>
        [Input("url", required: true)]
        public Input<string> Url { get; set; } = null!;

        public HookArgs()
        {
        }
        public static new HookArgs Empty => new HookArgs();
    }

    public sealed class HookState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether the webhook configuration is active or not (Default: `true`).
        /// </summary>
        [Input("active")]
        public Input<bool>? Active { get; set; }

        /// <summary>
        /// The name / description to show in the UI.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("events")]
        private InputList<string>? _events;

        /// <summary>
        /// The events this webhook is subscribed to. Valid values can be found at [Bitbucket Event Payloads Docs](https://support.atlassian.com/bitbucket-cloud/docs/event-payloads/).
        /// </summary>
        public InputList<string> Events
        {
            get => _events ?? (_events = new InputList<string>());
            set => _events = value;
        }

        /// <summary>
        /// Whether a webhook history is enabled.
        /// </summary>
        [Input("historyEnabled")]
        public Input<bool>? HistoryEnabled { get; set; }

        /// <summary>
        /// The owner of this repository. Can be you or any team you
        /// have write access to.
        /// </summary>
        [Input("owner")]
        public Input<string>? Owner { get; set; }

        /// <summary>
        /// The name of the repository.
        /// </summary>
        [Input("repository")]
        public Input<string>? Repository { get; set; }

        [Input("secret")]
        private Input<string>? _secret;

        /// <summary>
        /// A Webhook secret value. Passing a null or empty secret or not passing a secret will leave the webhook's secret unset. This value is not returned on read and cannot resolve diffs or be imported as its not returned back from bitbucket API.
        /// </summary>
        public Input<string>? Secret
        {
            get => _secret;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _secret = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Whether a webhook secret is set.
        /// </summary>
        [Input("secretSet")]
        public Input<bool>? SecretSet { get; set; }

        /// <summary>
        /// Whether to skip certificate verification or not (Default: `true`).
        /// </summary>
        [Input("skipCertVerification")]
        public Input<bool>? SkipCertVerification { get; set; }

        /// <summary>
        /// Where to POST to.
        /// </summary>
        [Input("url")]
        public Input<string>? Url { get; set; }

        /// <summary>
        /// The UUID of the workspace webhook.
        /// </summary>
        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        public HookState()
        {
        }
        public static new HookState Empty => new HookState();
    }
}
