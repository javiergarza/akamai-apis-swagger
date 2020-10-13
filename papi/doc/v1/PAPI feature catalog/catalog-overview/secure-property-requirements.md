---
title: "Secure property requirements"
slug: "secure-property-requirements"
hidden: false
createdAt: "2020-06-15T22:33:50.746Z"
updatedAt: "2020-06-15T22:33:50.746Z"
---
For some of the behaviors detailed in this reference, you may need to
enable `is_secure` on the top-level default rule. This is necessary to
apply a shared certificate across all hostnames.

See
[Rule Trees](https://learn.akamai.com/en-us/api/core_features/property_manager/v1.html#ruletrees)
for more guidance on the default rule's structure.