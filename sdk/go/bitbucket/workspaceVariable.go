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

type WorkspaceVariable struct {
	pulumi.CustomResourceState

	Key       pulumi.StringOutput  `pulumi:"key"`
	Secured   pulumi.BoolPtrOutput `pulumi:"secured"`
	Uuid      pulumi.StringOutput  `pulumi:"uuid"`
	Value     pulumi.StringOutput  `pulumi:"value"`
	Workspace pulumi.StringOutput  `pulumi:"workspace"`
}

// NewWorkspaceVariable registers a new resource with the given unique name, arguments, and options.
func NewWorkspaceVariable(ctx *pulumi.Context,
	name string, args *WorkspaceVariableArgs, opts ...pulumi.ResourceOption) (*WorkspaceVariable, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Key == nil {
		return nil, errors.New("invalid value for required argument 'Key'")
	}
	if args.Value == nil {
		return nil, errors.New("invalid value for required argument 'Value'")
	}
	if args.Workspace == nil {
		return nil, errors.New("invalid value for required argument 'Workspace'")
	}
	if args.Value != nil {
		args.Value = pulumi.ToSecret(args.Value).(pulumi.StringInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"value",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource WorkspaceVariable
	err := ctx.RegisterResource("bitbucket:index/workspaceVariable:WorkspaceVariable", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetWorkspaceVariable gets an existing WorkspaceVariable resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetWorkspaceVariable(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *WorkspaceVariableState, opts ...pulumi.ResourceOption) (*WorkspaceVariable, error) {
	var resource WorkspaceVariable
	err := ctx.ReadResource("bitbucket:index/workspaceVariable:WorkspaceVariable", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering WorkspaceVariable resources.
type workspaceVariableState struct {
	Key       *string `pulumi:"key"`
	Secured   *bool   `pulumi:"secured"`
	Uuid      *string `pulumi:"uuid"`
	Value     *string `pulumi:"value"`
	Workspace *string `pulumi:"workspace"`
}

type WorkspaceVariableState struct {
	Key       pulumi.StringPtrInput
	Secured   pulumi.BoolPtrInput
	Uuid      pulumi.StringPtrInput
	Value     pulumi.StringPtrInput
	Workspace pulumi.StringPtrInput
}

func (WorkspaceVariableState) ElementType() reflect.Type {
	return reflect.TypeOf((*workspaceVariableState)(nil)).Elem()
}

type workspaceVariableArgs struct {
	Key       string `pulumi:"key"`
	Secured   *bool  `pulumi:"secured"`
	Value     string `pulumi:"value"`
	Workspace string `pulumi:"workspace"`
}

// The set of arguments for constructing a WorkspaceVariable resource.
type WorkspaceVariableArgs struct {
	Key       pulumi.StringInput
	Secured   pulumi.BoolPtrInput
	Value     pulumi.StringInput
	Workspace pulumi.StringInput
}

func (WorkspaceVariableArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*workspaceVariableArgs)(nil)).Elem()
}

type WorkspaceVariableInput interface {
	pulumi.Input

	ToWorkspaceVariableOutput() WorkspaceVariableOutput
	ToWorkspaceVariableOutputWithContext(ctx context.Context) WorkspaceVariableOutput
}

func (*WorkspaceVariable) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkspaceVariable)(nil)).Elem()
}

func (i *WorkspaceVariable) ToWorkspaceVariableOutput() WorkspaceVariableOutput {
	return i.ToWorkspaceVariableOutputWithContext(context.Background())
}

func (i *WorkspaceVariable) ToWorkspaceVariableOutputWithContext(ctx context.Context) WorkspaceVariableOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspaceVariableOutput)
}

func (i *WorkspaceVariable) ToOutput(ctx context.Context) pulumix.Output[*WorkspaceVariable] {
	return pulumix.Output[*WorkspaceVariable]{
		OutputState: i.ToWorkspaceVariableOutputWithContext(ctx).OutputState,
	}
}

// WorkspaceVariableArrayInput is an input type that accepts WorkspaceVariableArray and WorkspaceVariableArrayOutput values.
// You can construct a concrete instance of `WorkspaceVariableArrayInput` via:
//
//	WorkspaceVariableArray{ WorkspaceVariableArgs{...} }
type WorkspaceVariableArrayInput interface {
	pulumi.Input

	ToWorkspaceVariableArrayOutput() WorkspaceVariableArrayOutput
	ToWorkspaceVariableArrayOutputWithContext(context.Context) WorkspaceVariableArrayOutput
}

type WorkspaceVariableArray []WorkspaceVariableInput

func (WorkspaceVariableArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*WorkspaceVariable)(nil)).Elem()
}

func (i WorkspaceVariableArray) ToWorkspaceVariableArrayOutput() WorkspaceVariableArrayOutput {
	return i.ToWorkspaceVariableArrayOutputWithContext(context.Background())
}

func (i WorkspaceVariableArray) ToWorkspaceVariableArrayOutputWithContext(ctx context.Context) WorkspaceVariableArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspaceVariableArrayOutput)
}

func (i WorkspaceVariableArray) ToOutput(ctx context.Context) pulumix.Output[[]*WorkspaceVariable] {
	return pulumix.Output[[]*WorkspaceVariable]{
		OutputState: i.ToWorkspaceVariableArrayOutputWithContext(ctx).OutputState,
	}
}

// WorkspaceVariableMapInput is an input type that accepts WorkspaceVariableMap and WorkspaceVariableMapOutput values.
// You can construct a concrete instance of `WorkspaceVariableMapInput` via:
//
//	WorkspaceVariableMap{ "key": WorkspaceVariableArgs{...} }
type WorkspaceVariableMapInput interface {
	pulumi.Input

	ToWorkspaceVariableMapOutput() WorkspaceVariableMapOutput
	ToWorkspaceVariableMapOutputWithContext(context.Context) WorkspaceVariableMapOutput
}

type WorkspaceVariableMap map[string]WorkspaceVariableInput

func (WorkspaceVariableMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*WorkspaceVariable)(nil)).Elem()
}

func (i WorkspaceVariableMap) ToWorkspaceVariableMapOutput() WorkspaceVariableMapOutput {
	return i.ToWorkspaceVariableMapOutputWithContext(context.Background())
}

func (i WorkspaceVariableMap) ToWorkspaceVariableMapOutputWithContext(ctx context.Context) WorkspaceVariableMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(WorkspaceVariableMapOutput)
}

func (i WorkspaceVariableMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*WorkspaceVariable] {
	return pulumix.Output[map[string]*WorkspaceVariable]{
		OutputState: i.ToWorkspaceVariableMapOutputWithContext(ctx).OutputState,
	}
}

type WorkspaceVariableOutput struct{ *pulumi.OutputState }

func (WorkspaceVariableOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**WorkspaceVariable)(nil)).Elem()
}

func (o WorkspaceVariableOutput) ToWorkspaceVariableOutput() WorkspaceVariableOutput {
	return o
}

func (o WorkspaceVariableOutput) ToWorkspaceVariableOutputWithContext(ctx context.Context) WorkspaceVariableOutput {
	return o
}

func (o WorkspaceVariableOutput) ToOutput(ctx context.Context) pulumix.Output[*WorkspaceVariable] {
	return pulumix.Output[*WorkspaceVariable]{
		OutputState: o.OutputState,
	}
}

func (o WorkspaceVariableOutput) Key() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkspaceVariable) pulumi.StringOutput { return v.Key }).(pulumi.StringOutput)
}

func (o WorkspaceVariableOutput) Secured() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *WorkspaceVariable) pulumi.BoolPtrOutput { return v.Secured }).(pulumi.BoolPtrOutput)
}

func (o WorkspaceVariableOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkspaceVariable) pulumi.StringOutput { return v.Uuid }).(pulumi.StringOutput)
}

func (o WorkspaceVariableOutput) Value() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkspaceVariable) pulumi.StringOutput { return v.Value }).(pulumi.StringOutput)
}

func (o WorkspaceVariableOutput) Workspace() pulumi.StringOutput {
	return o.ApplyT(func(v *WorkspaceVariable) pulumi.StringOutput { return v.Workspace }).(pulumi.StringOutput)
}

type WorkspaceVariableArrayOutput struct{ *pulumi.OutputState }

func (WorkspaceVariableArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*WorkspaceVariable)(nil)).Elem()
}

func (o WorkspaceVariableArrayOutput) ToWorkspaceVariableArrayOutput() WorkspaceVariableArrayOutput {
	return o
}

func (o WorkspaceVariableArrayOutput) ToWorkspaceVariableArrayOutputWithContext(ctx context.Context) WorkspaceVariableArrayOutput {
	return o
}

func (o WorkspaceVariableArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*WorkspaceVariable] {
	return pulumix.Output[[]*WorkspaceVariable]{
		OutputState: o.OutputState,
	}
}

func (o WorkspaceVariableArrayOutput) Index(i pulumi.IntInput) WorkspaceVariableOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *WorkspaceVariable {
		return vs[0].([]*WorkspaceVariable)[vs[1].(int)]
	}).(WorkspaceVariableOutput)
}

type WorkspaceVariableMapOutput struct{ *pulumi.OutputState }

func (WorkspaceVariableMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*WorkspaceVariable)(nil)).Elem()
}

func (o WorkspaceVariableMapOutput) ToWorkspaceVariableMapOutput() WorkspaceVariableMapOutput {
	return o
}

func (o WorkspaceVariableMapOutput) ToWorkspaceVariableMapOutputWithContext(ctx context.Context) WorkspaceVariableMapOutput {
	return o
}

func (o WorkspaceVariableMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*WorkspaceVariable] {
	return pulumix.Output[map[string]*WorkspaceVariable]{
		OutputState: o.OutputState,
	}
}

func (o WorkspaceVariableMapOutput) MapIndex(k pulumi.StringInput) WorkspaceVariableOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *WorkspaceVariable {
		return vs[0].(map[string]*WorkspaceVariable)[vs[1].(string)]
	}).(WorkspaceVariableOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*WorkspaceVariableInput)(nil)).Elem(), &WorkspaceVariable{})
	pulumi.RegisterInputType(reflect.TypeOf((*WorkspaceVariableArrayInput)(nil)).Elem(), WorkspaceVariableArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*WorkspaceVariableMapInput)(nil)).Elem(), WorkspaceVariableMap{})
	pulumi.RegisterOutputType(WorkspaceVariableOutput{})
	pulumi.RegisterOutputType(WorkspaceVariableArrayOutput{})
	pulumi.RegisterOutputType(WorkspaceVariableMapOutput{})
}
