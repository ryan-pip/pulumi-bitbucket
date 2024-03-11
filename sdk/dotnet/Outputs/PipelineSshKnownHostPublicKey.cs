// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Bitbucket.Outputs
{

    [OutputType]
    public sealed class PipelineSshKnownHostPublicKey
    {
        /// <summary>
        /// The plain public key.
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// The type of the public key. Valid values are `ssh-ed25519`, `ecdsa-sha2-nistp256`, `ssh-rsa`, and `ssh-dss`.
        /// </summary>
        public readonly string KeyType;
        public readonly string? Md5Fingerprint;
        public readonly string? Sha256Fingerprint;

        [OutputConstructor]
        private PipelineSshKnownHostPublicKey(
            string key,

            string keyType,

            string? md5Fingerprint,

            string? sha256Fingerprint)
        {
            Key = key;
            KeyType = keyType;
            Md5Fingerprint = md5Fingerprint;
            Sha256Fingerprint = sha256Fingerprint;
        }
    }
}