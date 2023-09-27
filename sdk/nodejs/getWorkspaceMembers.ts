// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function getWorkspaceMembers(args: GetWorkspaceMembersArgs, opts?: pulumi.InvokeOptions): Promise<GetWorkspaceMembersResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("bitbucket:index/getWorkspaceMembers:getWorkspaceMembers", {
        "workspace": args.workspace,
    }, opts);
}

/**
 * A collection of arguments for invoking getWorkspaceMembers.
 */
export interface GetWorkspaceMembersArgs {
    workspace: string;
}

/**
 * A collection of values returned by getWorkspaceMembers.
 */
export interface GetWorkspaceMembersResult {
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly members: string[];
    readonly workspace: string;
}
export function getWorkspaceMembersOutput(args: GetWorkspaceMembersOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetWorkspaceMembersResult> {
    return pulumi.output(args).apply((a: any) => getWorkspaceMembers(a, opts))
}

/**
 * A collection of arguments for invoking getWorkspaceMembers.
 */
export interface GetWorkspaceMembersOutputArgs {
    workspace: pulumi.Input<string>;
}
