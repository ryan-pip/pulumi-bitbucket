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

type BranchingModel struct {
	pulumi.CustomResourceState

	BranchTypes BranchingModelBranchTypeArrayOutput `pulumi:"branchTypes"`
	Development BranchingModelDevelopmentOutput     `pulumi:"development"`
	Owner       pulumi.StringOutput                 `pulumi:"owner"`
	Production  BranchingModelProductionPtrOutput   `pulumi:"production"`
	Repository  pulumi.StringOutput                 `pulumi:"repository"`
}

// NewBranchingModel registers a new resource with the given unique name, arguments, and options.
func NewBranchingModel(ctx *pulumi.Context,
	name string, args *BranchingModelArgs, opts ...pulumi.ResourceOption) (*BranchingModel, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Development == nil {
		return nil, errors.New("invalid value for required argument 'Development'")
	}
	if args.Owner == nil {
		return nil, errors.New("invalid value for required argument 'Owner'")
	}
	if args.Repository == nil {
		return nil, errors.New("invalid value for required argument 'Repository'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource BranchingModel
	err := ctx.RegisterResource("bitbucket:index/branchingModel:BranchingModel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBranchingModel gets an existing BranchingModel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBranchingModel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BranchingModelState, opts ...pulumi.ResourceOption) (*BranchingModel, error) {
	var resource BranchingModel
	err := ctx.ReadResource("bitbucket:index/branchingModel:BranchingModel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BranchingModel resources.
type branchingModelState struct {
	BranchTypes []BranchingModelBranchType `pulumi:"branchTypes"`
	Development *BranchingModelDevelopment `pulumi:"development"`
	Owner       *string                    `pulumi:"owner"`
	Production  *BranchingModelProduction  `pulumi:"production"`
	Repository  *string                    `pulumi:"repository"`
}

type BranchingModelState struct {
	BranchTypes BranchingModelBranchTypeArrayInput
	Development BranchingModelDevelopmentPtrInput
	Owner       pulumi.StringPtrInput
	Production  BranchingModelProductionPtrInput
	Repository  pulumi.StringPtrInput
}

func (BranchingModelState) ElementType() reflect.Type {
	return reflect.TypeOf((*branchingModelState)(nil)).Elem()
}

type branchingModelArgs struct {
	BranchTypes []BranchingModelBranchType `pulumi:"branchTypes"`
	Development BranchingModelDevelopment  `pulumi:"development"`
	Owner       string                     `pulumi:"owner"`
	Production  *BranchingModelProduction  `pulumi:"production"`
	Repository  string                     `pulumi:"repository"`
}

// The set of arguments for constructing a BranchingModel resource.
type BranchingModelArgs struct {
	BranchTypes BranchingModelBranchTypeArrayInput
	Development BranchingModelDevelopmentInput
	Owner       pulumi.StringInput
	Production  BranchingModelProductionPtrInput
	Repository  pulumi.StringInput
}

func (BranchingModelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*branchingModelArgs)(nil)).Elem()
}

type BranchingModelInput interface {
	pulumi.Input

	ToBranchingModelOutput() BranchingModelOutput
	ToBranchingModelOutputWithContext(ctx context.Context) BranchingModelOutput
}

func (*BranchingModel) ElementType() reflect.Type {
	return reflect.TypeOf((**BranchingModel)(nil)).Elem()
}

func (i *BranchingModel) ToBranchingModelOutput() BranchingModelOutput {
	return i.ToBranchingModelOutputWithContext(context.Background())
}

func (i *BranchingModel) ToBranchingModelOutputWithContext(ctx context.Context) BranchingModelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BranchingModelOutput)
}

func (i *BranchingModel) ToOutput(ctx context.Context) pulumix.Output[*BranchingModel] {
	return pulumix.Output[*BranchingModel]{
		OutputState: i.ToBranchingModelOutputWithContext(ctx).OutputState,
	}
}

// BranchingModelArrayInput is an input type that accepts BranchingModelArray and BranchingModelArrayOutput values.
// You can construct a concrete instance of `BranchingModelArrayInput` via:
//
//	BranchingModelArray{ BranchingModelArgs{...} }
type BranchingModelArrayInput interface {
	pulumi.Input

	ToBranchingModelArrayOutput() BranchingModelArrayOutput
	ToBranchingModelArrayOutputWithContext(context.Context) BranchingModelArrayOutput
}

type BranchingModelArray []BranchingModelInput

func (BranchingModelArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*BranchingModel)(nil)).Elem()
}

func (i BranchingModelArray) ToBranchingModelArrayOutput() BranchingModelArrayOutput {
	return i.ToBranchingModelArrayOutputWithContext(context.Background())
}

func (i BranchingModelArray) ToBranchingModelArrayOutputWithContext(ctx context.Context) BranchingModelArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BranchingModelArrayOutput)
}

func (i BranchingModelArray) ToOutput(ctx context.Context) pulumix.Output[[]*BranchingModel] {
	return pulumix.Output[[]*BranchingModel]{
		OutputState: i.ToBranchingModelArrayOutputWithContext(ctx).OutputState,
	}
}

// BranchingModelMapInput is an input type that accepts BranchingModelMap and BranchingModelMapOutput values.
// You can construct a concrete instance of `BranchingModelMapInput` via:
//
//	BranchingModelMap{ "key": BranchingModelArgs{...} }
type BranchingModelMapInput interface {
	pulumi.Input

	ToBranchingModelMapOutput() BranchingModelMapOutput
	ToBranchingModelMapOutputWithContext(context.Context) BranchingModelMapOutput
}

type BranchingModelMap map[string]BranchingModelInput

func (BranchingModelMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*BranchingModel)(nil)).Elem()
}

func (i BranchingModelMap) ToBranchingModelMapOutput() BranchingModelMapOutput {
	return i.ToBranchingModelMapOutputWithContext(context.Background())
}

func (i BranchingModelMap) ToBranchingModelMapOutputWithContext(ctx context.Context) BranchingModelMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(BranchingModelMapOutput)
}

func (i BranchingModelMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*BranchingModel] {
	return pulumix.Output[map[string]*BranchingModel]{
		OutputState: i.ToBranchingModelMapOutputWithContext(ctx).OutputState,
	}
}

type BranchingModelOutput struct{ *pulumi.OutputState }

func (BranchingModelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**BranchingModel)(nil)).Elem()
}

func (o BranchingModelOutput) ToBranchingModelOutput() BranchingModelOutput {
	return o
}

func (o BranchingModelOutput) ToBranchingModelOutputWithContext(ctx context.Context) BranchingModelOutput {
	return o
}

func (o BranchingModelOutput) ToOutput(ctx context.Context) pulumix.Output[*BranchingModel] {
	return pulumix.Output[*BranchingModel]{
		OutputState: o.OutputState,
	}
}

func (o BranchingModelOutput) BranchTypes() BranchingModelBranchTypeArrayOutput {
	return o.ApplyT(func(v *BranchingModel) BranchingModelBranchTypeArrayOutput { return v.BranchTypes }).(BranchingModelBranchTypeArrayOutput)
}

func (o BranchingModelOutput) Development() BranchingModelDevelopmentOutput {
	return o.ApplyT(func(v *BranchingModel) BranchingModelDevelopmentOutput { return v.Development }).(BranchingModelDevelopmentOutput)
}

func (o BranchingModelOutput) Owner() pulumi.StringOutput {
	return o.ApplyT(func(v *BranchingModel) pulumi.StringOutput { return v.Owner }).(pulumi.StringOutput)
}

func (o BranchingModelOutput) Production() BranchingModelProductionPtrOutput {
	return o.ApplyT(func(v *BranchingModel) BranchingModelProductionPtrOutput { return v.Production }).(BranchingModelProductionPtrOutput)
}

func (o BranchingModelOutput) Repository() pulumi.StringOutput {
	return o.ApplyT(func(v *BranchingModel) pulumi.StringOutput { return v.Repository }).(pulumi.StringOutput)
}

type BranchingModelArrayOutput struct{ *pulumi.OutputState }

func (BranchingModelArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*BranchingModel)(nil)).Elem()
}

func (o BranchingModelArrayOutput) ToBranchingModelArrayOutput() BranchingModelArrayOutput {
	return o
}

func (o BranchingModelArrayOutput) ToBranchingModelArrayOutputWithContext(ctx context.Context) BranchingModelArrayOutput {
	return o
}

func (o BranchingModelArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*BranchingModel] {
	return pulumix.Output[[]*BranchingModel]{
		OutputState: o.OutputState,
	}
}

func (o BranchingModelArrayOutput) Index(i pulumi.IntInput) BranchingModelOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *BranchingModel {
		return vs[0].([]*BranchingModel)[vs[1].(int)]
	}).(BranchingModelOutput)
}

type BranchingModelMapOutput struct{ *pulumi.OutputState }

func (BranchingModelMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*BranchingModel)(nil)).Elem()
}

func (o BranchingModelMapOutput) ToBranchingModelMapOutput() BranchingModelMapOutput {
	return o
}

func (o BranchingModelMapOutput) ToBranchingModelMapOutputWithContext(ctx context.Context) BranchingModelMapOutput {
	return o
}

func (o BranchingModelMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*BranchingModel] {
	return pulumix.Output[map[string]*BranchingModel]{
		OutputState: o.OutputState,
	}
}

func (o BranchingModelMapOutput) MapIndex(k pulumi.StringInput) BranchingModelOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *BranchingModel {
		return vs[0].(map[string]*BranchingModel)[vs[1].(string)]
	}).(BranchingModelOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*BranchingModelInput)(nil)).Elem(), &BranchingModel{})
	pulumi.RegisterInputType(reflect.TypeOf((*BranchingModelArrayInput)(nil)).Elem(), BranchingModelArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*BranchingModelMapInput)(nil)).Elem(), BranchingModelMap{})
	pulumi.RegisterOutputType(BranchingModelOutput{})
	pulumi.RegisterOutputType(BranchingModelArrayOutput{})
	pulumi.RegisterOutputType(BranchingModelMapOutput{})
}
