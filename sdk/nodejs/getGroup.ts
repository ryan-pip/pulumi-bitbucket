// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a way to fetch data of a group.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as bitbucket from "@pulumi/bitbucket";
 *
 * const example = bitbucket.getGroup({
 *     slug: "example",
 *     workspace: "example",
 * });
 * ```
 */
export function getGroup(args: GetGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("bitbucket:index/getGroup:getGroup", {
        "slug": args.slug,
        "workspace": args.workspace,
    }, opts);
}

/**
 * A collection of arguments for invoking getGroup.
 */
export interface GetGroupArgs {
    /**
     * The group's slug.
     */
    slug: string;
    /**
     * The UUID that bitbucket groups to connect a group to various objects
     */
    workspace: string;
}

/**
 * A collection of values returned by getGroup.
 */
export interface GetGroupResult {
    /**
     * Whether to automatically add users the group
     */
    readonly autoAdd: boolean;
    /**
     * Whether to disable email forwarding for group.
     */
    readonly emailForwardingDisabled: boolean;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The name of the group.
     */
    readonly name: string;
    /**
     * One of `read`, `write`, and `admin`.
     */
    readonly permission: string;
    readonly slug: string;
    readonly workspace: string;
}
/**
 * Provides a way to fetch data of a group.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as bitbucket from "@pulumi/bitbucket";
 *
 * const example = bitbucket.getGroup({
 *     slug: "example",
 *     workspace: "example",
 * });
 * ```
 */
export function getGroupOutput(args: GetGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetGroupResult> {
    return pulumi.output(args).apply((a: any) => getGroup(a, opts))
}

/**
 * A collection of arguments for invoking getGroup.
 */
export interface GetGroupOutputArgs {
    /**
     * The group's slug.
     */
    slug: pulumi.Input<string>;
    /**
     * The UUID that bitbucket groups to connect a group to various objects
     */
    workspace: pulumi.Input<string>;
}
