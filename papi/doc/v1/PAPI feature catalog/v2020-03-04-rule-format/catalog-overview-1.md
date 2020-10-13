---
title: "Catalog overview"
slug: "catalog-overview-1"
hidden: false
createdAt: "2020-06-11T13:13:46.573Z"
updatedAt: "2020-06-15T20:16:54.378Z"
---
## Rule tree basics

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

## Read-only features [ro]

Some of the behaviors and criteria listed in this reference are
identified as _read-only_. These advanced features often directly
specify raw XML metadata that, if not configured properly, may cause
unexpected problems when executing on edge servers.  Do not edit these
behaviors when modifying rules trees, and do not alter their sequence
within each rule.  Contact your Akamai representative for assistance
if you need to modify one of these behaviors. See the following in the
main PAPI guide for more information:

- [Advanced and locked features](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#advancedfeatures),
for more details on read-only features.

- [Custom behaviors and overrides](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#custombehaviors),
for a way to apply advanced behaviors to many properties.

## Secure property requirements [sf]

For some of the behaviors detailed in this reference, you may need to
enable `is_secure` on the top-level default rule. This is necessary to
apply a shared certificate across all hostnames.

See
[Rule Trees](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#ruletrees)
for more guidance on the default rule's structure.

## Support for variables [vf]

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

## About rule formats [rf]

Akamai often modifies PAPI features, each time deploying a new
internal version of the feature. If you are using the Property Manager
interface in [Akamai Control Center](http://control.akamai.com), you
may be prompted to upgrade to new feature versions as they become
available. PAPI does not support this system of selective updates for
each feature. Instead, PAPI's rule objects are simply versioned as a
whole. These versions, which update infrequently, are known as _rule
formats_.

Rule formats are versioned by date, for example, `v2017-06-19`, or the
most recent rule format titled `latest`.  When you specify a feature
within a rule tree assigned with the `v2017-06-19` rule format, PAPI
uses the most recent version of the feature that rule format supports.
Only by updating to a newer rule format such as `v2018-02-27` do you
upgrade to new versions of various features, which often allow an
expanded set of options and enumerations.

PAPI users should assign the most recent dated rule format to freeze
the set of features. Otherwise if you assign the `latest` rule format,
features update automatically to their most recent version. This may
abruptly result in errors if JSON objects your rules specify no longer
comply with the most recent feature's set of requirements.  PAPI
provides a more stable path to update rule formats that fixes these
requirements for you.  For more information, see
[Update rules to a newer set of features](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#updaterf).

See
[Understanding rule formats](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#understandingruleformats)
for more information on PAPI's rule format versioning system.