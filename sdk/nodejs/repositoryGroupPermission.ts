// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class RepositoryGroupPermission extends pulumi.CustomResource {
    /**
     * Get an existing RepositoryGroupPermission resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RepositoryGroupPermissionState, opts?: pulumi.CustomResourceOptions): RepositoryGroupPermission {
        return new RepositoryGroupPermission(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'bitbucket:index/repositoryGroupPermission:RepositoryGroupPermission';

    /**
     * Returns true if the given object is an instance of RepositoryGroupPermission.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RepositoryGroupPermission {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RepositoryGroupPermission.__pulumiType;
    }

    public readonly groupSlug!: pulumi.Output<string>;
    public readonly permission!: pulumi.Output<string>;
    public readonly repoSlug!: pulumi.Output<string>;
    public readonly workspace!: pulumi.Output<string>;

    /**
     * Create a RepositoryGroupPermission resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RepositoryGroupPermissionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RepositoryGroupPermissionArgs | RepositoryGroupPermissionState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as RepositoryGroupPermissionState | undefined;
            resourceInputs["groupSlug"] = state ? state.groupSlug : undefined;
            resourceInputs["permission"] = state ? state.permission : undefined;
            resourceInputs["repoSlug"] = state ? state.repoSlug : undefined;
            resourceInputs["workspace"] = state ? state.workspace : undefined;
        } else {
            const args = argsOrState as RepositoryGroupPermissionArgs | undefined;
            if ((!args || args.groupSlug === undefined) && !opts.urn) {
                throw new Error("Missing required property 'groupSlug'");
            }
            if ((!args || args.permission === undefined) && !opts.urn) {
                throw new Error("Missing required property 'permission'");
            }
            if ((!args || args.repoSlug === undefined) && !opts.urn) {
                throw new Error("Missing required property 'repoSlug'");
            }
            if ((!args || args.workspace === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workspace'");
            }
            resourceInputs["groupSlug"] = args ? args.groupSlug : undefined;
            resourceInputs["permission"] = args ? args.permission : undefined;
            resourceInputs["repoSlug"] = args ? args.repoSlug : undefined;
            resourceInputs["workspace"] = args ? args.workspace : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(RepositoryGroupPermission.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RepositoryGroupPermission resources.
 */
export interface RepositoryGroupPermissionState {
    groupSlug?: pulumi.Input<string>;
    permission?: pulumi.Input<string>;
    repoSlug?: pulumi.Input<string>;
    workspace?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RepositoryGroupPermission resource.
 */
export interface RepositoryGroupPermissionArgs {
    groupSlug: pulumi.Input<string>;
    permission: pulumi.Input<string>;
    repoSlug: pulumi.Input<string>;
    workspace: pulumi.Input<string>;
}
