// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Bitbucket.Inputs
{

    public sealed class PipelineScheduleTargetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the reference.
        /// </summary>
        [Input("refName", required: true)]
        public Input<string> RefName { get; set; } = null!;

        /// <summary>
        /// The type of reference. Valid values are `branch` and `tag`.
        /// </summary>
        [Input("refType", required: true)]
        public Input<string> RefType { get; set; } = null!;

        /// <summary>
        /// Selector spec. See Selector below.
        /// </summary>
        [Input("selector", required: true)]
        public Input<Inputs.PipelineScheduleTargetSelectorArgs> Selector { get; set; } = null!;

        public PipelineScheduleTargetArgs()
        {
        }
        public static new PipelineScheduleTargetArgs Empty => new PipelineScheduleTargetArgs();
    }
}
