// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * This resource allows you to manage your projects in your bitbucket team.
 *
 * OAuth2 Scopes: `project` and `project:admin`
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as bitbucket from "@ryan-pip/pulumi_bitbucket";
 *
 * const devops = new bitbucket.Project("devops", {
 *     key: "DEVOPS",
 *     owner: "my-team",
 * });
 * ```
 *
 * ## Import
 *
 * Repositories can be imported using their `owner/key` ID, e.g.
 *
 * ```sh
 *  $ pulumi import bitbucket:index/project:Project my_project my-account/project_key
 * ```
 */
export class Project extends pulumi.CustomResource {
    /**
     * Get an existing Project resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectState, opts?: pulumi.CustomResourceOptions): Project {
        return new Project(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'bitbucket:index/project:Project';

    /**
     * Returns true if the given object is an instance of Project.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Project {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Project.__pulumiType;
    }

    /**
     * The description of the project
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Indicates whether the project contains publicly visible repositories. Note that private projects cannot contain public repositories.
     */
    public /*out*/ readonly hasPubliclyVisibleRepos!: pulumi.Output<boolean>;
    /**
     * If you want to keep the project private - defaults to `true`
     */
    public readonly isPrivate!: pulumi.Output<boolean | undefined>;
    /**
     * The key used for this project
     */
    public readonly key!: pulumi.Output<string>;
    /**
     * A set of links to a resource related to this object. See Link Below.
     */
    public readonly link!: pulumi.Output<outputs.ProjectLink>;
    /**
     * The name of the project
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The owner of this project. Can be you or any team you have write access to.
     */
    public readonly owner!: pulumi.Output<string>;
    /**
     * The project's immutable id.
     */
    public /*out*/ readonly uuid!: pulumi.Output<string>;

    /**
     * Create a Project resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProjectArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProjectArgs | ProjectState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ProjectState | undefined;
            resourceInputs["description"] = state ? state.description : undefined;
            resourceInputs["hasPubliclyVisibleRepos"] = state ? state.hasPubliclyVisibleRepos : undefined;
            resourceInputs["isPrivate"] = state ? state.isPrivate : undefined;
            resourceInputs["key"] = state ? state.key : undefined;
            resourceInputs["link"] = state ? state.link : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["owner"] = state ? state.owner : undefined;
            resourceInputs["uuid"] = state ? state.uuid : undefined;
        } else {
            const args = argsOrState as ProjectArgs | undefined;
            if ((!args || args.key === undefined) && !opts.urn) {
                throw new Error("Missing required property 'key'");
            }
            if ((!args || args.owner === undefined) && !opts.urn) {
                throw new Error("Missing required property 'owner'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["isPrivate"] = args ? args.isPrivate : undefined;
            resourceInputs["key"] = args ? args.key : undefined;
            resourceInputs["link"] = args ? args.link : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["owner"] = args ? args.owner : undefined;
            resourceInputs["hasPubliclyVisibleRepos"] = undefined /*out*/;
            resourceInputs["uuid"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Project.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Project resources.
 */
export interface ProjectState {
    /**
     * The description of the project
     */
    description?: pulumi.Input<string>;
    /**
     * Indicates whether the project contains publicly visible repositories. Note that private projects cannot contain public repositories.
     */
    hasPubliclyVisibleRepos?: pulumi.Input<boolean>;
    /**
     * If you want to keep the project private - defaults to `true`
     */
    isPrivate?: pulumi.Input<boolean>;
    /**
     * The key used for this project
     */
    key?: pulumi.Input<string>;
    /**
     * A set of links to a resource related to this object. See Link Below.
     */
    link?: pulumi.Input<inputs.ProjectLink>;
    /**
     * The name of the project
     */
    name?: pulumi.Input<string>;
    /**
     * The owner of this project. Can be you or any team you have write access to.
     */
    owner?: pulumi.Input<string>;
    /**
     * The project's immutable id.
     */
    uuid?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Project resource.
 */
export interface ProjectArgs {
    /**
     * The description of the project
     */
    description?: pulumi.Input<string>;
    /**
     * If you want to keep the project private - defaults to `true`
     */
    isPrivate?: pulumi.Input<boolean>;
    /**
     * The key used for this project
     */
    key: pulumi.Input<string>;
    /**
     * A set of links to a resource related to this object. See Link Below.
     */
    link?: pulumi.Input<inputs.ProjectLink>;
    /**
     * The name of the project
     */
    name?: pulumi.Input<string>;
    /**
     * The owner of this project. Can be you or any team you have write access to.
     */
    owner: pulumi.Input<string>;
}
