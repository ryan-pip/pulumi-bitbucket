// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides support for setting up default reviewers for your project. You must however have the UUID of the user available. Since Bitbucket has removed usernames from its APIs the best case is to use the UUID via the data provider.
 *
 * OAuth2 Scopes: `project:admin`
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as bitbucket from "@pulumi/bitbucket";
 * import * as bitbucket from "@ryan-pip/pulumi_bitbucket";
 *
 * const reviewer = bitbucket.getUser({
 *     uuid: "{account UUID}",
 * });
 * const infrastructure = new bitbucket.ProjectDefaultReviewers("infrastructure", {
 *     workspace: "myteam",
 *     project: "TERRAFORM",
 *     reviewers: [reviewer.then(reviewer => reviewer.uuid)],
 * });
 * ```
 *
 * ## Import
 *
 * Project Default Reviewers can be imported using the workspace and project separated by a (`/`) and the end, e.g.,
 *
 * ```sh
 *  $ pulumi import bitbucket:index/projectDefaultReviewers:ProjectDefaultReviewers example myteam/terraform-code
 * ```
 */
export class ProjectDefaultReviewers extends pulumi.CustomResource {
    /**
     * Get an existing ProjectDefaultReviewers resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectDefaultReviewersState, opts?: pulumi.CustomResourceOptions): ProjectDefaultReviewers {
        return new ProjectDefaultReviewers(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'bitbucket:index/projectDefaultReviewers:ProjectDefaultReviewers';

    /**
     * Returns true if the given object is an instance of ProjectDefaultReviewers.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ProjectDefaultReviewers {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ProjectDefaultReviewers.__pulumiType;
    }

    /**
     * The key of the project.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * A list of reviewers to use.
     */
    public readonly reviewers!: pulumi.Output<string[]>;
    /**
     * The workspace of this project. Can be you or any team you
     * have write access to.
     */
    public readonly workspace!: pulumi.Output<string>;

    /**
     * Create a ProjectDefaultReviewers resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProjectDefaultReviewersArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProjectDefaultReviewersArgs | ProjectDefaultReviewersState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ProjectDefaultReviewersState | undefined;
            resourceInputs["project"] = state ? state.project : undefined;
            resourceInputs["reviewers"] = state ? state.reviewers : undefined;
            resourceInputs["workspace"] = state ? state.workspace : undefined;
        } else {
            const args = argsOrState as ProjectDefaultReviewersArgs | undefined;
            if ((!args || args.project === undefined) && !opts.urn) {
                throw new Error("Missing required property 'project'");
            }
            if ((!args || args.reviewers === undefined) && !opts.urn) {
                throw new Error("Missing required property 'reviewers'");
            }
            if ((!args || args.workspace === undefined) && !opts.urn) {
                throw new Error("Missing required property 'workspace'");
            }
            resourceInputs["project"] = args ? args.project : undefined;
            resourceInputs["reviewers"] = args ? args.reviewers : undefined;
            resourceInputs["workspace"] = args ? args.workspace : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ProjectDefaultReviewers.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ProjectDefaultReviewers resources.
 */
export interface ProjectDefaultReviewersState {
    /**
     * The key of the project.
     */
    project?: pulumi.Input<string>;
    /**
     * A list of reviewers to use.
     */
    reviewers?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The workspace of this project. Can be you or any team you
     * have write access to.
     */
    workspace?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ProjectDefaultReviewers resource.
 */
export interface ProjectDefaultReviewersArgs {
    /**
     * The key of the project.
     */
    project: pulumi.Input<string>;
    /**
     * A list of reviewers to use.
     */
    reviewers: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The workspace of this project. Can be you or any team you
     * have write access to.
     */
    workspace: pulumi.Input<string>;
}
