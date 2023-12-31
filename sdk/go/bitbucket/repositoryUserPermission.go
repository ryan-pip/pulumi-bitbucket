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

type RepositoryUserPermission struct {
	pulumi.CustomResourceState

	Permission pulumi.StringOutput `pulumi:"permission"`
	RepoSlug   pulumi.StringOutput `pulumi:"repoSlug"`
	UserId     pulumi.StringOutput `pulumi:"userId"`
	Workspace  pulumi.StringOutput `pulumi:"workspace"`
}

// NewRepositoryUserPermission registers a new resource with the given unique name, arguments, and options.
func NewRepositoryUserPermission(ctx *pulumi.Context,
	name string, args *RepositoryUserPermissionArgs, opts ...pulumi.ResourceOption) (*RepositoryUserPermission, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Permission == nil {
		return nil, errors.New("invalid value for required argument 'Permission'")
	}
	if args.RepoSlug == nil {
		return nil, errors.New("invalid value for required argument 'RepoSlug'")
	}
	if args.UserId == nil {
		return nil, errors.New("invalid value for required argument 'UserId'")
	}
	if args.Workspace == nil {
		return nil, errors.New("invalid value for required argument 'Workspace'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource RepositoryUserPermission
	err := ctx.RegisterResource("bitbucket:index/repositoryUserPermission:RepositoryUserPermission", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRepositoryUserPermission gets an existing RepositoryUserPermission resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRepositoryUserPermission(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RepositoryUserPermissionState, opts ...pulumi.ResourceOption) (*RepositoryUserPermission, error) {
	var resource RepositoryUserPermission
	err := ctx.ReadResource("bitbucket:index/repositoryUserPermission:RepositoryUserPermission", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RepositoryUserPermission resources.
type repositoryUserPermissionState struct {
	Permission *string `pulumi:"permission"`
	RepoSlug   *string `pulumi:"repoSlug"`
	UserId     *string `pulumi:"userId"`
	Workspace  *string `pulumi:"workspace"`
}

type RepositoryUserPermissionState struct {
	Permission pulumi.StringPtrInput
	RepoSlug   pulumi.StringPtrInput
	UserId     pulumi.StringPtrInput
	Workspace  pulumi.StringPtrInput
}

func (RepositoryUserPermissionState) ElementType() reflect.Type {
	return reflect.TypeOf((*repositoryUserPermissionState)(nil)).Elem()
}

type repositoryUserPermissionArgs struct {
	Permission string `pulumi:"permission"`
	RepoSlug   string `pulumi:"repoSlug"`
	UserId     string `pulumi:"userId"`
	Workspace  string `pulumi:"workspace"`
}

// The set of arguments for constructing a RepositoryUserPermission resource.
type RepositoryUserPermissionArgs struct {
	Permission pulumi.StringInput
	RepoSlug   pulumi.StringInput
	UserId     pulumi.StringInput
	Workspace  pulumi.StringInput
}

func (RepositoryUserPermissionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*repositoryUserPermissionArgs)(nil)).Elem()
}

type RepositoryUserPermissionInput interface {
	pulumi.Input

	ToRepositoryUserPermissionOutput() RepositoryUserPermissionOutput
	ToRepositoryUserPermissionOutputWithContext(ctx context.Context) RepositoryUserPermissionOutput
}

func (*RepositoryUserPermission) ElementType() reflect.Type {
	return reflect.TypeOf((**RepositoryUserPermission)(nil)).Elem()
}

func (i *RepositoryUserPermission) ToRepositoryUserPermissionOutput() RepositoryUserPermissionOutput {
	return i.ToRepositoryUserPermissionOutputWithContext(context.Background())
}

func (i *RepositoryUserPermission) ToRepositoryUserPermissionOutputWithContext(ctx context.Context) RepositoryUserPermissionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RepositoryUserPermissionOutput)
}

func (i *RepositoryUserPermission) ToOutput(ctx context.Context) pulumix.Output[*RepositoryUserPermission] {
	return pulumix.Output[*RepositoryUserPermission]{
		OutputState: i.ToRepositoryUserPermissionOutputWithContext(ctx).OutputState,
	}
}

// RepositoryUserPermissionArrayInput is an input type that accepts RepositoryUserPermissionArray and RepositoryUserPermissionArrayOutput values.
// You can construct a concrete instance of `RepositoryUserPermissionArrayInput` via:
//
//	RepositoryUserPermissionArray{ RepositoryUserPermissionArgs{...} }
type RepositoryUserPermissionArrayInput interface {
	pulumi.Input

	ToRepositoryUserPermissionArrayOutput() RepositoryUserPermissionArrayOutput
	ToRepositoryUserPermissionArrayOutputWithContext(context.Context) RepositoryUserPermissionArrayOutput
}

type RepositoryUserPermissionArray []RepositoryUserPermissionInput

func (RepositoryUserPermissionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RepositoryUserPermission)(nil)).Elem()
}

func (i RepositoryUserPermissionArray) ToRepositoryUserPermissionArrayOutput() RepositoryUserPermissionArrayOutput {
	return i.ToRepositoryUserPermissionArrayOutputWithContext(context.Background())
}

func (i RepositoryUserPermissionArray) ToRepositoryUserPermissionArrayOutputWithContext(ctx context.Context) RepositoryUserPermissionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RepositoryUserPermissionArrayOutput)
}

func (i RepositoryUserPermissionArray) ToOutput(ctx context.Context) pulumix.Output[[]*RepositoryUserPermission] {
	return pulumix.Output[[]*RepositoryUserPermission]{
		OutputState: i.ToRepositoryUserPermissionArrayOutputWithContext(ctx).OutputState,
	}
}

// RepositoryUserPermissionMapInput is an input type that accepts RepositoryUserPermissionMap and RepositoryUserPermissionMapOutput values.
// You can construct a concrete instance of `RepositoryUserPermissionMapInput` via:
//
//	RepositoryUserPermissionMap{ "key": RepositoryUserPermissionArgs{...} }
type RepositoryUserPermissionMapInput interface {
	pulumi.Input

	ToRepositoryUserPermissionMapOutput() RepositoryUserPermissionMapOutput
	ToRepositoryUserPermissionMapOutputWithContext(context.Context) RepositoryUserPermissionMapOutput
}

type RepositoryUserPermissionMap map[string]RepositoryUserPermissionInput

func (RepositoryUserPermissionMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RepositoryUserPermission)(nil)).Elem()
}

func (i RepositoryUserPermissionMap) ToRepositoryUserPermissionMapOutput() RepositoryUserPermissionMapOutput {
	return i.ToRepositoryUserPermissionMapOutputWithContext(context.Background())
}

func (i RepositoryUserPermissionMap) ToRepositoryUserPermissionMapOutputWithContext(ctx context.Context) RepositoryUserPermissionMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RepositoryUserPermissionMapOutput)
}

func (i RepositoryUserPermissionMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*RepositoryUserPermission] {
	return pulumix.Output[map[string]*RepositoryUserPermission]{
		OutputState: i.ToRepositoryUserPermissionMapOutputWithContext(ctx).OutputState,
	}
}

type RepositoryUserPermissionOutput struct{ *pulumi.OutputState }

func (RepositoryUserPermissionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RepositoryUserPermission)(nil)).Elem()
}

func (o RepositoryUserPermissionOutput) ToRepositoryUserPermissionOutput() RepositoryUserPermissionOutput {
	return o
}

func (o RepositoryUserPermissionOutput) ToRepositoryUserPermissionOutputWithContext(ctx context.Context) RepositoryUserPermissionOutput {
	return o
}

func (o RepositoryUserPermissionOutput) ToOutput(ctx context.Context) pulumix.Output[*RepositoryUserPermission] {
	return pulumix.Output[*RepositoryUserPermission]{
		OutputState: o.OutputState,
	}
}

func (o RepositoryUserPermissionOutput) Permission() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryUserPermission) pulumi.StringOutput { return v.Permission }).(pulumi.StringOutput)
}

func (o RepositoryUserPermissionOutput) RepoSlug() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryUserPermission) pulumi.StringOutput { return v.RepoSlug }).(pulumi.StringOutput)
}

func (o RepositoryUserPermissionOutput) UserId() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryUserPermission) pulumi.StringOutput { return v.UserId }).(pulumi.StringOutput)
}

func (o RepositoryUserPermissionOutput) Workspace() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryUserPermission) pulumi.StringOutput { return v.Workspace }).(pulumi.StringOutput)
}

type RepositoryUserPermissionArrayOutput struct{ *pulumi.OutputState }

func (RepositoryUserPermissionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RepositoryUserPermission)(nil)).Elem()
}

func (o RepositoryUserPermissionArrayOutput) ToRepositoryUserPermissionArrayOutput() RepositoryUserPermissionArrayOutput {
	return o
}

func (o RepositoryUserPermissionArrayOutput) ToRepositoryUserPermissionArrayOutputWithContext(ctx context.Context) RepositoryUserPermissionArrayOutput {
	return o
}

func (o RepositoryUserPermissionArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*RepositoryUserPermission] {
	return pulumix.Output[[]*RepositoryUserPermission]{
		OutputState: o.OutputState,
	}
}

func (o RepositoryUserPermissionArrayOutput) Index(i pulumi.IntInput) RepositoryUserPermissionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *RepositoryUserPermission {
		return vs[0].([]*RepositoryUserPermission)[vs[1].(int)]
	}).(RepositoryUserPermissionOutput)
}

type RepositoryUserPermissionMapOutput struct{ *pulumi.OutputState }

func (RepositoryUserPermissionMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RepositoryUserPermission)(nil)).Elem()
}

func (o RepositoryUserPermissionMapOutput) ToRepositoryUserPermissionMapOutput() RepositoryUserPermissionMapOutput {
	return o
}

func (o RepositoryUserPermissionMapOutput) ToRepositoryUserPermissionMapOutputWithContext(ctx context.Context) RepositoryUserPermissionMapOutput {
	return o
}

func (o RepositoryUserPermissionMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*RepositoryUserPermission] {
	return pulumix.Output[map[string]*RepositoryUserPermission]{
		OutputState: o.OutputState,
	}
}

func (o RepositoryUserPermissionMapOutput) MapIndex(k pulumi.StringInput) RepositoryUserPermissionOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *RepositoryUserPermission {
		return vs[0].(map[string]*RepositoryUserPermission)[vs[1].(string)]
	}).(RepositoryUserPermissionOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RepositoryUserPermissionInput)(nil)).Elem(), &RepositoryUserPermission{})
	pulumi.RegisterInputType(reflect.TypeOf((*RepositoryUserPermissionArrayInput)(nil)).Elem(), RepositoryUserPermissionArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*RepositoryUserPermissionMapInput)(nil)).Elem(), RepositoryUserPermissionMap{})
	pulumi.RegisterOutputType(RepositoryUserPermissionOutput{})
	pulumi.RegisterOutputType(RepositoryUserPermissionArrayOutput{})
	pulumi.RegisterOutputType(RepositoryUserPermissionMapOutput{})
}
