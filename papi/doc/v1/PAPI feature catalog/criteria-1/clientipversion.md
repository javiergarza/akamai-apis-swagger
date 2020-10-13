---
title: "clientIpVersion"
slug: "clientipversion"
hidden: false
createdAt: "2020-06-15T22:17:34.715Z"
updatedAt: "2020-06-15T22:17:34.715Z"
---
__Property Manager name__: [Client IP Version](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the version of the IP protocol used by the requesting client.

__Options__:

- `value` (_enum string_): The IP version of the client request, either `IPV4` or `IPV6`.

- `useXForwardedFor` (_boolean_): When connecting via a proxy server as determined by the `X-Forwarded-For` header, enabling this option matches the connecting client's IP address rather than the original end client specified in the header.
