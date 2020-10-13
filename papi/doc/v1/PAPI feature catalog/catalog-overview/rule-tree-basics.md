---
title: "Rule tree basics"
slug: "rule-tree-basics"
hidden: false
createdAt: "2020-06-15T22:32:24.780Z"
updatedAt: "2020-06-15T22:32:45.401Z"
---
PAPI's
[Rule Trees](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#ruletrees)
section offers guidance on how rules are arranged as a tree structure,
allowing you to program your web content.  To summarize, each set of
rules requires these two behaviors in the top-level _default rule_:

- [`origin`](#origin), which specifies where to get the content from.

- [`cpCode`](#cpcode), which tracks each edge request for the purpose
of reporting and billing.

Each rule specifies a set of behaviors. You may add a set of criteria
to conditionally execute behaviors in any nested child rules. You can
nest these rules five layers deep within the rule tree.

Each feature is a small JSON object that specifies its own set of
_options_. Options are often cross-dependent in various ways. For
example, you only specify your origin's `hostname` option if the
`originType` enumeration is set to a `CUSTOMER`-defined origin.
Such cross-dependencies are detailed throughout this reference.

The overall set of features available to you is determined by the
product and set of modules associated with the property under your Akamai
contract.  You can get that information by running either of these
PAPI operations:

- [List Available Behaviors](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#getavailablebehaviors)
- [List Available Criteria](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#getavailablebehaviors)

When you activate a property, Property Manager translates the entire
rule tree and the property's set of hostnames to _metadata_, an XML
format that executes on Akamai's edge network.