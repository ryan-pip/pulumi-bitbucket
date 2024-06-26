// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a way to fetch data on a pipeline OIDC Config Keys.
 *
 * OAuth2 Scopes: `none`
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as bitbucket from "@pulumi/bitbucket";
 *
 * const example = bitbucket.getPipelineOidcConfigKeys({
 *     workspace: "example",
 * });
 * ```
 */
export function getPipelineOidcConfigKeys(args: GetPipelineOidcConfigKeysArgs, opts?: pulumi.InvokeOptions): Promise<GetPipelineOidcConfigKeysResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("bitbucket:index/getPipelineOidcConfigKeys:getPipelineOidcConfigKeys", {
        "workspace": args.workspace,
    }, opts);
}

/**
 * A collection of arguments for invoking getPipelineOidcConfigKeys.
 */
export interface GetPipelineOidcConfigKeysArgs {
    /**
     * The workspace to fetch pipeline oidc config keys.
     */
    workspace: string;
}

/**
 * A collection of values returned by getPipelineOidcConfigKeys.
 */
export interface GetPipelineOidcConfigKeysResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly keys: string;
    readonly workspace: string;
}
/**
 * Provides a way to fetch data on a pipeline OIDC Config Keys.
 *
 * OAuth2 Scopes: `none`
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as bitbucket from "@pulumi/bitbucket";
 *
 * const example = bitbucket.getPipelineOidcConfigKeys({
 *     workspace: "example",
 * });
 * ```
 */
export function getPipelineOidcConfigKeysOutput(args: GetPipelineOidcConfigKeysOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPipelineOidcConfigKeysResult> {
    return pulumi.output(args).apply((a: any) => getPipelineOidcConfigKeys(a, opts))
}

/**
 * A collection of arguments for invoking getPipelineOidcConfigKeys.
 */
export interface GetPipelineOidcConfigKeysOutputArgs {
    /**
     * The workspace to fetch pipeline oidc config keys.
     */
    workspace: pulumi.Input<string>;
}
