// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package bitbucket

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/ryan-pip/pulumi-bitbucket/sdk/go/bitbucket/internal"
)

// Provides a way to fetch data of group members.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/ryan-pip/pulumi-bitbucket/sdk/go/bitbucket"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := bitbucket.GetGroupMembers(ctx, &bitbucket.GetGroupMembersArgs{
//				Slug:      "example",
//				Workspace: "example",
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func GetGroupMembers(ctx *pulumi.Context, args *GetGroupMembersArgs, opts ...pulumi.InvokeOption) (*GetGroupMembersResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetGroupMembersResult
	err := ctx.Invoke("bitbucket:index/getGroupMembers:getGroupMembers", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGroupMembers.
type GetGroupMembersArgs struct {
	// The group's slug.
	Slug string `pulumi:"slug"`
	// The UUID that bitbucket groups to connect a group to various objects
	Workspace string `pulumi:"workspace"`
}

// A collection of values returned by getGroupMembers.
type GetGroupMembersResult struct {
	// A set of group member objects. See Group Member below.
	GroupMembers []GetGroupMembersGroupMember `pulumi:"groupMembers"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// A list of group member uuid.
	//
	// Deprecated: use group_members instead
	Members   []string `pulumi:"members"`
	Slug      string   `pulumi:"slug"`
	Workspace string   `pulumi:"workspace"`
}

func GetGroupMembersOutput(ctx *pulumi.Context, args GetGroupMembersOutputArgs, opts ...pulumi.InvokeOption) GetGroupMembersResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetGroupMembersResult, error) {
			args := v.(GetGroupMembersArgs)
			r, err := GetGroupMembers(ctx, &args, opts...)
			var s GetGroupMembersResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetGroupMembersResultOutput)
}

// A collection of arguments for invoking getGroupMembers.
type GetGroupMembersOutputArgs struct {
	// The group's slug.
	Slug pulumi.StringInput `pulumi:"slug"`
	// The UUID that bitbucket groups to connect a group to various objects
	Workspace pulumi.StringInput `pulumi:"workspace"`
}

func (GetGroupMembersOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetGroupMembersArgs)(nil)).Elem()
}

// A collection of values returned by getGroupMembers.
type GetGroupMembersResultOutput struct{ *pulumi.OutputState }

func (GetGroupMembersResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetGroupMembersResult)(nil)).Elem()
}

func (o GetGroupMembersResultOutput) ToGetGroupMembersResultOutput() GetGroupMembersResultOutput {
	return o
}

func (o GetGroupMembersResultOutput) ToGetGroupMembersResultOutputWithContext(ctx context.Context) GetGroupMembersResultOutput {
	return o
}

// A set of group member objects. See Group Member below.
func (o GetGroupMembersResultOutput) GroupMembers() GetGroupMembersGroupMemberArrayOutput {
	return o.ApplyT(func(v GetGroupMembersResult) []GetGroupMembersGroupMember { return v.GroupMembers }).(GetGroupMembersGroupMemberArrayOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetGroupMembersResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetGroupMembersResult) string { return v.Id }).(pulumi.StringOutput)
}

// A list of group member uuid.
//
// Deprecated: use group_members instead
func (o GetGroupMembersResultOutput) Members() pulumi.StringArrayOutput {
	return o.ApplyT(func(v GetGroupMembersResult) []string { return v.Members }).(pulumi.StringArrayOutput)
}

func (o GetGroupMembersResultOutput) Slug() pulumi.StringOutput {
	return o.ApplyT(func(v GetGroupMembersResult) string { return v.Slug }).(pulumi.StringOutput)
}

func (o GetGroupMembersResultOutput) Workspace() pulumi.StringOutput {
	return o.ApplyT(func(v GetGroupMembersResult) string { return v.Workspace }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetGroupMembersResultOutput{})
}
