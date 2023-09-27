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

type DeploymentVariable struct {
	pulumi.CustomResourceState

	Deployment pulumi.StringOutput  `pulumi:"deployment"`
	Key        pulumi.StringOutput  `pulumi:"key"`
	Secured    pulumi.BoolPtrOutput `pulumi:"secured"`
	Uuid       pulumi.StringOutput  `pulumi:"uuid"`
	Value      pulumi.StringOutput  `pulumi:"value"`
}

// NewDeploymentVariable registers a new resource with the given unique name, arguments, and options.
func NewDeploymentVariable(ctx *pulumi.Context,
	name string, args *DeploymentVariableArgs, opts ...pulumi.ResourceOption) (*DeploymentVariable, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Deployment == nil {
		return nil, errors.New("invalid value for required argument 'Deployment'")
	}
	if args.Key == nil {
		return nil, errors.New("invalid value for required argument 'Key'")
	}
	if args.Value == nil {
		return nil, errors.New("invalid value for required argument 'Value'")
	}
	if args.Value != nil {
		args.Value = pulumi.ToSecret(args.Value).(pulumi.StringInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"value",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DeploymentVariable
	err := ctx.RegisterResource("bitbucket:index/deploymentVariable:DeploymentVariable", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDeploymentVariable gets an existing DeploymentVariable resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDeploymentVariable(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DeploymentVariableState, opts ...pulumi.ResourceOption) (*DeploymentVariable, error) {
	var resource DeploymentVariable
	err := ctx.ReadResource("bitbucket:index/deploymentVariable:DeploymentVariable", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DeploymentVariable resources.
type deploymentVariableState struct {
	Deployment *string `pulumi:"deployment"`
	Key        *string `pulumi:"key"`
	Secured    *bool   `pulumi:"secured"`
	Uuid       *string `pulumi:"uuid"`
	Value      *string `pulumi:"value"`
}

type DeploymentVariableState struct {
	Deployment pulumi.StringPtrInput
	Key        pulumi.StringPtrInput
	Secured    pulumi.BoolPtrInput
	Uuid       pulumi.StringPtrInput
	Value      pulumi.StringPtrInput
}

func (DeploymentVariableState) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentVariableState)(nil)).Elem()
}

type deploymentVariableArgs struct {
	Deployment string `pulumi:"deployment"`
	Key        string `pulumi:"key"`
	Secured    *bool  `pulumi:"secured"`
	Value      string `pulumi:"value"`
}

// The set of arguments for constructing a DeploymentVariable resource.
type DeploymentVariableArgs struct {
	Deployment pulumi.StringInput
	Key        pulumi.StringInput
	Secured    pulumi.BoolPtrInput
	Value      pulumi.StringInput
}

func (DeploymentVariableArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*deploymentVariableArgs)(nil)).Elem()
}

type DeploymentVariableInput interface {
	pulumi.Input

	ToDeploymentVariableOutput() DeploymentVariableOutput
	ToDeploymentVariableOutputWithContext(ctx context.Context) DeploymentVariableOutput
}

func (*DeploymentVariable) ElementType() reflect.Type {
	return reflect.TypeOf((**DeploymentVariable)(nil)).Elem()
}

func (i *DeploymentVariable) ToDeploymentVariableOutput() DeploymentVariableOutput {
	return i.ToDeploymentVariableOutputWithContext(context.Background())
}

func (i *DeploymentVariable) ToDeploymentVariableOutputWithContext(ctx context.Context) DeploymentVariableOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeploymentVariableOutput)
}

func (i *DeploymentVariable) ToOutput(ctx context.Context) pulumix.Output[*DeploymentVariable] {
	return pulumix.Output[*DeploymentVariable]{
		OutputState: i.ToDeploymentVariableOutputWithContext(ctx).OutputState,
	}
}

// DeploymentVariableArrayInput is an input type that accepts DeploymentVariableArray and DeploymentVariableArrayOutput values.
// You can construct a concrete instance of `DeploymentVariableArrayInput` via:
//
//	DeploymentVariableArray{ DeploymentVariableArgs{...} }
type DeploymentVariableArrayInput interface {
	pulumi.Input

	ToDeploymentVariableArrayOutput() DeploymentVariableArrayOutput
	ToDeploymentVariableArrayOutputWithContext(context.Context) DeploymentVariableArrayOutput
}

type DeploymentVariableArray []DeploymentVariableInput

func (DeploymentVariableArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DeploymentVariable)(nil)).Elem()
}

func (i DeploymentVariableArray) ToDeploymentVariableArrayOutput() DeploymentVariableArrayOutput {
	return i.ToDeploymentVariableArrayOutputWithContext(context.Background())
}

func (i DeploymentVariableArray) ToDeploymentVariableArrayOutputWithContext(ctx context.Context) DeploymentVariableArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeploymentVariableArrayOutput)
}

func (i DeploymentVariableArray) ToOutput(ctx context.Context) pulumix.Output[[]*DeploymentVariable] {
	return pulumix.Output[[]*DeploymentVariable]{
		OutputState: i.ToDeploymentVariableArrayOutputWithContext(ctx).OutputState,
	}
}

// DeploymentVariableMapInput is an input type that accepts DeploymentVariableMap and DeploymentVariableMapOutput values.
// You can construct a concrete instance of `DeploymentVariableMapInput` via:
//
//	DeploymentVariableMap{ "key": DeploymentVariableArgs{...} }
type DeploymentVariableMapInput interface {
	pulumi.Input

	ToDeploymentVariableMapOutput() DeploymentVariableMapOutput
	ToDeploymentVariableMapOutputWithContext(context.Context) DeploymentVariableMapOutput
}

type DeploymentVariableMap map[string]DeploymentVariableInput

func (DeploymentVariableMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DeploymentVariable)(nil)).Elem()
}

func (i DeploymentVariableMap) ToDeploymentVariableMapOutput() DeploymentVariableMapOutput {
	return i.ToDeploymentVariableMapOutputWithContext(context.Background())
}

func (i DeploymentVariableMap) ToDeploymentVariableMapOutputWithContext(ctx context.Context) DeploymentVariableMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DeploymentVariableMapOutput)
}

func (i DeploymentVariableMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*DeploymentVariable] {
	return pulumix.Output[map[string]*DeploymentVariable]{
		OutputState: i.ToDeploymentVariableMapOutputWithContext(ctx).OutputState,
	}
}

type DeploymentVariableOutput struct{ *pulumi.OutputState }

func (DeploymentVariableOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DeploymentVariable)(nil)).Elem()
}

func (o DeploymentVariableOutput) ToDeploymentVariableOutput() DeploymentVariableOutput {
	return o
}

func (o DeploymentVariableOutput) ToDeploymentVariableOutputWithContext(ctx context.Context) DeploymentVariableOutput {
	return o
}

func (o DeploymentVariableOutput) ToOutput(ctx context.Context) pulumix.Output[*DeploymentVariable] {
	return pulumix.Output[*DeploymentVariable]{
		OutputState: o.OutputState,
	}
}

func (o DeploymentVariableOutput) Deployment() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentVariable) pulumi.StringOutput { return v.Deployment }).(pulumi.StringOutput)
}

func (o DeploymentVariableOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentVariable) pulumi.StringOutput { return v.Key }).(pulumi.StringOutput)
}

func (o DeploymentVariableOutput) Secured() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *DeploymentVariable) pulumi.BoolPtrOutput { return v.Secured }).(pulumi.BoolPtrOutput)
}

func (o DeploymentVariableOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentVariable) pulumi.StringOutput { return v.Uuid }).(pulumi.StringOutput)
}

func (o DeploymentVariableOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v *DeploymentVariable) pulumi.StringOutput { return v.Value }).(pulumi.StringOutput)
}

type DeploymentVariableArrayOutput struct{ *pulumi.OutputState }

func (DeploymentVariableArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*DeploymentVariable)(nil)).Elem()
}

func (o DeploymentVariableArrayOutput) ToDeploymentVariableArrayOutput() DeploymentVariableArrayOutput {
	return o
}

func (o DeploymentVariableArrayOutput) ToDeploymentVariableArrayOutputWithContext(ctx context.Context) DeploymentVariableArrayOutput {
	return o
}

func (o DeploymentVariableArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*DeploymentVariable] {
	return pulumix.Output[[]*DeploymentVariable]{
		OutputState: o.OutputState,
	}
}

func (o DeploymentVariableArrayOutput) Index(i pulumi.IntInput) DeploymentVariableOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *DeploymentVariable {
		return vs[0].([]*DeploymentVariable)[vs[1].(int)]
	}).(DeploymentVariableOutput)
}

type DeploymentVariableMapOutput struct{ *pulumi.OutputState }

func (DeploymentVariableMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*DeploymentVariable)(nil)).Elem()
}

func (o DeploymentVariableMapOutput) ToDeploymentVariableMapOutput() DeploymentVariableMapOutput {
	return o
}

func (o DeploymentVariableMapOutput) ToDeploymentVariableMapOutputWithContext(ctx context.Context) DeploymentVariableMapOutput {
	return o
}

func (o DeploymentVariableMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*DeploymentVariable] {
	return pulumix.Output[map[string]*DeploymentVariable]{
		OutputState: o.OutputState,
	}
}

func (o DeploymentVariableMapOutput) MapIndex(k pulumi.StringInput) DeploymentVariableOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *DeploymentVariable {
		return vs[0].(map[string]*DeploymentVariable)[vs[1].(string)]
	}).(DeploymentVariableOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DeploymentVariableInput)(nil)).Elem(), &DeploymentVariable{})
	pulumi.RegisterInputType(reflect.TypeOf((*DeploymentVariableArrayInput)(nil)).Elem(), DeploymentVariableArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DeploymentVariableMapInput)(nil)).Elem(), DeploymentVariableMap{})
	pulumi.RegisterOutputType(DeploymentVariableOutput{})
	pulumi.RegisterOutputType(DeploymentVariableArrayOutput{})
	pulumi.RegisterOutputType(DeploymentVariableMapOutput{})
}
