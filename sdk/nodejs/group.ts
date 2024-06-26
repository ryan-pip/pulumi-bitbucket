// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Bitbucket group resource.
 *
 * This allows you to manage your groups.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as bitbucket from "@pulumi/bitbucket";
 * import * as bitbucket from "@ryan-pip/pulumi_bitbucket";
 *
 * const testWorkspace = bitbucket.getWorkspace({
 *     workspace: "example",
 * });
 * const testGroup = new bitbucket.Group("testGroup", {
 *     workspace: testWorkspace.then(testWorkspace => testWorkspace.id),
 *     autoAdd: true,
 *     permission: "read",
 * });
 * ```
 *
 * ## Import
 *
 * Groups can be imported using their `workspace/group-slug` ID, e.g.
 *
 * ```sh
 *  $ pulumi import bitbucket:index/group:Group group my-workspace/group-slug
 * ```
 */
export class Group extends pulumi.CustomResource {
    /**
     * Get an existing Group resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupState, opts?: pulumi.CustomResourceOptions): Group {
        return new Group(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'bitbucket:index/group:Group';

    /**
     * Returns true if the given object is an instance of Group.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Group {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Group.__pulumiType;
    }

    /**
     * Whether to automatically add users the group
     */
    public readonly autoAdd!: pulumi.Output<boolean | undefined>;
    /**
     * Whether to disable email forwarding for group.
     */
    public readonly emailForwardingDisabled!: pulumi.Output<boolean | undefined>;
    /**
     * The name of the group.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * One of `read`, `write`, and `admin`.
     */
    public readonly permission!: pulumi.Output<string | undefined>;
    /**
     * The groups slug.
     */
    public /*out*/ readonly slug!: pulumi.Output<string>;
    /**
     * The workspace of this repository.
     */
    public readonly workspace!: pulumi.Output<string>;

    /**
     * Create a Group resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupArgs | GroupState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GroupState | undefined;
            resourceInputs["autoAdd"] = state ? state.autoAdd : undefined;
            resourceInputs["emailForwardingDisabled"] = state ? state.emailForwardingDisabled : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["permission"] = state ? state.permission : undefined;
            resourceInputs["slug"] = state ? state.slug : undefined;
            resourceInputs["workspace"] = state ? state.workspace : undefined;
        } else {
            const args = argsOrState as GroupArgs | undefined;
            if ((!args || args.workspace === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workspace'");
            }
            resourceInputs["autoAdd"] = args ? args.autoAdd : undefined;
            resourceInputs["emailForwardingDisabled"] = args ? args.emailForwardingDisabled : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["permission"] = args ? args.permission : undefined;
            resourceInputs["workspace"] = args ? args.workspace : undefined;
            resourceInputs["slug"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Group.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Group resources.
 */
export interface GroupState {
    /**
     * Whether to automatically add users the group
     */
    autoAdd?: pulumi.Input<boolean>;
    /**
     * Whether to disable email forwarding for group.
     */
    emailForwardingDisabled?: pulumi.Input<boolean>;
    /**
     * The name of the group.
     */
    name?: pulumi.Input<string>;
    /**
     * One of `read`, `write`, and `admin`.
     */
    permission?: pulumi.Input<string>;
    /**
     * The groups slug.
     */
    slug?: pulumi.Input<string>;
    /**
     * The workspace of this repository.
     */
    workspace?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Group resource.
 */
export interface GroupArgs {
    /**
     * Whether to automatically add users the group
     */
    autoAdd?: pulumi.Input<boolean>;
    /**
     * Whether to disable email forwarding for group.
     */
    emailForwardingDisabled?: pulumi.Input<boolean>;
    /**
     * The name of the group.
     */
    name?: pulumi.Input<string>;
    /**
     * One of `read`, `write`, and `admin`.
     */
    permission?: pulumi.Input<string>;
    /**
     * The workspace of this repository.
     */
    workspace: pulumi.Input<string>;
}
