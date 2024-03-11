// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Bitbucket workspace hook resource.
 *
 * This allows you to manage your webhooks on a workspace.
 *
 * OAuth2 Scopes: `webhook`
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as bitbucket from "@ryan-pip/pulumi_bitbucket";
 *
 * const deployOnPush = new bitbucket.WorkspaceHook("deployOnPush", {
 *     description: "Deploy the code via my webhook",
 *     events: ["repo:push"],
 *     url: "https://mywebhookservice.mycompany.com/deploy-on-push",
 *     workspace: "myteam",
 * });
 * ```
 *
 * ## Import
 *
 * Hooks can be imported using their `workspace/hook-id` ID, e.g.
 *
 * ```sh
 *  $ pulumi import bitbucket:index/workspaceHook:WorkspaceHook hook my-account/hook-id
 * ```
 */
export class WorkspaceHook extends pulumi.CustomResource {
    /**
     * Get an existing WorkspaceHook resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WorkspaceHookState, opts?: pulumi.CustomResourceOptions): WorkspaceHook {
        return new WorkspaceHook(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'bitbucket:index/workspaceHook:WorkspaceHook';

    /**
     * Returns true if the given object is an instance of WorkspaceHook.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is WorkspaceHook {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === WorkspaceHook.__pulumiType;
    }

    /**
     * Whether the webhook configuration is active or not (Default: `true`).
     */
    public readonly active!: pulumi.Output<boolean | undefined>;
    /**
     * The name / description to show in the UI.
     */
    public readonly description!: pulumi.Output<string>;
    /**
     * The events this webhook is subscribed to. Valid values can be found at [Bitbucket Webhook Docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-post).
     */
    public readonly events!: pulumi.Output<string[]>;
    /**
     * Whether a webhook history is enabled.
     */
    public readonly historyEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * A Webhook secret value. Passing a null or empty secret or not passing a secret will leave the webhook's secret unset. This value is not returned on read and cannot resolve diffs or be imported as its not returned back from bitbucket API.
     */
    public readonly secret!: pulumi.Output<string | undefined>;
    /**
     * Whether a webhook secret is set.
     */
    public /*out*/ readonly secretSet!: pulumi.Output<boolean>;
    /**
     * Whether to skip certificate verification or not (Default: `true`).
     */
    public readonly skipCertVerification!: pulumi.Output<boolean | undefined>;
    /**
     * Where to POST to.
     */
    public readonly url!: pulumi.Output<string>;
    /**
     * The UUID of the workspace webhook.
     */
    public /*out*/ readonly uuid!: pulumi.Output<string>;
    /**
     * The workspace of this repository. Can be you or any team you
     * have write access to.
     */
    public readonly workspace!: pulumi.Output<string>;

    /**
     * Create a WorkspaceHook resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: WorkspaceHookArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: WorkspaceHookArgs | WorkspaceHookState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as WorkspaceHookState | undefined;
            resourceInputs["active"] = state ? state.active : undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["events"] = state ? state.events : undefined;
            resourceInputs["historyEnabled"] = state ? state.historyEnabled : undefined;
            resourceInputs["secret"] = state ? state.secret : undefined;
            resourceInputs["secretSet"] = state ? state.secretSet : undefined;
            resourceInputs["skipCertVerification"] = state ? state.skipCertVerification : undefined;
            resourceInputs["url"] = state ? state.url : undefined;
            resourceInputs["uuid"] = state ? state.uuid : undefined;
            resourceInputs["workspace"] = state ? state.workspace : undefined;
        } else {
            const args = argsOrState as WorkspaceHookArgs | undefined;
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            if ((!args || args.events === undefined) && !opts.urn) {
                throw new Error("Missing required property 'events'");
            }
            if ((!args || args.url === undefined) && !opts.urn) {
                throw new Error("Missing required property 'url'");
            }
            if ((!args || args.workspace === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workspace'");
            }
            resourceInputs["active"] = args ? args.active : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["events"] = args ? args.events : undefined;
            resourceInputs["historyEnabled"] = args ? args.historyEnabled : undefined;
            resourceInputs["secret"] = args?.secret ? pulumi.secret(args.secret) : undefined;
            resourceInputs["skipCertVerification"] = args ? args.skipCertVerification : undefined;
            resourceInputs["url"] = args ? args.url : undefined;
            resourceInputs["workspace"] = args ? args.workspace : undefined;
            resourceInputs["secretSet"] = undefined /*out*/;
            resourceInputs["uuid"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["secret"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(WorkspaceHook.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering WorkspaceHook resources.
 */
export interface WorkspaceHookState {
    /**
     * Whether the webhook configuration is active or not (Default: `true`).
     */
    active?: pulumi.Input<boolean>;
    /**
     * The name / description to show in the UI.
     */
    description?: pulumi.Input<string>;
    /**
     * The events this webhook is subscribed to. Valid values can be found at [Bitbucket Webhook Docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-post).
     */
    events?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Whether a webhook history is enabled.
     */
    historyEnabled?: pulumi.Input<boolean>;
    /**
     * A Webhook secret value. Passing a null or empty secret or not passing a secret will leave the webhook's secret unset. This value is not returned on read and cannot resolve diffs or be imported as its not returned back from bitbucket API.
     */
    secret?: pulumi.Input<string>;
    /**
     * Whether a webhook secret is set.
     */
    secretSet?: pulumi.Input<boolean>;
    /**
     * Whether to skip certificate verification or not (Default: `true`).
     */
    skipCertVerification?: pulumi.Input<boolean>;
    /**
     * Where to POST to.
     */
    url?: pulumi.Input<string>;
    /**
     * The UUID of the workspace webhook.
     */
    uuid?: pulumi.Input<string>;
    /**
     * The workspace of this repository. Can be you or any team you
     * have write access to.
     */
    workspace?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a WorkspaceHook resource.
 */
export interface WorkspaceHookArgs {
    /**
     * Whether the webhook configuration is active or not (Default: `true`).
     */
    active?: pulumi.Input<boolean>;
    /**
     * The name / description to show in the UI.
     */
    description: pulumi.Input<string>;
    /**
     * The events this webhook is subscribed to. Valid values can be found at [Bitbucket Webhook Docs](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-hooks-post).
     */
    events: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Whether a webhook history is enabled.
     */
    historyEnabled?: pulumi.Input<boolean>;
    /**
     * A Webhook secret value. Passing a null or empty secret or not passing a secret will leave the webhook's secret unset. This value is not returned on read and cannot resolve diffs or be imported as its not returned back from bitbucket API.
     */
    secret?: pulumi.Input<string>;
    /**
     * Whether to skip certificate verification or not (Default: `true`).
     */
    skipCertVerification?: pulumi.Input<boolean>;
    /**
     * Where to POST to.
     */
    url: pulumi.Input<string>;
    /**
     * The workspace of this repository. Can be you or any team you
     * have write access to.
     */
    workspace: pulumi.Input<string>;
}
