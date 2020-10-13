---
title: "Support for variables"
slug: "support-for-variables"
hidden: false
createdAt: "2020-06-15T22:34:22.338Z"
updatedAt: "2020-06-15T22:34:22.338Z"
---
Many of the feature options detailed in this reference support
_variables_.  Along with read-only system variables, you can declare
your own set of dynamic variable strings at the top of the rule tree,
inject them in various features' option values, use the
[`setVariable`](#setvariable) behavior to modify them along the way
within the rule tree, and specify [`matchVariable`](#matchvariable)
criteria to execute conditional rules.

For more details, see the
[Variables](https://developer.akamai.com/api/core_features/property_manager/v1.html#variables)
section of the main PAPI reference.