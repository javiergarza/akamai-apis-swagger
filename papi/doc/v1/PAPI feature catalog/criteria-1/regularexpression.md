---
title: "regularExpression"
slug: "regularexpression"
hidden: false
createdAt: "2020-06-15T22:25:07.227Z"
updatedAt: "2020-06-15T22:25:07.227Z"
---
__Property Manager name__: [Regex](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches a regular expression against a string, especially to apply behaviors flexibly based on the contents of dynamic [variables](#vf).

__Options__:

- `matchString` (_string; allows [variables](#vf)_): The string to match, typically the contents of a dynamic variable.

- `regex` (_string_): The regular expression (PCRE) to match against the string.

- `caseSensitive` (_boolean_): When disabled, the regular expression match is case-insensitive.
