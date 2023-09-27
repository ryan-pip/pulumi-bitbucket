// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package bitbucket

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"github.com/ryan-pip/pulumi-bitbucket/sdk/go/bitbucket/internal"
)

type GroupMembership struct {
	pulumi.CustomResourceState

	GroupSlug pulumi.StringOutput `pulumi:"groupSlug"`
	Slug      pulumi.StringOutput `pulumi:"slug"`
	Uuid      pulumi.StringOutput `pulumi:"uuid"`
	Workspace pulumi.StringOutput `pulumi:"workspace"`
}

// NewGroupMembership registers a new resource with the given unique name, arguments, and options.
func NewGroupMembership(ctx *pulumi.Context,
	name string, args *GroupMembershipArgs, opts ...pulumi.ResourceOption) (*GroupMembership, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.GroupSlug == nil {
		return nil, errors.New("invalid value for required argument 'GroupSlug'")
	}
	if args.Uuid == nil {
		return nil, errors.New("invalid value for required argument 'Uuid'")
	}
	if args.Workspace == nil {
		return nil, errors.New("invalid value for required argument 'Workspace'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource GroupMembership
	err := ctx.RegisterResource("bitbucket:index/groupMembership:GroupMembership", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGroupMembership gets an existing GroupMembership resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGroupMembership(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GroupMembershipState, opts ...pulumi.ResourceOption) (*GroupMembership, error) {
	var resource GroupMembership
	err := ctx.ReadResource("bitbucket:index/groupMembership:GroupMembership", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GroupMembership resources.
type groupMembershipState struct {
	GroupSlug *string `pulumi:"groupSlug"`
	Slug      *string `pulumi:"slug"`
	Uuid      *string `pulumi:"uuid"`
	Workspace *string `pulumi:"workspace"`
}

type GroupMembershipState struct {
	GroupSlug pulumi.StringPtrInput
	Slug      pulumi.StringPtrInput
	Uuid      pulumi.StringPtrInput
	Workspace pulumi.StringPtrInput
}

func (GroupMembershipState) ElementType() reflect.Type {
	return reflect.TypeOf((*groupMembershipState)(nil)).Elem()
}

type groupMembershipArgs struct {
	GroupSlug string `pulumi:"groupSlug"`
	Uuid      string `pulumi:"uuid"`
	Workspace string `pulumi:"workspace"`
}

// The set of arguments for constructing a GroupMembership resource.
type GroupMembershipArgs struct {
	GroupSlug pulumi.StringInput
	Uuid      pulumi.StringInput
	Workspace pulumi.StringInput
}

func (GroupMembershipArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*groupMembershipArgs)(nil)).Elem()
}

type GroupMembershipInput interface {
	pulumi.Input

	ToGroupMembershipOutput() GroupMembershipOutput
	ToGroupMembershipOutputWithContext(ctx context.Context) GroupMembershipOutput
}

func (*GroupMembership) ElementType() reflect.Type {
	return reflect.TypeOf((**GroupMembership)(nil)).Elem()
}

func (i *GroupMembership) ToGroupMembershipOutput() GroupMembershipOutput {
	return i.ToGroupMembershipOutputWithContext(context.Background())
}

func (i *GroupMembership) ToGroupMembershipOutputWithContext(ctx context.Context) GroupMembershipOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupMembershipOutput)
}

func (i *GroupMembership) ToOutput(ctx context.Context) pulumix.Output[*GroupMembership] {
	return pulumix.Output[*GroupMembership]{
		OutputState: i.ToGroupMembershipOutputWithContext(ctx).OutputState,
	}
}

// GroupMembershipArrayInput is an input type that accepts GroupMembershipArray and GroupMembershipArrayOutput values.
// You can construct a concrete instance of `GroupMembershipArrayInput` via:
//
//	GroupMembershipArray{ GroupMembershipArgs{...} }
type GroupMembershipArrayInput interface {
	pulumi.Input

	ToGroupMembershipArrayOutput() GroupMembershipArrayOutput
	ToGroupMembershipArrayOutputWithContext(context.Context) GroupMembershipArrayOutput
}

type GroupMembershipArray []GroupMembershipInput

func (GroupMembershipArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*GroupMembership)(nil)).Elem()
}

func (i GroupMembershipArray) ToGroupMembershipArrayOutput() GroupMembershipArrayOutput {
	return i.ToGroupMembershipArrayOutputWithContext(context.Background())
}

func (i GroupMembershipArray) ToGroupMembershipArrayOutputWithContext(ctx context.Context) GroupMembershipArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupMembershipArrayOutput)
}

func (i GroupMembershipArray) ToOutput(ctx context.Context) pulumix.Output[[]*GroupMembership] {
	return pulumix.Output[[]*GroupMembership]{
		OutputState: i.ToGroupMembershipArrayOutputWithContext(ctx).OutputState,
	}
}

// GroupMembershipMapInput is an input type that accepts GroupMembershipMap and GroupMembershipMapOutput values.
// You can construct a concrete instance of `GroupMembershipMapInput` via:
//
//	GroupMembershipMap{ "key": GroupMembershipArgs{...} }
type GroupMembershipMapInput interface {
	pulumi.Input

	ToGroupMembershipMapOutput() GroupMembershipMapOutput
	ToGroupMembershipMapOutputWithContext(context.Context) GroupMembershipMapOutput
}

type GroupMembershipMap map[string]GroupMembershipInput

func (GroupMembershipMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*GroupMembership)(nil)).Elem()
}

func (i GroupMembershipMap) ToGroupMembershipMapOutput() GroupMembershipMapOutput {
	return i.ToGroupMembershipMapOutputWithContext(context.Background())
}

func (i GroupMembershipMap) ToGroupMembershipMapOutputWithContext(ctx context.Context) GroupMembershipMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GroupMembershipMapOutput)
}

func (i GroupMembershipMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*GroupMembership] {
	return pulumix.Output[map[string]*GroupMembership]{
		OutputState: i.ToGroupMembershipMapOutputWithContext(ctx).OutputState,
	}
}

type GroupMembershipOutput struct{ *pulumi.OutputState }

func (GroupMembershipOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**GroupMembership)(nil)).Elem()
}

func (o GroupMembershipOutput) ToGroupMembershipOutput() GroupMembershipOutput {
	return o
}

func (o GroupMembershipOutput) ToGroupMembershipOutputWithContext(ctx context.Context) GroupMembershipOutput {
	return o
}

func (o GroupMembershipOutput) ToOutput(ctx context.Context) pulumix.Output[*GroupMembership] {
	return pulumix.Output[*GroupMembership]{
		OutputState: o.OutputState,
	}
}

func (o GroupMembershipOutput) GroupSlug() pulumi.StringOutput {
	return o.ApplyT(func(v *GroupMembership) pulumi.StringOutput { return v.GroupSlug }).(pulumi.StringOutput)
}

func (o GroupMembershipOutput) Slug() pulumi.StringOutput {
	return o.ApplyT(func(v *GroupMembership) pulumi.StringOutput { return v.Slug }).(pulumi.StringOutput)
}

func (o GroupMembershipOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v *GroupMembership) pulumi.StringOutput { return v.Uuid }).(pulumi.StringOutput)
}

func (o GroupMembershipOutput) Workspace() pulumi.StringOutput {
	return o.ApplyT(func(v *GroupMembership) pulumi.StringOutput { return v.Workspace }).(pulumi.StringOutput)
}

type GroupMembershipArrayOutput struct{ *pulumi.OutputState }

func (GroupMembershipArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*GroupMembership)(nil)).Elem()
}

func (o GroupMembershipArrayOutput) ToGroupMembershipArrayOutput() GroupMembershipArrayOutput {
	return o
}

func (o GroupMembershipArrayOutput) ToGroupMembershipArrayOutputWithContext(ctx context.Context) GroupMembershipArrayOutput {
	return o
}

func (o GroupMembershipArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*GroupMembership] {
	return pulumix.Output[[]*GroupMembership]{
		OutputState: o.OutputState,
	}
}

func (o GroupMembershipArrayOutput) Index(i pulumi.IntInput) GroupMembershipOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *GroupMembership {
		return vs[0].([]*GroupMembership)[vs[1].(int)]
	}).(GroupMembershipOutput)
}

type GroupMembershipMapOutput struct{ *pulumi.OutputState }

func (GroupMembershipMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*GroupMembership)(nil)).Elem()
}

func (o GroupMembershipMapOutput) ToGroupMembershipMapOutput() GroupMembershipMapOutput {
	return o
}

func (o GroupMembershipMapOutput) ToGroupMembershipMapOutputWithContext(ctx context.Context) GroupMembershipMapOutput {
	return o
}

func (o GroupMembershipMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*GroupMembership] {
	return pulumix.Output[map[string]*GroupMembership]{
		OutputState: o.OutputState,
	}
}

func (o GroupMembershipMapOutput) MapIndex(k pulumi.StringInput) GroupMembershipOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *GroupMembership {
		return vs[0].(map[string]*GroupMembership)[vs[1].(string)]
	}).(GroupMembershipOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*GroupMembershipInput)(nil)).Elem(), &GroupMembership{})
	pulumi.RegisterInputType(reflect.TypeOf((*GroupMembershipArrayInput)(nil)).Elem(), GroupMembershipArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GroupMembershipMapInput)(nil)).Elem(), GroupMembershipMap{})
	pulumi.RegisterOutputType(GroupMembershipOutput{})
	pulumi.RegisterOutputType(GroupMembershipArrayOutput{})
	pulumi.RegisterOutputType(GroupMembershipMapOutput{})
}
