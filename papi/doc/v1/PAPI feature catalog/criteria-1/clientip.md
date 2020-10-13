---
title: "clientIp"
slug: "clientip"
hidden: false
createdAt: "2020-06-15T22:17:17.110Z"
updatedAt: "2020-06-15T22:17:17.110Z"
---
__Property Manager name__: [Client IP](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the IP number of the requesting client.

__Options__:

- `matchOperator` (_enum string_): Matches the contents of `values` if set to `IS_ONE_OF`, otherwise `IS_NOT_ONE_OF` reverses the match.

- `values` (_array of string values_): IP or CIDR block, for example: `71.92.0.0/14`.

- `useHeaders` (_boolean_): When connecting via a proxy server as determined by the `X-Forwarded-For` header, enabling this option matches the connecting client's IP address rather than the original end client specified in the header.
