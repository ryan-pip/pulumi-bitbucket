// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class GroupMembership extends pulumi.CustomResource {
    /**
     * Get an existing GroupMembership resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GroupMembershipState, opts?: pulumi.CustomResourceOptions): GroupMembership {
        return new GroupMembership(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'bitbucket:index/groupMembership:GroupMembership';

    /**
     * Returns true if the given object is an instance of GroupMembership.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is GroupMembership {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === GroupMembership.__pulumiType;
    }

    public readonly groupSlug!: pulumi.Output<string>;
    public /*out*/ readonly slug!: pulumi.Output<string>;
    public readonly uuid!: pulumi.Output<string>;
    public readonly workspace!: pulumi.Output<string>;

    /**
     * Create a GroupMembership resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: GroupMembershipArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: GroupMembershipArgs | GroupMembershipState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as GroupMembershipState | undefined;
            resourceInputs["groupSlug"] = state ? state.groupSlug : undefined;
            resourceInputs["slug"] = state ? state.slug : undefined;
            resourceInputs["uuid"] = state ? state.uuid : undefined;
            resourceInputs["workspace"] = state ? state.workspace : undefined;
        } else {
            const args = argsOrState as GroupMembershipArgs | undefined;
            if ((!args || args.groupSlug === undefined) && !opts.urn) {
                throw new Error("Missing required property 'groupSlug'");
            }
            if ((!args || args.uuid === undefined) && !opts.urn) {
                throw new Error("Missing required property 'uuid'");
            }
            if ((!args || args.workspace === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workspace'");
            }
            resourceInputs["groupSlug"] = args ? args.groupSlug : undefined;
            resourceInputs["uuid"] = args ? args.uuid : undefined;
            resourceInputs["workspace"] = args ? args.workspace : undefined;
            resourceInputs["slug"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(GroupMembership.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering GroupMembership resources.
 */
export interface GroupMembershipState {
    groupSlug?: pulumi.Input<string>;
    slug?: pulumi.Input<string>;
    uuid?: pulumi.Input<string>;
    workspace?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a GroupMembership resource.
 */
export interface GroupMembershipArgs {
    groupSlug: pulumi.Input<string>;
    uuid: pulumi.Input<string>;
    workspace: pulumi.Input<string>;
}
