---
title: "Update rules to a newer set of features"
slug: "update-rules-to-a-newer-set-of-features"
hidden: false
createdAt: "2020-06-05T16:54:01.744Z"
updatedAt: "2020-06-05T16:54:01.744Z"
---
This section describes a specific use for the
[Get a rule tree](#getpropertyversionrules) operation described above:
to increment the versioned set of rule format features that are
assigned to a rule tree. See also
[Freeze a rule tree's feature set](#freezerf)
to assign a specific rule format.

Use this procedure to update from one rule format to another more
recent version, incrementing the assigned set of features. This also
modifies the rule tree to implement most required syntax changes, such
as changes to option names and enum values. You can't use this
approach to assign an older rule format. In this procedure, the
initial GET operation specifies a MIME type that converts the rule
tree, after which you PUT the converted object to write it back.

1. [List rule formats](#getruleformats) and store the more recent
rule format version string to which you want to update the rule tree.

1. Build a custom MIME type string using this template,
`application/vnd.akamai.papirules.vYYYY-MM-DD+json`, where
`vYYYY-MM-DD` is the variable rule format version string.

1. GET the rule tree as described above, adding an `Accept` header
that specifies the custom MIME type.

1. Confirm the response object's top-level `ruleFormat` reflects the
desired version.

1. PUT the converted rule tree to the same URL you got it from, adding
a `Content-Type` header that specifies the same custom MIME type.

This represents the formal update path to increment versions of
deployed features. Do _not_ assign a rule format of `latest`, as that
doesn't modify your rule tree to smoothly upgrade to any emerging
changes to features. The `latest` rule format is instead likely to
produce unexpected errors over time.

Updating to a more recent rule format modifies the rule tree to
accommodate renamed options, renamed enumeration values, and two-state
enums retyped as boolean. Other values may not be able to convert,
such as string numerics retyped as actual numerics, or if an updated
behavior features a new required option or different validation
criteria. If this occurs, the PUT response's rule tree object includes
errors that help you refine the updated rule tree, as detailed in the
[Errors](#errors) section.