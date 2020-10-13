---
title: "fileExtension"
slug: "fileextension"
hidden: false
createdAt: "2020-06-15T22:20:00.402Z"
updatedAt: "2020-06-15T22:20:00.402Z"
---
__Property Manager name__: [File Extension](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches the requested filename's extension, if present.

__Options__:

- `matchOperator` (_enum string_): Matches the contents of `values` if set to `IS_ONE_OF`, otherwise `IS_NOT_ONE_OF` reverses the match.

- `values` (_array of string values_): An array of file extension strings, with no leading dot characters, for example `png`, `jpg`, `jpeg`, and `gif`.

- `matchCaseSensitive` (_boolean_): When enabled, the match is case-sensitive.
