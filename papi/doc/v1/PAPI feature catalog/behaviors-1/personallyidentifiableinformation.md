---
title: "personallyIdentifiableInformation"
slug: "personallyidentifiableinformation"
hidden: false
createdAt: "2020-06-15T21:44:50.247Z"
updatedAt: "2020-06-15T21:44:50.247Z"
---
__Property Manager name__: [Personally Identifiable Information](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0061)

Marks content covered by the current rule as sensitive _personally identifiable information_ that needs to be treated as secure and private. That includes anything involving personal information: name, social security number, date and place of birth, mother's maiden name, biometric data, or any other data linked to an individual. If you attempt to save a property with such a rule that also caches or logs sensitive content, the added behavior results in a validation error.

> __WARNING__: This feature only identifies some vulnerabilities. For
example, it does not prevent you from including secure information in
a query string or writing it to an origin folder. It also can't tell
whether the SSL protocol is in effect.

__Options__:

<div class="option" markdown="1" id="personallyIdentifiableInformation.enabled" >

- `enabled` (_boolean_): When enabled, marks content as personally identifiable information (PII).

</div>

</div>

<div class="feature" data-feature="phasedRelease" markdown="1">
