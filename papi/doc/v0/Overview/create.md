---
title: "Create edge hostnames"
slug: "create"
hidden: false
createdAt: "2020-06-05T16:22:03.913Z"
updatedAt: "2020-06-05T16:22:24.288Z"
---
As summarized in [PAPI concepts](#papiconcepts), edge hostnames
provide the DNS-based mechanism that maps each user request from the
originally requested hostname over to the optimal Akamai edge server.
You use PAPI to create edge hostnames that correspond to origin
hostnames under your control, then
[assign them](#putpropertyversionhostnames)
to properties.
Edge hostnames add extra segments as suffixes, making them slightly
longer than the original hostnames on which they're based.

You can create three different types of Akamai edge hostname,
depending on the level of security you need for your traffic.  Some
types need to be enabled on your Akamai contract. Each requires a
different procedure to form request data for the [Create a new edge
hostname](#postedgehostnames) operation:

- __Standard TLS__.  Use Standard TLS edge hostnames for HTTP-only
traffic, or for HTTPS traffic that doesn't need to be PCI compliant.
Standard TLS edge hostnames use the `edgesuite.net` domain suffix, so
that an original hostname of `www.example.com` results in an edge
hostname of `www.example.com.edgesuite.net`.
    See [Create a Standard TLS edge hostname](#standardtls).

- __Enhanced TLS__.  Use Enhanced TLS edge hostnames for PCI-compliant
HTTPS traffic.  This option requires the ID for a TLS certificate
deployed over the
[Certificate Provisioning System API](https://developer.akamai.com/api/core_features/certificate_provisioning_system/v2.html) (CPS).
Enhanced TLS edge hostnames use the `edgekey.net` domain suffix, so
that an original hostname of `www.example.com` results in an edge
hostname of `www.example.com.edgekey.net`.
Support for Enhanced TLS needs to be included in your contract.
    See [Create an Enhanced TLS edge hostname](#enhancedtls).

- __Shared Certificate__. This alternative to Standard TLS allows you
to apply an existing `*.akamaized.net` shared certificate to HTTP-only
or non-PCI compliant HTTPS traffic. In this case, the property
hostname needs to match the edge hostname, both using the
`akamaized.net` domain.  For the wildcard to work, you can specify a
single subdomain such as `mywebsite.akamaized.net`, but no further
subdomains such as `my.website.akamaized.net`.
Support for a shared certificate needs to be included in your contract.
    See [Create a Shared Certificate edge hostname](#sharedcert).

For more information, see
[Create edge hostnames using PAPI]({{base.url}}/{{page.language}}/learn_akamai/getting_started_with_akamai_developers/core_features/create_edgehostnames.html).

No matter what type of edge hostname you create, you may have the
option to assign a use case to optimize the type of traffic deployed
under the product. For details, see
[Assign a use case to an edge hostname](#assignausecase).