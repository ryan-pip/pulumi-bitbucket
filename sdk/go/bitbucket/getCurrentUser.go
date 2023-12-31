// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package bitbucket

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/ryan-pip/pulumi-bitbucket/sdk/go/bitbucket/internal"
)

func GetCurrentUser(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*GetCurrentUserResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetCurrentUserResult
	err := ctx.Invoke("bitbucket:index/getCurrentUser:getCurrentUser", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getCurrentUser.
type GetCurrentUserResult struct {
	DisplayName string                `pulumi:"displayName"`
	Emails      []GetCurrentUserEmail `pulumi:"emails"`
	// The provider-assigned unique ID for this managed resource.
	Id       string `pulumi:"id"`
	Username string `pulumi:"username"`
	Uuid     string `pulumi:"uuid"`
}
