---
title: "variableError"
slug: "variableerror"
hidden: false
createdAt: "2020-06-15T22:30:52.701Z"
updatedAt: "2020-06-15T22:30:52.701Z"
---
__Property Manager name__: [Variable Error](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches any runtime errors that occur on edge servers based on the configuration of a [`setVariable`](#setvariable) behavior. See [Support for variables](#vf) section for more information on this feature.

__Options__:

- `result` (_boolean_): When enabled, matches errors for the specified set of `variableNames`, otherwise matches errors from variables outside that set.

- `variableNames` (_string_): The name of the variable whose error triggers the match, or a space- or comma-delimited list of more than one variable name. Note that if you define a variable named `VAR`, the name in this field must appear with its added prefix as `PMUSER_VAR`. When such a variable is inserted into other fields, it appears with an additional namespace as `{{user.PMUSER_VAR}}`. See the [`setVariable`](#setvariable) for details on variable names.
