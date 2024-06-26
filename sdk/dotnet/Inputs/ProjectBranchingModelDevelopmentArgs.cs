// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Bitbucket.Inputs
{

    public sealed class ProjectBranchingModelDevelopmentArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Optional and only returned for a project's branching model. Indicates if the indicated branch exists on the project (`false`) or not (`true`). This is useful for determining a fallback to the mainbranch when a project is inheriting its project's branching model.
        /// </summary>
        [Input("branchDoesNotExist")]
        public Input<bool>? BranchDoesNotExist { get; set; }

        [Input("isValid")]
        public Input<bool>? IsValid { get; set; }

        /// <summary>
        /// The configured branch. It must be null when `use_mainbranch` is true. Otherwise it must be a non-empty value. It is possible for the configured branch to not exist (e.g. it was deleted after the settings are set).
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Indicates if the setting points at an explicit branch (`false`) or tracks the main branch (`true`). When `true` the name must be null or not provided. When `false` the name must contain a non-empty branch name.
        /// </summary>
        [Input("useMainbranch")]
        public Input<bool>? UseMainbranch { get; set; }

        public ProjectBranchingModelDevelopmentArgs()
        {
        }
        public static new ProjectBranchingModelDevelopmentArgs Empty => new ProjectBranchingModelDevelopmentArgs();
    }
}
