// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package bitbucket

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"github.com/ryan-pip/pulumi-bitbucket/sdk/go/bitbucket/internal"
)

func GetUser(ctx *pulumi.Context, args *GetUserArgs, opts ...pulumi.InvokeOption) (*GetUserResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetUserResult
	err := ctx.Invoke("bitbucket:index/getUser:getUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getUser.
type GetUserArgs struct {
	DisplayName *string `pulumi:"displayName"`
	Uuid        *string `pulumi:"uuid"`
}

// A collection of values returned by getUser.
type GetUserResult struct {
	DisplayName *string `pulumi:"displayName"`
	// The provider-assigned unique ID for this managed resource.
	Id       string  `pulumi:"id"`
	Username string  `pulumi:"username"`
	Uuid     *string `pulumi:"uuid"`
}

func GetUserOutput(ctx *pulumi.Context, args GetUserOutputArgs, opts ...pulumi.InvokeOption) GetUserResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetUserResult, error) {
			args := v.(GetUserArgs)
			r, err := GetUser(ctx, &args, opts...)
			var s GetUserResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetUserResultOutput)
}

// A collection of arguments for invoking getUser.
type GetUserOutputArgs struct {
	DisplayName pulumi.StringPtrInput `pulumi:"displayName"`
	Uuid        pulumi.StringPtrInput `pulumi:"uuid"`
}

func (GetUserOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUserArgs)(nil)).Elem()
}

// A collection of values returned by getUser.
type GetUserResultOutput struct{ *pulumi.OutputState }

func (GetUserResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetUserResult)(nil)).Elem()
}

func (o GetUserResultOutput) ToGetUserResultOutput() GetUserResultOutput {
	return o
}

func (o GetUserResultOutput) ToGetUserResultOutputWithContext(ctx context.Context) GetUserResultOutput {
	return o
}

func (o GetUserResultOutput) ToOutput(ctx context.Context) pulumix.Output[GetUserResult] {
	return pulumix.Output[GetUserResult]{
		OutputState: o.OutputState,
	}
}

func (o GetUserResultOutput) DisplayName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetUserResult) *string { return v.DisplayName }).(pulumi.StringPtrOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetUserResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetUserResultOutput) Username() pulumi.StringOutput {
	return o.ApplyT(func(v GetUserResult) string { return v.Username }).(pulumi.StringOutput)
}

func (o GetUserResultOutput) Uuid() pulumi.StringPtrOutput {
	return o.ApplyT(func(v GetUserResult) *string { return v.Uuid }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(GetUserResultOutput{})
}
