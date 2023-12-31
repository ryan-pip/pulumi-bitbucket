// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

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

    public readonly active!: pulumi.Output<boolean | undefined>;
    public readonly description!: pulumi.Output<string>;
    public readonly events!: pulumi.Output<string[]>;
    public readonly skipCertVerification!: pulumi.Output<boolean | undefined>;
    public readonly url!: pulumi.Output<string>;
    public /*out*/ readonly uuid!: pulumi.Output<string>;
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
            resourceInputs["skipCertVerification"] = args ? args.skipCertVerification : undefined;
            resourceInputs["url"] = args ? args.url : undefined;
            resourceInputs["workspace"] = args ? args.workspace : undefined;
            resourceInputs["uuid"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(WorkspaceHook.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering WorkspaceHook resources.
 */
export interface WorkspaceHookState {
    active?: pulumi.Input<boolean>;
    description?: pulumi.Input<string>;
    events?: pulumi.Input<pulumi.Input<string>[]>;
    skipCertVerification?: pulumi.Input<boolean>;
    url?: pulumi.Input<string>;
    uuid?: pulumi.Input<string>;
    workspace?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a WorkspaceHook resource.
 */
export interface WorkspaceHookArgs {
    active?: pulumi.Input<boolean>;
    description: pulumi.Input<string>;
    events: pulumi.Input<pulumi.Input<string>[]>;
    skipCertVerification?: pulumi.Input<boolean>;
    url: pulumi.Input<string>;
    workspace: pulumi.Input<string>;
}
