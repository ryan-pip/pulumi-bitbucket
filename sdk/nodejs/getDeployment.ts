// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a way to fetch data on a Deployment.
 *
 * OAuth2 Scopes: `none`
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as bitbucket from "@pulumi/bitbucket";
 *
 * const example = bitbucket.getDeployment({
 *     repository: "example",
 *     uuid: "example",
 *     workspace: "example",
 * });
 * ```
 */
export function getDeployment(args: GetDeploymentArgs, opts?: pulumi.InvokeOptions): Promise<GetDeploymentResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("bitbucket:index/getDeployment:getDeployment", {
        "repository": args.repository,
        "uuid": args.uuid,
        "workspace": args.workspace,
    }, opts);
}

/**
 * A collection of arguments for invoking getDeployment.
 */
export interface GetDeploymentArgs {
    /**
     * The repository name.
     */
    repository: string;
    /**
     * The environment UUID.
     */
    uuid: string;
    /**
     * The workspace name.
     */
    workspace: string;
}

/**
 * A collection of values returned by getDeployment.
 */
export interface GetDeploymentResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The name of the environment.
     */
    readonly name: string;
    readonly repository: string;
    /**
     * The stage (Test, Staging, Production).
     */
    readonly stage: string;
    readonly uuid: string;
    readonly workspace: string;
}
/**
 * Provides a way to fetch data on a Deployment.
 *
 * OAuth2 Scopes: `none`
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as bitbucket from "@pulumi/bitbucket";
 *
 * const example = bitbucket.getDeployment({
 *     repository: "example",
 *     uuid: "example",
 *     workspace: "example",
 * });
 * ```
 */
export function getDeploymentOutput(args: GetDeploymentOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDeploymentResult> {
    return pulumi.output(args).apply((a: any) => getDeployment(a, opts))
}

/**
 * A collection of arguments for invoking getDeployment.
 */
export interface GetDeploymentOutputArgs {
    /**
     * The repository name.
     */
    repository: pulumi.Input<string>;
    /**
     * The environment UUID.
     */
    uuid: pulumi.Input<string>;
    /**
     * The workspace name.
     */
    workspace: pulumi.Input<string>;
}
