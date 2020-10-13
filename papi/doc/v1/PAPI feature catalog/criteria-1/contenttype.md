---
title: "contentType"
slug: "contenttype"
hidden: false
createdAt: "2020-06-15T22:19:01.838Z"
updatedAt: "2020-06-15T22:19:01.838Z"
---
__Property Manager name__: [Content Type](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the HTTP response header's `Content-Type`.

__Options__:

- `matchOperator` (_enum string_): Matches any `Content-Type` among specified `values` when set to `IS_ONE_OF`, otherwise `IS_NOT_ONE_OF` reverses the match.

- `values` (_array of string values_): `Content-Type` response header value, for example `text/html`.

- `matchWildcard` (_boolean_): When enabled, allows `*` and `?` wildcard matches among the `values`, so that specifying `text/*` matches both `text/html` and `text/css`.

- `matchCaseSensitive` (_boolean_): When enabled, the match is case-sensitive for all `values`.
