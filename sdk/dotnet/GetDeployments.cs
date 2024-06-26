// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Bitbucket
{
    public static class GetDeployments
    {
        /// <summary>
        /// Provides a way to fetch data on Deployments.
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
        ///     var example = Bitbucket.GetDeployments.Invoke(new()
        ///     {
        ///         Repository = "example",
        ///         Workspace = "example",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetDeploymentsResult> InvokeAsync(GetDeploymentsArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDeploymentsResult>("bitbucket:index/getDeployments:getDeployments", args ?? new GetDeploymentsArgs(), options.WithDefaults());

        /// <summary>
        /// Provides a way to fetch data on Deployments.
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
        ///     var example = Bitbucket.GetDeployments.Invoke(new()
        ///     {
        ///         Repository = "example",
        ///         Workspace = "example",
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetDeploymentsResult> Invoke(GetDeploymentsInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDeploymentsResult>("bitbucket:index/getDeployments:getDeployments", args ?? new GetDeploymentsInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDeploymentsArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The repository name.
        /// </summary>
        [Input("repository", required: true)]
        public string Repository { get; set; } = null!;

        /// <summary>
        /// The workspace name.
        /// </summary>
        [Input("workspace", required: true)]
        public string Workspace { get; set; } = null!;

        public GetDeploymentsArgs()
        {
        }
        public static new GetDeploymentsArgs Empty => new GetDeploymentsArgs();
    }

    public sealed class GetDeploymentsInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The repository name.
        /// </summary>
        [Input("repository", required: true)]
        public Input<string> Repository { get; set; } = null!;

        /// <summary>
        /// The workspace name.
        /// </summary>
        [Input("workspace", required: true)]
        public Input<string> Workspace { get; set; } = null!;

        public GetDeploymentsInvokeArgs()
        {
        }
        public static new GetDeploymentsInvokeArgs Empty => new GetDeploymentsInvokeArgs();
    }


    [OutputType]
    public sealed class GetDeploymentsResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Names of deployments for a repository.
        /// </summary>
        public readonly ImmutableArray<string> Names;
        public readonly string Repository;
        /// <summary>
        /// UUIDs of deployments for a repository.
        /// </summary>
        public readonly ImmutableArray<string> Uuids;
        public readonly string Workspace;

        [OutputConstructor]
        private GetDeploymentsResult(
            string id,

            ImmutableArray<string> names,

            string repository,

            ImmutableArray<string> uuids,

            string workspace)
        {
            Id = id;
            Names = names;
            Repository = repository;
            Uuids = uuids;
            Workspace = workspace;
        }
    }
}
