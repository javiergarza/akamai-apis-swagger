---
title: "contentDeliveryNetwork"
slug: "contentdeliverynetwork"
hidden: false
createdAt: "2020-06-15T22:18:42.222Z"
updatedAt: "2020-06-15T22:18:42.222Z"
---
__Property Manager name__: CDN Network

A [read-only criteria](#ro) that specifies the type of Akamai network handling the request.  Contact Akamai Professional Services for help configuring it.

__Options__:

- `matchOperator` (_enum string_): Matches the specified `network` if set to `IS`, otherwise `IS_NOT` reverses the match..

- `network` (_enum string_): Match requests served from either the `PRODUCTION` or `STAGING` network.
