// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class RepositoryUserPermission extends pulumi.CustomResource {
    /**
     * Get an existing RepositoryUserPermission resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RepositoryUserPermissionState, opts?: pulumi.CustomResourceOptions): RepositoryUserPermission {
        return new RepositoryUserPermission(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'bitbucket:index/repositoryUserPermission:RepositoryUserPermission';

    /**
     * Returns true if the given object is an instance of RepositoryUserPermission.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RepositoryUserPermission {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RepositoryUserPermission.__pulumiType;
    }

    public readonly permission!: pulumi.Output<string>;
    public readonly repoSlug!: pulumi.Output<string>;
    public readonly userId!: pulumi.Output<string>;
    public readonly workspace!: pulumi.Output<string>;

    /**
     * Create a RepositoryUserPermission resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RepositoryUserPermissionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RepositoryUserPermissionArgs | RepositoryUserPermissionState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as RepositoryUserPermissionState | undefined;
            resourceInputs["permission"] = state ? state.permission : undefined;
            resourceInputs["repoSlug"] = state ? state.repoSlug : undefined;
            resourceInputs["userId"] = state ? state.userId : undefined;
            resourceInputs["workspace"] = state ? state.workspace : undefined;
        } else {
            const args = argsOrState as RepositoryUserPermissionArgs | undefined;
            if ((!args || args.permission === undefined) && !opts.urn) {
                throw new Error("Missing required property 'permission'");
            }
            if ((!args || args.repoSlug === undefined) && !opts.urn) {
                throw new Error("Missing required property 'repoSlug'");
            }
            if ((!args || args.userId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'userId'");
            }
            if ((!args || args.workspace === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workspace'");
            }
            resourceInputs["permission"] = args ? args.permission : undefined;
            resourceInputs["repoSlug"] = args ? args.repoSlug : undefined;
            resourceInputs["userId"] = args ? args.userId : undefined;
            resourceInputs["workspace"] = args ? args.workspace : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(RepositoryUserPermission.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RepositoryUserPermission resources.
 */
export interface RepositoryUserPermissionState {
    permission?: pulumi.Input<string>;
    repoSlug?: pulumi.Input<string>;
    userId?: pulumi.Input<string>;
    workspace?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RepositoryUserPermission resource.
 */
export interface RepositoryUserPermissionArgs {
    permission: pulumi.Input<string>;
    repoSlug: pulumi.Input<string>;
    userId: pulumi.Input<string>;
    workspace: pulumi.Input<string>;
}
