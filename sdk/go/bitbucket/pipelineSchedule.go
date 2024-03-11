// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package bitbucket

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/ryan-pip/pulumi-bitbucket/sdk/go/bitbucket/internal"
)

// Provides a Bitbucket Pipeline Schedule resource.
//
// This allows you to manage your Pipeline Schedules for a repository.
//
// OAuth2 Scopes: `none`
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
//			_, err := bitbucket.NewPipelineSchedule(ctx, "test", &bitbucket.PipelineScheduleArgs{
//				Workspace:   pulumi.String("example"),
//				Repository:  pulumi.Any(bitbucket_repository.Test.Name),
//				CronPattern: pulumi.String("0 30 * * * ? *"),
//				Enabled:     pulumi.Bool(true),
//				Target: &bitbucket.PipelineScheduleTargetArgs{
//					RefName: pulumi.String("master"),
//					RefType: pulumi.String("branch"),
//					Selector: &bitbucket.PipelineScheduleTargetSelectorArgs{
//						Pattern: pulumi.String("staging"),
//					},
//				},
//			})
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
//
// ## Import
//
// Pipeline Schedules can be imported using their `workspace/repo-slug/uuid` ID, e.g.
//
// ```sh
//
//	$ pulumi import bitbucket:index/pipelineSchedule:PipelineSchedule schedule workspace/repo-slug/uuid
//
// ```
type PipelineSchedule struct {
	pulumi.CustomResourceState

	// The cron expression that the schedule applies.
	CronPattern pulumi.StringOutput `pulumi:"cronPattern"`
	// Whether the schedule is enabled.
	Enabled pulumi.BoolOutput `pulumi:"enabled"`
	// The Repository to create schedule in.
	Repository pulumi.StringOutput `pulumi:"repository"`
	// Schedule Target definition. See Target below.
	Target PipelineScheduleTargetOutput `pulumi:"target"`
	// The UUID identifying the schedule.
	Uuid pulumi.StringOutput `pulumi:"uuid"`
	// The Workspace where the repository resides.
	Workspace pulumi.StringOutput `pulumi:"workspace"`
}

// NewPipelineSchedule registers a new resource with the given unique name, arguments, and options.
func NewPipelineSchedule(ctx *pulumi.Context,
	name string, args *PipelineScheduleArgs, opts ...pulumi.ResourceOption) (*PipelineSchedule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CronPattern == nil {
		return nil, errors.New("invalid value for required argument 'CronPattern'")
	}
	if args.Enabled == nil {
		return nil, errors.New("invalid value for required argument 'Enabled'")
	}
	if args.Repository == nil {
		return nil, errors.New("invalid value for required argument 'Repository'")
	}
	if args.Target == nil {
		return nil, errors.New("invalid value for required argument 'Target'")
	}
	if args.Workspace == nil {
		return nil, errors.New("invalid value for required argument 'Workspace'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource PipelineSchedule
	err := ctx.RegisterResource("bitbucket:index/pipelineSchedule:PipelineSchedule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPipelineSchedule gets an existing PipelineSchedule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPipelineSchedule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PipelineScheduleState, opts ...pulumi.ResourceOption) (*PipelineSchedule, error) {
	var resource PipelineSchedule
	err := ctx.ReadResource("bitbucket:index/pipelineSchedule:PipelineSchedule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PipelineSchedule resources.
type pipelineScheduleState struct {
	// The cron expression that the schedule applies.
	CronPattern *string `pulumi:"cronPattern"`
	// Whether the schedule is enabled.
	Enabled *bool `pulumi:"enabled"`
	// The Repository to create schedule in.
	Repository *string `pulumi:"repository"`
	// Schedule Target definition. See Target below.
	Target *PipelineScheduleTarget `pulumi:"target"`
	// The UUID identifying the schedule.
	Uuid *string `pulumi:"uuid"`
	// The Workspace where the repository resides.
	Workspace *string `pulumi:"workspace"`
}

type PipelineScheduleState struct {
	// The cron expression that the schedule applies.
	CronPattern pulumi.StringPtrInput
	// Whether the schedule is enabled.
	Enabled pulumi.BoolPtrInput
	// The Repository to create schedule in.
	Repository pulumi.StringPtrInput
	// Schedule Target definition. See Target below.
	Target PipelineScheduleTargetPtrInput
	// The UUID identifying the schedule.
	Uuid pulumi.StringPtrInput
	// The Workspace where the repository resides.
	Workspace pulumi.StringPtrInput
}

func (PipelineScheduleState) ElementType() reflect.Type {
	return reflect.TypeOf((*pipelineScheduleState)(nil)).Elem()
}

type pipelineScheduleArgs struct {
	// The cron expression that the schedule applies.
	CronPattern string `pulumi:"cronPattern"`
	// Whether the schedule is enabled.
	Enabled bool `pulumi:"enabled"`
	// The Repository to create schedule in.
	Repository string `pulumi:"repository"`
	// Schedule Target definition. See Target below.
	Target PipelineScheduleTarget `pulumi:"target"`
	// The Workspace where the repository resides.
	Workspace string `pulumi:"workspace"`
}

// The set of arguments for constructing a PipelineSchedule resource.
type PipelineScheduleArgs struct {
	// The cron expression that the schedule applies.
	CronPattern pulumi.StringInput
	// Whether the schedule is enabled.
	Enabled pulumi.BoolInput
	// The Repository to create schedule in.
	Repository pulumi.StringInput
	// Schedule Target definition. See Target below.
	Target PipelineScheduleTargetInput
	// The Workspace where the repository resides.
	Workspace pulumi.StringInput
}

func (PipelineScheduleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*pipelineScheduleArgs)(nil)).Elem()
}

type PipelineScheduleInput interface {
	pulumi.Input

	ToPipelineScheduleOutput() PipelineScheduleOutput
	ToPipelineScheduleOutputWithContext(ctx context.Context) PipelineScheduleOutput
}

func (*PipelineSchedule) ElementType() reflect.Type {
	return reflect.TypeOf((**PipelineSchedule)(nil)).Elem()
}

func (i *PipelineSchedule) ToPipelineScheduleOutput() PipelineScheduleOutput {
	return i.ToPipelineScheduleOutputWithContext(context.Background())
}

func (i *PipelineSchedule) ToPipelineScheduleOutputWithContext(ctx context.Context) PipelineScheduleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineScheduleOutput)
}

// PipelineScheduleArrayInput is an input type that accepts PipelineScheduleArray and PipelineScheduleArrayOutput values.
// You can construct a concrete instance of `PipelineScheduleArrayInput` via:
//
//	PipelineScheduleArray{ PipelineScheduleArgs{...} }
type PipelineScheduleArrayInput interface {
	pulumi.Input

	ToPipelineScheduleArrayOutput() PipelineScheduleArrayOutput
	ToPipelineScheduleArrayOutputWithContext(context.Context) PipelineScheduleArrayOutput
}

type PipelineScheduleArray []PipelineScheduleInput

func (PipelineScheduleArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PipelineSchedule)(nil)).Elem()
}

func (i PipelineScheduleArray) ToPipelineScheduleArrayOutput() PipelineScheduleArrayOutput {
	return i.ToPipelineScheduleArrayOutputWithContext(context.Background())
}

func (i PipelineScheduleArray) ToPipelineScheduleArrayOutputWithContext(ctx context.Context) PipelineScheduleArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineScheduleArrayOutput)
}

// PipelineScheduleMapInput is an input type that accepts PipelineScheduleMap and PipelineScheduleMapOutput values.
// You can construct a concrete instance of `PipelineScheduleMapInput` via:
//
//	PipelineScheduleMap{ "key": PipelineScheduleArgs{...} }
type PipelineScheduleMapInput interface {
	pulumi.Input

	ToPipelineScheduleMapOutput() PipelineScheduleMapOutput
	ToPipelineScheduleMapOutputWithContext(context.Context) PipelineScheduleMapOutput
}

type PipelineScheduleMap map[string]PipelineScheduleInput

func (PipelineScheduleMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PipelineSchedule)(nil)).Elem()
}

func (i PipelineScheduleMap) ToPipelineScheduleMapOutput() PipelineScheduleMapOutput {
	return i.ToPipelineScheduleMapOutputWithContext(context.Background())
}

func (i PipelineScheduleMap) ToPipelineScheduleMapOutputWithContext(ctx context.Context) PipelineScheduleMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PipelineScheduleMapOutput)
}

type PipelineScheduleOutput struct{ *pulumi.OutputState }

func (PipelineScheduleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PipelineSchedule)(nil)).Elem()
}

func (o PipelineScheduleOutput) ToPipelineScheduleOutput() PipelineScheduleOutput {
	return o
}

func (o PipelineScheduleOutput) ToPipelineScheduleOutputWithContext(ctx context.Context) PipelineScheduleOutput {
	return o
}

// The cron expression that the schedule applies.
func (o PipelineScheduleOutput) CronPattern() pulumi.StringOutput {
	return o.ApplyT(func(v *PipelineSchedule) pulumi.StringOutput { return v.CronPattern }).(pulumi.StringOutput)
}

// Whether the schedule is enabled.
func (o PipelineScheduleOutput) Enabled() pulumi.BoolOutput {
	return o.ApplyT(func(v *PipelineSchedule) pulumi.BoolOutput { return v.Enabled }).(pulumi.BoolOutput)
}

// The Repository to create schedule in.
func (o PipelineScheduleOutput) Repository() pulumi.StringOutput {
	return o.ApplyT(func(v *PipelineSchedule) pulumi.StringOutput { return v.Repository }).(pulumi.StringOutput)
}

// Schedule Target definition. See Target below.
func (o PipelineScheduleOutput) Target() PipelineScheduleTargetOutput {
	return o.ApplyT(func(v *PipelineSchedule) PipelineScheduleTargetOutput { return v.Target }).(PipelineScheduleTargetOutput)
}

// The UUID identifying the schedule.
func (o PipelineScheduleOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v *PipelineSchedule) pulumi.StringOutput { return v.Uuid }).(pulumi.StringOutput)
}

// The Workspace where the repository resides.
func (o PipelineScheduleOutput) Workspace() pulumi.StringOutput {
	return o.ApplyT(func(v *PipelineSchedule) pulumi.StringOutput { return v.Workspace }).(pulumi.StringOutput)
}

type PipelineScheduleArrayOutput struct{ *pulumi.OutputState }

func (PipelineScheduleArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*PipelineSchedule)(nil)).Elem()
}

func (o PipelineScheduleArrayOutput) ToPipelineScheduleArrayOutput() PipelineScheduleArrayOutput {
	return o
}

func (o PipelineScheduleArrayOutput) ToPipelineScheduleArrayOutputWithContext(ctx context.Context) PipelineScheduleArrayOutput {
	return o
}

func (o PipelineScheduleArrayOutput) Index(i pulumi.IntInput) PipelineScheduleOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *PipelineSchedule {
		return vs[0].([]*PipelineSchedule)[vs[1].(int)]
	}).(PipelineScheduleOutput)
}

type PipelineScheduleMapOutput struct{ *pulumi.OutputState }

func (PipelineScheduleMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*PipelineSchedule)(nil)).Elem()
}

func (o PipelineScheduleMapOutput) ToPipelineScheduleMapOutput() PipelineScheduleMapOutput {
	return o
}

func (o PipelineScheduleMapOutput) ToPipelineScheduleMapOutputWithContext(ctx context.Context) PipelineScheduleMapOutput {
	return o
}

func (o PipelineScheduleMapOutput) MapIndex(k pulumi.StringInput) PipelineScheduleOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *PipelineSchedule {
		return vs[0].(map[string]*PipelineSchedule)[vs[1].(string)]
	}).(PipelineScheduleOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineScheduleInput)(nil)).Elem(), &PipelineSchedule{})
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineScheduleArrayInput)(nil)).Elem(), PipelineScheduleArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*PipelineScheduleMapInput)(nil)).Elem(), PipelineScheduleMap{})
	pulumi.RegisterOutputType(PipelineScheduleOutput{})
	pulumi.RegisterOutputType(PipelineScheduleArrayOutput{})
	pulumi.RegisterOutputType(PipelineScheduleMapOutput{})
}
