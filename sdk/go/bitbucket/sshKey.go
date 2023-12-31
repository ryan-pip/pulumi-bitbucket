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

type SshKey struct {
	pulumi.CustomResourceState

	Comment pulumi.StringOutput    `pulumi:"comment"`
	Key     pulumi.StringPtrOutput `pulumi:"key"`
	Label   pulumi.StringPtrOutput `pulumi:"label"`
	User    pulumi.StringOutput    `pulumi:"user"`
	Uuid    pulumi.StringOutput    `pulumi:"uuid"`
}

// NewSshKey registers a new resource with the given unique name, arguments, and options.
func NewSshKey(ctx *pulumi.Context,
	name string, args *SshKeyArgs, opts ...pulumi.ResourceOption) (*SshKey, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.User == nil {
		return nil, errors.New("invalid value for required argument 'User'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SshKey
	err := ctx.RegisterResource("bitbucket:index/sshKey:SshKey", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSshKey gets an existing SshKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSshKey(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SshKeyState, opts ...pulumi.ResourceOption) (*SshKey, error) {
	var resource SshKey
	err := ctx.ReadResource("bitbucket:index/sshKey:SshKey", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SshKey resources.
type sshKeyState struct {
	Comment *string `pulumi:"comment"`
	Key     *string `pulumi:"key"`
	Label   *string `pulumi:"label"`
	User    *string `pulumi:"user"`
	Uuid    *string `pulumi:"uuid"`
}

type SshKeyState struct {
	Comment pulumi.StringPtrInput
	Key     pulumi.StringPtrInput
	Label   pulumi.StringPtrInput
	User    pulumi.StringPtrInput
	Uuid    pulumi.StringPtrInput
}

func (SshKeyState) ElementType() reflect.Type {
	return reflect.TypeOf((*sshKeyState)(nil)).Elem()
}

type sshKeyArgs struct {
	Key   *string `pulumi:"key"`
	Label *string `pulumi:"label"`
	User  string  `pulumi:"user"`
}

// The set of arguments for constructing a SshKey resource.
type SshKeyArgs struct {
	Key   pulumi.StringPtrInput
	Label pulumi.StringPtrInput
	User  pulumi.StringInput
}

func (SshKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*sshKeyArgs)(nil)).Elem()
}

type SshKeyInput interface {
	pulumi.Input

	ToSshKeyOutput() SshKeyOutput
	ToSshKeyOutputWithContext(ctx context.Context) SshKeyOutput
}

func (*SshKey) ElementType() reflect.Type {
	return reflect.TypeOf((**SshKey)(nil)).Elem()
}

func (i *SshKey) ToSshKeyOutput() SshKeyOutput {
	return i.ToSshKeyOutputWithContext(context.Background())
}

func (i *SshKey) ToSshKeyOutputWithContext(ctx context.Context) SshKeyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SshKeyOutput)
}

func (i *SshKey) ToOutput(ctx context.Context) pulumix.Output[*SshKey] {
	return pulumix.Output[*SshKey]{
		OutputState: i.ToSshKeyOutputWithContext(ctx).OutputState,
	}
}

// SshKeyArrayInput is an input type that accepts SshKeyArray and SshKeyArrayOutput values.
// You can construct a concrete instance of `SshKeyArrayInput` via:
//
//	SshKeyArray{ SshKeyArgs{...} }
type SshKeyArrayInput interface {
	pulumi.Input

	ToSshKeyArrayOutput() SshKeyArrayOutput
	ToSshKeyArrayOutputWithContext(context.Context) SshKeyArrayOutput
}

type SshKeyArray []SshKeyInput

func (SshKeyArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SshKey)(nil)).Elem()
}

func (i SshKeyArray) ToSshKeyArrayOutput() SshKeyArrayOutput {
	return i.ToSshKeyArrayOutputWithContext(context.Background())
}

func (i SshKeyArray) ToSshKeyArrayOutputWithContext(ctx context.Context) SshKeyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SshKeyArrayOutput)
}

func (i SshKeyArray) ToOutput(ctx context.Context) pulumix.Output[[]*SshKey] {
	return pulumix.Output[[]*SshKey]{
		OutputState: i.ToSshKeyArrayOutputWithContext(ctx).OutputState,
	}
}

// SshKeyMapInput is an input type that accepts SshKeyMap and SshKeyMapOutput values.
// You can construct a concrete instance of `SshKeyMapInput` via:
//
//	SshKeyMap{ "key": SshKeyArgs{...} }
type SshKeyMapInput interface {
	pulumi.Input

	ToSshKeyMapOutput() SshKeyMapOutput
	ToSshKeyMapOutputWithContext(context.Context) SshKeyMapOutput
}

type SshKeyMap map[string]SshKeyInput

func (SshKeyMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SshKey)(nil)).Elem()
}

func (i SshKeyMap) ToSshKeyMapOutput() SshKeyMapOutput {
	return i.ToSshKeyMapOutputWithContext(context.Background())
}

func (i SshKeyMap) ToSshKeyMapOutputWithContext(ctx context.Context) SshKeyMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SshKeyMapOutput)
}

func (i SshKeyMap) ToOutput(ctx context.Context) pulumix.Output[map[string]*SshKey] {
	return pulumix.Output[map[string]*SshKey]{
		OutputState: i.ToSshKeyMapOutputWithContext(ctx).OutputState,
	}
}

type SshKeyOutput struct{ *pulumi.OutputState }

func (SshKeyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SshKey)(nil)).Elem()
}

func (o SshKeyOutput) ToSshKeyOutput() SshKeyOutput {
	return o
}

func (o SshKeyOutput) ToSshKeyOutputWithContext(ctx context.Context) SshKeyOutput {
	return o
}

func (o SshKeyOutput) ToOutput(ctx context.Context) pulumix.Output[*SshKey] {
	return pulumix.Output[*SshKey]{
		OutputState: o.OutputState,
	}
}

func (o SshKeyOutput) Comment() pulumi.StringOutput {
	return o.ApplyT(func(v *SshKey) pulumi.StringOutput { return v.Comment }).(pulumi.StringOutput)
}

func (o SshKeyOutput) Key() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SshKey) pulumi.StringPtrOutput { return v.Key }).(pulumi.StringPtrOutput)
}

func (o SshKeyOutput) Label() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SshKey) pulumi.StringPtrOutput { return v.Label }).(pulumi.StringPtrOutput)
}

func (o SshKeyOutput) User() pulumi.StringOutput {
	return o.ApplyT(func(v *SshKey) pulumi.StringOutput { return v.User }).(pulumi.StringOutput)
}

func (o SshKeyOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v *SshKey) pulumi.StringOutput { return v.Uuid }).(pulumi.StringOutput)
}

type SshKeyArrayOutput struct{ *pulumi.OutputState }

func (SshKeyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*SshKey)(nil)).Elem()
}

func (o SshKeyArrayOutput) ToSshKeyArrayOutput() SshKeyArrayOutput {
	return o
}

func (o SshKeyArrayOutput) ToSshKeyArrayOutputWithContext(ctx context.Context) SshKeyArrayOutput {
	return o
}

func (o SshKeyArrayOutput) ToOutput(ctx context.Context) pulumix.Output[[]*SshKey] {
	return pulumix.Output[[]*SshKey]{
		OutputState: o.OutputState,
	}
}

func (o SshKeyArrayOutput) Index(i pulumi.IntInput) SshKeyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *SshKey {
		return vs[0].([]*SshKey)[vs[1].(int)]
	}).(SshKeyOutput)
}

type SshKeyMapOutput struct{ *pulumi.OutputState }

func (SshKeyMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*SshKey)(nil)).Elem()
}

func (o SshKeyMapOutput) ToSshKeyMapOutput() SshKeyMapOutput {
	return o
}

func (o SshKeyMapOutput) ToSshKeyMapOutputWithContext(ctx context.Context) SshKeyMapOutput {
	return o
}

func (o SshKeyMapOutput) ToOutput(ctx context.Context) pulumix.Output[map[string]*SshKey] {
	return pulumix.Output[map[string]*SshKey]{
		OutputState: o.OutputState,
	}
}

func (o SshKeyMapOutput) MapIndex(k pulumi.StringInput) SshKeyOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *SshKey {
		return vs[0].(map[string]*SshKey)[vs[1].(string)]
	}).(SshKeyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SshKeyInput)(nil)).Elem(), &SshKey{})
	pulumi.RegisterInputType(reflect.TypeOf((*SshKeyArrayInput)(nil)).Elem(), SshKeyArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*SshKeyMapInput)(nil)).Elem(), SshKeyMap{})
	pulumi.RegisterOutputType(SshKeyOutput{})
	pulumi.RegisterOutputType(SshKeyArrayOutput{})
	pulumi.RegisterOutputType(SshKeyMapOutput{})
}
