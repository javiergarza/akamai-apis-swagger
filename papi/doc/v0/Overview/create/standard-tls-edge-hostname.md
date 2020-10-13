---
title: "Standard TLS edge hostname"
slug: "standard-tls-edge-hostname"
hidden: false
createdAt: "2020-06-05T16:26:25.873Z"
updatedAt: "2020-06-05T20:11:09.886Z"
---
Use Standard TLS edge hostnames for HTTP-only traffic, or for HTTPS
traffic that doesn't need to be PCI compliant.  This variation on the
[Create a new edge hostname](#postedgehostnames) operation creates a
Standard TLS edge hostname:

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
            "productId": "Dynamic_Site_Del",
            "domainPrefix": "www.example.com",
            "domainSuffix": "edgesuite.net",
            "secureNetwork": "STANDARD_TLS",
            "ipVersionBehavior": "IPV4"
        }

1. Specify the `productId` to assign to the edge hostname.

1. Set the `domainPrefix` to the original hostname, for example
`www.example.com`.

1. Set the `domainSuffix` to `edgesuite.net`.

1. Set the `secureNetwork` to `STANDARD_TLS`.

1. Set the request's `ipVersionBehavior` to `IPV4`, `IPV6`, or
`IPV6_COMPLIANCE` to support both.

1. POST the object to
`/papi/v0/edgehostnames{?contractId,groupId}`.

1. Optionally GET the response object's `edgeHostnameLink` or the
`Location` header to poll the new edge hostname's deployment `status`.
This runs the [Get an edge hostname](#getedgehostname) operation.