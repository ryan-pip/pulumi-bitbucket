// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a way to fetch data of the current user.
 *
 * OAuth2 Scopes: `account`
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as bitbucket from "@pulumi/bitbucket";
 *
 * const example = bitbucket.getCurrentUser({});
 * ```
 */
export function getCurrentUser(opts?: pulumi.InvokeOptions): Promise<GetCurrentUserResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("bitbucket:index/getCurrentUser:getCurrentUser", {
    }, opts);
}

/**
 * A collection of values returned by getCurrentUser.
 */
export interface GetCurrentUserResult {
    /**
     * the display name that the user wants to use for GDPR
     */
    readonly displayName: string;
    /**
     * The email address.
     */
    readonly emails: outputs.GetCurrentUserEmail[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The Username.
     */
    readonly username: string;
    /**
     * the uuid that bitbucket users to connect a user to various objects
     */
    readonly uuid: string;
}
/**
 * Provides a way to fetch data of the current user.
 *
 * OAuth2 Scopes: `account`
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as bitbucket from "@pulumi/bitbucket";
 *
 * const example = bitbucket.getCurrentUser({});
 * ```
 */
export function getCurrentUserOutput(opts?: pulumi.InvokeOptions): pulumi.Output<GetCurrentUserResult> {
    return pulumi.output(getCurrentUser(opts))
}
