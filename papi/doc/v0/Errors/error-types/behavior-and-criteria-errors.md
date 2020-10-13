---
title: "Behavior and criteria errors"
slug: "behavior-and-criteria-errors"
hidden: false
createdAt: "2020-06-05T21:18:58.367Z"
updatedAt: "2020-06-05T21:18:58.367Z"
---
These general errors relate to how you implement behaviors and
criteria. They may be listed within [Rule](#rule) objects,
and may prevent you from activating the property version:

| Type | Description |
| :--- | :--- |
| `compatible_behaviors` | Rules include incompatible behaviors. |
| `condition_no_prompt_upgrade` | You must upgrade to a new version of a criteria. |
| `deprecated` | The behavior has been deprecated. |
| `deprecated_delete` | The behavior has been removed. |
| `deprecated_readonly` | The behavior has been deprecated. |
| `duplicate_feature` | Two behaviors of the same type are inappropriately placed within the same rule. |
| `feature_no_prompt_upgrade` | A new version of the behavior is available, requiring an upgrade. |
| `feature_upgrade_required` | The property needs to be upgraded to replace a deprecated behavior. |
| `feature_upgrade_required_readonly` | The property needs to be upgraded to replace a deprecated behavior, but this version can't be edited. Create a new version if necessary. |
| `feature_upgrade_required_viewonly` | A new version of the behavior is available, requiring an upgrade. |
| `generic_behavior_issue.kss_not_object` | A new version of the behavior is available that may require a different set of options. |
| `generic_behavior_issue.netstorage_group_not_available` | A specified NetStorage account isn't assigned to this property's group. |
| `generic_behavior_issue.origin_missing_auxlist_subtitle` | Your auxiliary certificate list specifies trusted items not reflected in what your [`origin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#origin) behavior specifies. Confirm they're accurate, and contact your account team if there's a problem. |
| `generic_behavior_issue.origin_missing_trust_ca_certs_from_underride` | Your auxiliary certificate list specifies trusted items not reflected in what your [`origin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#origin) behavior specifies. Confirm they're accurate, and contact your account team if there's a problem. |
| `generic_behavior_issue.origin_missing_trust_certs_from_underride` | Your auxiliary certificate list specifies trusted items not reflected in what your [`origin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#origin) behavior specifies. Confirm they're accurate, and contact your account team if there's a problem. |
| `generic_behavior_issue.origin_valid_cn_missing_values_from_underride_error` | The [`origin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#origin) behavior's `customValidCnValues` option is missing CN/SAN match values from the auxiliary certificates list, so an ordinarily trusted certificate may not be trusted, and may result in a service outage. |
| `generic_behavior_issue.origin_valid_cn_missing_values_from_underride_warning` | Confirm the [`origin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#origin) behavior's `customValidCnValues` option includes all CN/SAN values from the auxiliary certificates list. |
| `generic_behavior_issue.origin_valid_cn_wildcard` | Values in the [`origin`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#origin) behavior's `customValidCnValues` option may contain a star (`*`) character, but it's interpreted literally. |
| `incompatible_condition` | There's an incompatibility with a specific criteria within the same rule. |
| `incompatible_features` | There's an incompatibility with a specific behavior within the same rule. |
| `incompatible_stages.multiple` | There's an incompatibility with a set of match criteria. |
| `incompatible_stages.none` | There's an incompatibility with a criteria in a parent rule. |
| `incompatible_stages.one` | There's an incompatibility with a criteria that appears in the same rule. |
| `required_feature` | The `default` rule requires a behavior for the property to work. |
| `too_many_instances` | There are more instances of the specified behavior than allowed within a property. |
| `unknown_condition` | The criteria isn't supported, and you need to remove it before activating your property. |
| `unknown_feature` | The behavior isn't supported, and you need to remove it before activating your property. |
| `unknown_feature_attribute` | The behavior or criteria specifies an unknown option. |