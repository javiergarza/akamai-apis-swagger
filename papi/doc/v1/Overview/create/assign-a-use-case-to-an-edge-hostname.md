---
title: "Assign a use case"
slug: "assign-a-use-case-to-an-edge-hostname"
hidden: false
createdAt: "2020-06-05T16:33:19.542Z"
updatedAt: "2020-06-10T03:14:36.627Z"
---
When creating a new edge hostname, you can configure it to serve different types of traffic that align to important use cases. Akamai provides various preset use case scenarios that affect how the edge hostname is configured once deployed.  By default, edge hostnames are configured to deploy the same type of traffic for any Akamai product. Assigning a use case allows you to optimize different types of traffic. For example, if the edge hostname is deployed for the Download Delivery product, you can distinguish high-priority `FOREGROUND` downloads from others that download in the `BACKGROUND`.

To assign a use case to a new edge hostname:

1. If you don't already have a `contractId` value, run the [List contracts](#getcontracts) operation to choose one.

1. If you don't already have a `productId` value, run the [List products](#getproducts) operation. Different products may offer different sets of use cases.

1. Use the `productId` values to run the [List use cases](#getusecases) operation.

1. If the response includes a `useCases` array, choose the [UseCase](#84c668bb) object that best matches your traffic's intended deployment profile. If a `useCases` array isn't present, it means this product doesn't support any use cases, and you can stop this procedure.

1. Store the object's `useCase` ID and `type`.

1. Store one of the provided `options` as an `option` value.

1. Follow the procedure to create a [Standard TLS](#standardtls), [Enhanced TLS](#enhancedtls), or [Shared Certificate](#sharedcert) edge hostname. The [EdgeHostname](#67914a1f) POST object needs to be arranged differently for each type of edge hostname.

1. Before POSTing the new edge hostname, add a `useCases` array that includes an object that specifies each data member you copied from the [UseCase](#84c668bb) response object. The object needs to specify a `useCase`, `type`, and `option` value. For example:

        {
            "productId": "prd_Dynamic_Site_Del",
            "domainPrefix": "www.example.com",
            "domainSuffix": "edgesuite.net",
            "secureNetwork": "STANDARD_TLS",
            "ipVersionBehavior": "IPV4",
            "useCases": [
                {
                    "useCase": "Download_Mode",
                    "option": "BACKGROUND",
                    "type": "GLOBAL"
                }
            ]
        }

1. Once you have added the use case to the [EdgeHostname](#67914a1f) request object, POST it to `/papi/v0/edgehostnames{?contractId,groupId}`.

1. Optionally GET the response object's `edgeHostnameLink` or the `Location` header to poll the new edge hostname's deployment `status`. This runs the [Get an edge hostname](#getedgehostname) operation.