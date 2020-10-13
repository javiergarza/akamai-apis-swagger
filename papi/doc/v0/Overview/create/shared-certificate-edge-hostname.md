---
title: "Shared Certificate edge hostname"
slug: "shared-certificate-edge-hostname"
hidden: false
createdAt: "2020-06-05T16:32:11.185Z"
updatedAt: "2020-06-05T16:34:37.044Z"
---
This alternative to [Standard TLS](#standardtls) allows you to apply a
single `*.akamaized.net` shared certificate to HTTP-only or non-PCI
compliant HTTPS traffic. In this case, the property hostname needs to
match the edge hostname, both using the `akamaized.net` domain.  For
the wildcard to work, you can specify a single subdomain such as
`mywebsite.akamaized.net`, but no further subdomains such as
`my.website.akamaized.net`.

This variation on the [Create a new edge hostname](#postedgehostnames)
operation creates a shared certificate edge hostname:

1. If you don't already have a `contractId` value, run the [List
contracts](#getcontracts) operation and select one from the list.

1. If you don't already have a `groupId` value, run the [List
groups](#getgroups) operation and select one from the list.

1. If you don't already have a `productId` value, run the [List
products](#getproducts) operation and select the relevant one to
enable the edge hostname.

1. Build an [EdgeHostname](#edgehostname) POST object such as this
example:

        {
            "productId": "Adaptive_Media_Delivery",
            "domainPrefix": "www-example_com",
            "domainSuffix": "akamaized.net",
            "secureNetwork": "SHARED_CERT",
            "ipVersionBehavior": "IPV4"
        }

1. Specify the `productId` to assign to the edge hostname.

1. Set the `domainPrefix` to the additional subdomain segment, such as
`www-example_com`. Note that the value can include dashes and
underscores, but no dots that would result in nested subdomains.

1. Set the `domainSuffix` to `akamaized.net`.

1. Set `secureNetwork` to `SHARED_CERT`.

1. Set the request's `ipVersionBehavior` to `IPV4`, `IPV6`, or
`IPV6_COMPLIANCE` to support both.

1. POST the object to
`/papi/v0/edgehostnames{?contractId,groupId}`.

1. Optionally GET the response object's `edgeHostnameLink` or the
`Location` header to poll the new edge hostname's deployment `status`.
This runs the [Get an edge hostname](#getedgehostname) operation.