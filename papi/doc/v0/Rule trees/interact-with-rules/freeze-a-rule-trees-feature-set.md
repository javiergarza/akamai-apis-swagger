---
title: "Freeze a rule tree's feature set"
slug: "freeze-a-rule-trees-feature-set"
hidden: false
createdAt: "2020-06-05T16:55:40.489Z"
updatedAt: "2020-06-05T16:55:40.489Z"
---
This section describes a specific use for the
[Update a rule tree](#putpropertyversionrules)
operation: to assign a specific rule format's feature set to a rule
tree. See also
[Freeze a rule tree's feature set](#freezerf) to increment the
versioned set of rule format features that are assigned to a rule
tree.

Rule trees are best deployed by assigning them a rule format that
specifies a fixed, frozen set of features that are guaranteed not to
change unexpectedly over time and cause errors. New properties' rule
trees are assigned whatever rule format you specify as a default
[client setting](#getclientsettings), or else the most recent
dated rule format version available. To confirm your rule tree is
already frozen, and freeze it if necessary:

1. Run [Get a rule tree](#getpropertyversionrules) and store the URL
you use to get it.

1. If the rule tree's top-level `ruleFormat` member is a dated
version, the rule tree is already frozen. Continue to freeze it only
if it's `latest`.

1. Run [List rule formats](#getruleformats) and store the most recent
dated rule format version string.

1. Build a custom MIME type string using this template,
`application/vnd.akamai.papirules.vYYYY-MM-DD+json`, where
`vYYYY-MM-DD` is the variable rule format version string.

1. PUT the rule tree object to the same URL you used to get it, adding
the custom MIME type to the request as a `Content-Type` header.

See also [Get a rule tree](#getpropertyversionrules) for steps to
update a rule tree to a more recent rule format. If the set of
features you include in your rule tree doesn't conform to the
associated [rule format schema](#getruleformatschema), the response
includes errors that may prevent you from
[activating the property](#postpropertyactivations).