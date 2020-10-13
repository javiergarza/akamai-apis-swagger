---
title: "Enhanced TLS edge hostname"
slug: "enhanced-tls-edge-hostname"
hidden: false
createdAt: "2020-06-05T16:27:37.050Z"
updatedAt: "2020-06-11T13:00:58.362Z"
---
Use Enhanced TLS edge hostnames for PCI-compliant HTTPS traffic. This option requires the ID of a TLS certificate deployed over the [Certificate Provisioning System API](https://developer.akamai.com/api/core_features/certificate_provisioning_system/v2.html).

This variation on the [Create a new edge hostname](#postedgehostnames) operation creates an Enhanced TLS edge hostname:

1. If you don't already have a `contractId` value, run the [List contracts](#getcontracts) operation and select one from the list.

1. If you don't already have a `groupId` value, run the [List groups](#getgroups) operation and select one from the list.

1. If you don't already have a `productId` value, run the [List products](#getproducts) operation and select the relevant one to enable the edge hostname.

1. Build an [EdgeHostname](#edgehostname) POST object such as this example:

        {
            "productId": "Rich_Media_Accel",
            "domainPrefix": "www.example.com",
            "domainSuffix": "edgekey.net",
            "secureNetwork": "ENHANCED_TLS",
            "ipVersionBehavior": "IPV4",
            "certEnrollmentId": "10277"
        }

1. Specify the `productId` to assign to the edge hostname.

1. Set the `domainPrefix` to the origin hostname, for example `www.example.com`.

1. Set the `domainSuffix` to `edgekey.net`.

1. Set `secureNetwork` to `ENHANCED_TLS`.

1. Sett the request's `ipVersionBehavior` to `IPV4`, `IPV6`, or `IPV6_COMPLIANCE` to support both.

1. If you don't already have a `certEnrollmentId` value:

    1. Run the CPS API's [List
    enrollments](https://developer.akamai.com/api/core_features/certificate_provisioning_system/v2.html#getenrollments)
    operation, and select the appropriate object from the
    `enrollments` array.

    1. Strip the leading path expression from the object's `location`
    member, and use that string value as the `certEnrollmentId`. For
    example, if the `location` is `"/cps-api/enrollments/10002"`, the
    `certEnrollmentId` is `"10002"`.

    Note that if the certificate you want doesn't already exist,
    you need to run the CPS API's
    [Create an enrollment](https://developer.akamai.com/api/core_features/certificate_provisioning_system/v2.html#postenrollments)
    operation. It takes several hours to fully deploy a new
    certificate.

1. POST the object to `/papi/v0/edgehostnames{?contractId,groupId}`.

1. Optionally GET the response object's `edgeHostnameLink` or the `Location` header to poll the new edge hostname's deployment `status`. This runs the [Get an edge hostname](#getedgehostname) operation.