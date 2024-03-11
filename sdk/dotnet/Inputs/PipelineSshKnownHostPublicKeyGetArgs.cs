// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Bitbucket.Inputs
{

    public sealed class PipelineSshKnownHostPublicKeyGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The plain public key.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        /// <summary>
        /// The type of the public key. Valid values are `ssh-ed25519`, `ecdsa-sha2-nistp256`, `ssh-rsa`, and `ssh-dss`.
        /// </summary>
        [Input("keyType", required: true)]
        public Input<string> KeyType { get; set; } = null!;

        [Input("md5Fingerprint")]
        public Input<string>? Md5Fingerprint { get; set; }

        [Input("sha256Fingerprint")]
        public Input<string>? Sha256Fingerprint { get; set; }

        public PipelineSshKnownHostPublicKeyGetArgs()
        {
        }
        public static new PipelineSshKnownHostPublicKeyGetArgs Empty => new PipelineSshKnownHostPublicKeyGetArgs();
    }
}
