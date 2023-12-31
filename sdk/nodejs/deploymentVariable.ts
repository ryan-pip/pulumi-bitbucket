// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class DeploymentVariable extends pulumi.CustomResource {
    /**
     * Get an existing DeploymentVariable resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DeploymentVariableState, opts?: pulumi.CustomResourceOptions): DeploymentVariable {
        return new DeploymentVariable(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'bitbucket:index/deploymentVariable:DeploymentVariable';

    /**
     * Returns true if the given object is an instance of DeploymentVariable.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DeploymentVariable {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DeploymentVariable.__pulumiType;
    }

    public readonly deployment!: pulumi.Output<string>;
    public readonly key!: pulumi.Output<string>;
    public readonly secured!: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly uuid!: pulumi.Output<string>;
    public readonly value!: pulumi.Output<string>;

    /**
     * Create a DeploymentVariable resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DeploymentVariableArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DeploymentVariableArgs | DeploymentVariableState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DeploymentVariableState | undefined;
            resourceInputs["deployment"] = state ? state.deployment : undefined;
            resourceInputs["key"] = state ? state.key : undefined;
            resourceInputs["secured"] = state ? state.secured : undefined;
            resourceInputs["uuid"] = state ? state.uuid : undefined;
            resourceInputs["value"] = state ? state.value : undefined;
        } else {
            const args = argsOrState as DeploymentVariableArgs | undefined;
            if ((!args || args.deployment === undefined) && !opts.urn) {
                throw new Error("Missing required property 'deployment'");
            }
            if ((!args || args.key === undefined) && !opts.urn) {
                throw new Error("Missing required property 'key'");
            }
            if ((!args || args.value === undefined) && !opts.urn) {
                throw new Error("Missing required property 'value'");
            }
            resourceInputs["deployment"] = args ? args.deployment : undefined;
            resourceInputs["key"] = args ? args.key : undefined;
            resourceInputs["secured"] = args ? args.secured : undefined;
            resourceInputs["value"] = args?.value ? pulumi.secret(args.value) : undefined;
            resourceInputs["uuid"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["value"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(DeploymentVariable.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering DeploymentVariable resources.
 */
export interface DeploymentVariableState {
    deployment?: pulumi.Input<string>;
    key?: pulumi.Input<string>;
    secured?: pulumi.Input<boolean>;
    uuid?: pulumi.Input<string>;
    value?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a DeploymentVariable resource.
 */
export interface DeploymentVariableArgs {
    deployment: pulumi.Input<string>;
    key: pulumi.Input<string>;
    secured?: pulumi.Input<boolean>;
    value: pulumi.Input<string>;
}
