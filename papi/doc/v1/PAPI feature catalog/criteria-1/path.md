---
title: "path"
slug: "path"
hidden: false
createdAt: "2020-06-15T22:23:17.863Z"
updatedAt: "2020-06-15T22:23:17.863Z"
---
__Property Manager name__: [Path](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the URL's non-hostname path component.

__Options__:

- `matchOperator` (_enum string_): Matches the contents of `values` when set to `MATCHES_ONE_OF`, otherwise `DOES_NOT_MATCH_ONE_OF` reverses the match.

- `values` (_array of string values_): Matches the URL path, excluding leading hostname and trailing query parameters. The path is relative to the server root, for example `/blog`. The `value` accepts `*` or `?` wildcard characters, for example `/blog/*/2014`.

- `matchCaseSensitive` (_boolean_): When enabled, the match is case-sensitive.
