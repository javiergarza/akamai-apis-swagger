---
title: "v2020-03-04 rule format"
slug: "v2020-03-04-rule-format"
hidden: false
createdAt: "2020-06-11T13:10:23.122Z"
updatedAt: "2020-06-15T20:17:24.528Z"
---
The
[Property Manager API](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html)
(PAPI) allows you to programmatically configure your web content over
the Akamai edge network. By assigning _rules_ to a set of hostnames,
you modify how your origin content responds to your user's requests to
Akamai edge servers, often by configuring Akamai products, or by
applying your own customizations.

Along with the main
[API reference](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html)
that shows you how to use PAPI as a whole, this supplementary API
reference provides additional details on all of the _features_ that
you can include within the set of rules.  Features consist of either
_behaviors_ that specify actions affecting how your web content
responds, or match _criteria_ that determine the conditions under
which those actions execute.  The [Behaviors](#behaviors) and
[Criteria](#criteria) sections below provide details on the full set
of available features. The remainder of this section summarizes how
rule trees work, and provides pointers to the main API reference for
more information.
[block:callout]
{
  "type": "info",
  "body": "This reference provides details on the set of features\nsupported by the `latest` rule format version.  For the most stable\ndeployment, use the most recent dated rule format version.  See\n[About Rule Formats](#rf) for guidance."
}
[/block]