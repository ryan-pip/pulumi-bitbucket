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

// Provides a Bitbucket Repository Group Permission Resource.
//
// This allows you set explicit group permission for a repository.
//
// OAuth2 Scopes: `repository:admin`
//
// Note: can only be used when authenticating with Bitbucket Cloud using an _app password_. Authenticating via an OAuth flow gives a 403 error due to a [restriction in the Bitbucket Cloud API](https://developer.atlassian.com/cloud/bitbucket/rest/api-group-repositories/#api-repositories-workspace-repo-slug-permissions-config-groups-group-slug-put).
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
//			_, err := bitbucket.NewRepositoryGroupPermission(ctx, "example", &bitbucket.RepositoryGroupPermissionArgs{
//				Workspace:  pulumi.String("example"),
//				RepoSlug:   pulumi.Any(bitbucket_repository.Example.Name),
//				GroupSlug:  pulumi.Any(bitbucket_group.Example.Slug),
//				Permission: pulumi.String("read"),
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
// Repository Group Permissions can be imported using their `workspace:repo-slug:group-slug` ID, e.g.
//
// ```sh
//
//	$ pulumi import bitbucket:index/repositoryGroupPermission:RepositoryGroupPermission example workspace:repo-slug:group-slug
//
// ```
type RepositoryGroupPermission struct {
	pulumi.CustomResourceState

	// Slug of the requested group.
	GroupSlug pulumi.StringOutput `pulumi:"groupSlug"`
	// Permissions can be one of `read`, `write`, and `admin`.
	Permission pulumi.StringOutput `pulumi:"permission"`
	// The repository slug.
	RepoSlug pulumi.StringOutput `pulumi:"repoSlug"`
	// The workspace id.
	Workspace pulumi.StringOutput `pulumi:"workspace"`
}

// NewRepositoryGroupPermission registers a new resource with the given unique name, arguments, and options.
func NewRepositoryGroupPermission(ctx *pulumi.Context,
	name string, args *RepositoryGroupPermissionArgs, opts ...pulumi.ResourceOption) (*RepositoryGroupPermission, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.GroupSlug == nil {
		return nil, errors.New("invalid value for required argument 'GroupSlug'")
	}
	if args.Permission == nil {
		return nil, errors.New("invalid value for required argument 'Permission'")
	}
	if args.RepoSlug == nil {
		return nil, errors.New("invalid value for required argument 'RepoSlug'")
	}
	if args.Workspace == nil {
		return nil, errors.New("invalid value for required argument 'Workspace'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource RepositoryGroupPermission
	err := ctx.RegisterResource("bitbucket:index/repositoryGroupPermission:RepositoryGroupPermission", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRepositoryGroupPermission gets an existing RepositoryGroupPermission resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRepositoryGroupPermission(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RepositoryGroupPermissionState, opts ...pulumi.ResourceOption) (*RepositoryGroupPermission, error) {
	var resource RepositoryGroupPermission
	err := ctx.ReadResource("bitbucket:index/repositoryGroupPermission:RepositoryGroupPermission", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RepositoryGroupPermission resources.
type repositoryGroupPermissionState struct {
	// Slug of the requested group.
	GroupSlug *string `pulumi:"groupSlug"`
	// Permissions can be one of `read`, `write`, and `admin`.
	Permission *string `pulumi:"permission"`
	// The repository slug.
	RepoSlug *string `pulumi:"repoSlug"`
	// The workspace id.
	Workspace *string `pulumi:"workspace"`
}

type RepositoryGroupPermissionState struct {
	// Slug of the requested group.
	GroupSlug pulumi.StringPtrInput
	// Permissions can be one of `read`, `write`, and `admin`.
	Permission pulumi.StringPtrInput
	// The repository slug.
	RepoSlug pulumi.StringPtrInput
	// The workspace id.
	Workspace pulumi.StringPtrInput
}

func (RepositoryGroupPermissionState) ElementType() reflect.Type {
	return reflect.TypeOf((*repositoryGroupPermissionState)(nil)).Elem()
}

type repositoryGroupPermissionArgs struct {
	// Slug of the requested group.
	GroupSlug string `pulumi:"groupSlug"`
	// Permissions can be one of `read`, `write`, and `admin`.
	Permission string `pulumi:"permission"`
	// The repository slug.
	RepoSlug string `pulumi:"repoSlug"`
	// The workspace id.
	Workspace string `pulumi:"workspace"`
}

// The set of arguments for constructing a RepositoryGroupPermission resource.
type RepositoryGroupPermissionArgs struct {
	// Slug of the requested group.
	GroupSlug pulumi.StringInput
	// Permissions can be one of `read`, `write`, and `admin`.
	Permission pulumi.StringInput
	// The repository slug.
	RepoSlug pulumi.StringInput
	// The workspace id.
	Workspace pulumi.StringInput
}

func (RepositoryGroupPermissionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*repositoryGroupPermissionArgs)(nil)).Elem()
}

type RepositoryGroupPermissionInput interface {
	pulumi.Input

	ToRepositoryGroupPermissionOutput() RepositoryGroupPermissionOutput
	ToRepositoryGroupPermissionOutputWithContext(ctx context.Context) RepositoryGroupPermissionOutput
}

func (*RepositoryGroupPermission) ElementType() reflect.Type {
	return reflect.TypeOf((**RepositoryGroupPermission)(nil)).Elem()
}

func (i *RepositoryGroupPermission) ToRepositoryGroupPermissionOutput() RepositoryGroupPermissionOutput {
	return i.ToRepositoryGroupPermissionOutputWithContext(context.Background())
}

func (i *RepositoryGroupPermission) ToRepositoryGroupPermissionOutputWithContext(ctx context.Context) RepositoryGroupPermissionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RepositoryGroupPermissionOutput)
}

// RepositoryGroupPermissionArrayInput is an input type that accepts RepositoryGroupPermissionArray and RepositoryGroupPermissionArrayOutput values.
// You can construct a concrete instance of `RepositoryGroupPermissionArrayInput` via:
//
//	RepositoryGroupPermissionArray{ RepositoryGroupPermissionArgs{...} }
type RepositoryGroupPermissionArrayInput interface {
	pulumi.Input

	ToRepositoryGroupPermissionArrayOutput() RepositoryGroupPermissionArrayOutput
	ToRepositoryGroupPermissionArrayOutputWithContext(context.Context) RepositoryGroupPermissionArrayOutput
}

type RepositoryGroupPermissionArray []RepositoryGroupPermissionInput

func (RepositoryGroupPermissionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RepositoryGroupPermission)(nil)).Elem()
}

func (i RepositoryGroupPermissionArray) ToRepositoryGroupPermissionArrayOutput() RepositoryGroupPermissionArrayOutput {
	return i.ToRepositoryGroupPermissionArrayOutputWithContext(context.Background())
}

func (i RepositoryGroupPermissionArray) ToRepositoryGroupPermissionArrayOutputWithContext(ctx context.Context) RepositoryGroupPermissionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RepositoryGroupPermissionArrayOutput)
}

// RepositoryGroupPermissionMapInput is an input type that accepts RepositoryGroupPermissionMap and RepositoryGroupPermissionMapOutput values.
// You can construct a concrete instance of `RepositoryGroupPermissionMapInput` via:
//
//	RepositoryGroupPermissionMap{ "key": RepositoryGroupPermissionArgs{...} }
type RepositoryGroupPermissionMapInput interface {
	pulumi.Input

	ToRepositoryGroupPermissionMapOutput() RepositoryGroupPermissionMapOutput
	ToRepositoryGroupPermissionMapOutputWithContext(context.Context) RepositoryGroupPermissionMapOutput
}

type RepositoryGroupPermissionMap map[string]RepositoryGroupPermissionInput

func (RepositoryGroupPermissionMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RepositoryGroupPermission)(nil)).Elem()
}

func (i RepositoryGroupPermissionMap) ToRepositoryGroupPermissionMapOutput() RepositoryGroupPermissionMapOutput {
	return i.ToRepositoryGroupPermissionMapOutputWithContext(context.Background())
}

func (i RepositoryGroupPermissionMap) ToRepositoryGroupPermissionMapOutputWithContext(ctx context.Context) RepositoryGroupPermissionMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RepositoryGroupPermissionMapOutput)
}

type RepositoryGroupPermissionOutput struct{ *pulumi.OutputState }

func (RepositoryGroupPermissionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**RepositoryGroupPermission)(nil)).Elem()
}

func (o RepositoryGroupPermissionOutput) ToRepositoryGroupPermissionOutput() RepositoryGroupPermissionOutput {
	return o
}

func (o RepositoryGroupPermissionOutput) ToRepositoryGroupPermissionOutputWithContext(ctx context.Context) RepositoryGroupPermissionOutput {
	return o
}

// Slug of the requested group.
func (o RepositoryGroupPermissionOutput) GroupSlug() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryGroupPermission) pulumi.StringOutput { return v.GroupSlug }).(pulumi.StringOutput)
}

// Permissions can be one of `read`, `write`, and `admin`.
func (o RepositoryGroupPermissionOutput) Permission() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryGroupPermission) pulumi.StringOutput { return v.Permission }).(pulumi.StringOutput)
}

// The repository slug.
func (o RepositoryGroupPermissionOutput) RepoSlug() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryGroupPermission) pulumi.StringOutput { return v.RepoSlug }).(pulumi.StringOutput)
}

// The workspace id.
func (o RepositoryGroupPermissionOutput) Workspace() pulumi.StringOutput {
	return o.ApplyT(func(v *RepositoryGroupPermission) pulumi.StringOutput { return v.Workspace }).(pulumi.StringOutput)
}

type RepositoryGroupPermissionArrayOutput struct{ *pulumi.OutputState }

func (RepositoryGroupPermissionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*RepositoryGroupPermission)(nil)).Elem()
}

func (o RepositoryGroupPermissionArrayOutput) ToRepositoryGroupPermissionArrayOutput() RepositoryGroupPermissionArrayOutput {
	return o
}

func (o RepositoryGroupPermissionArrayOutput) ToRepositoryGroupPermissionArrayOutputWithContext(ctx context.Context) RepositoryGroupPermissionArrayOutput {
	return o
}

func (o RepositoryGroupPermissionArrayOutput) Index(i pulumi.IntInput) RepositoryGroupPermissionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *RepositoryGroupPermission {
		return vs[0].([]*RepositoryGroupPermission)[vs[1].(int)]
	}).(RepositoryGroupPermissionOutput)
}

type RepositoryGroupPermissionMapOutput struct{ *pulumi.OutputState }

func (RepositoryGroupPermissionMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*RepositoryGroupPermission)(nil)).Elem()
}

func (o RepositoryGroupPermissionMapOutput) ToRepositoryGroupPermissionMapOutput() RepositoryGroupPermissionMapOutput {
	return o
}

func (o RepositoryGroupPermissionMapOutput) ToRepositoryGroupPermissionMapOutputWithContext(ctx context.Context) RepositoryGroupPermissionMapOutput {
	return o
}

func (o RepositoryGroupPermissionMapOutput) MapIndex(k pulumi.StringInput) RepositoryGroupPermissionOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *RepositoryGroupPermission {
		return vs[0].(map[string]*RepositoryGroupPermission)[vs[1].(string)]
	}).(RepositoryGroupPermissionOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*RepositoryGroupPermissionInput)(nil)).Elem(), &RepositoryGroupPermission{})
	pulumi.RegisterInputType(reflect.TypeOf((*RepositoryGroupPermissionArrayInput)(nil)).Elem(), RepositoryGroupPermissionArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*RepositoryGroupPermissionMapInput)(nil)).Elem(), RepositoryGroupPermissionMap{})
	pulumi.RegisterOutputType(RepositoryGroupPermissionOutput{})
	pulumi.RegisterOutputType(RepositoryGroupPermissionArrayOutput{})
	pulumi.RegisterOutputType(RepositoryGroupPermissionMapOutput{})
}
