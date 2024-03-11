// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Bitbucket
{
    public static class GetIpRanges
    {
        /// <summary>
        /// Provides a way to fetch IP Ranges for whitelisting.
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
        ///     var example = Bitbucket.GetIpRanges.Invoke();
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetIpRangesResult> InvokeAsync(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetIpRangesResult>("bitbucket:index/getIpRanges:getIpRanges", InvokeArgs.Empty, options.WithDefaults());

        /// <summary>
        /// Provides a way to fetch IP Ranges for whitelisting.
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
        ///     var example = Bitbucket.GetIpRanges.Invoke();
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetIpRangesResult> Invoke(InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetIpRangesResult>("bitbucket:index/getIpRanges:getIpRanges", InvokeArgs.Empty, options.WithDefaults());
    }


    [OutputType]
    public sealed class GetIpRangesResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// A Set of IP Ranges. See Ranges below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetIpRangesRangeResult> Ranges;

        [OutputConstructor]
        private GetIpRangesResult(
            string id,

            ImmutableArray<Outputs.GetIpRangesRangeResult> ranges)
        {
            Id = id;
            Ranges = ranges;
        }
    }
}