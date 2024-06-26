// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Bitbucket
{
    public static class GetHookTypes
    {
        /// <summary>
        /// Provides a way to fetch data of hook types.
        /// 
        /// OAuth2 Scopes: `none`
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Bitbucket = Pulumi.Bitbucket;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Bitbucket.GetHookTypes.Invoke(new()
        ///     {
        ///         SubjectType = "workspace",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetHookTypesResult> InvokeAsync(GetHookTypesArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetHookTypesResult>("bitbucket:index/getHookTypes:getHookTypes", args ?? new GetHookTypesArgs(), options.WithDefaults());

        /// <summary>
        /// Provides a way to fetch data of hook types.
        /// 
        /// OAuth2 Scopes: `none`
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Bitbucket = Pulumi.Bitbucket;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Bitbucket.GetHookTypes.Invoke(new()
        ///     {
        ///         SubjectType = "workspace",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetHookTypesResult> Invoke(GetHookTypesInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetHookTypesResult>("bitbucket:index/getHookTypes:getHookTypes", args ?? new GetHookTypesInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetHookTypesArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// A resource or subject type. Valid values are `workspace`, `user`, `repository`, `team`.
        /// </summary>
        [Input("subjectType", required: true)]
        public string SubjectType { get; set; } = null!;

        public GetHookTypesArgs()
        {
        }
        public static new GetHookTypesArgs Empty => new GetHookTypesArgs();
    }

    public sealed class GetHookTypesInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// A resource or subject type. Valid values are `workspace`, `user`, `repository`, `team`.
        /// </summary>
        [Input("subjectType", required: true)]
        public Input<string> SubjectType { get; set; } = null!;

        public GetHookTypesInvokeArgs()
        {
        }
        public static new GetHookTypesInvokeArgs Empty => new GetHookTypesInvokeArgs();
    }


    [OutputType]
    public sealed class GetHookTypesResult
    {
        /// <summary>
        /// A Set of Hook Event Types. See Hook Types below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetHookTypesHookTypeResult> HookTypes;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string SubjectType;

        [OutputConstructor]
        private GetHookTypesResult(
            ImmutableArray<Outputs.GetHookTypesHookTypeResult> hookTypes,

            string id,

            string subjectType)
        {
            HookTypes = hookTypes;
            Id = id;
            SubjectType = subjectType;
        }
    }
}
