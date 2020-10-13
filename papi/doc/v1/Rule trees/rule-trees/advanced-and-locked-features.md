---
title: "Advanced and locked features"
slug: "advanced-and-locked-features"
hidden: false
createdAt: "2020-06-05T17:07:19.782Z"
updatedAt: "2020-06-10T03:12:22.938Z"
---
In addition to its `name` and component `options`, special types of behavior and criteria objects may feature these additional members:

- A `uuid` string signifies an _advanced_ feature. Advanced behaviors and criteria are read-only, and can only be modified by Akamai representatives. They typically deploy metadata customized for you, whose functionality falls outside the predefined guidelines of what other read/write behaviors can do. Such metadata might also cause problems if executed outside of its intended context within the rule tree. Throughout the [PAPI Feature Catalog Reference](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html), advanced features are identified as _read-only_.

- If a `locked` boolean member is `true`, it indicates a behavior or criteria that your Akamai representative has _locked_ so that you can't modify it. You typically arrange with your representative to lock certain behaviors to protect sensitive data from erroneous changes. Any kind of behavior or criteria may be locked, including writable ones.

When modifying rule trees, you need to preserve the state of any `uuid` or `locked` members. You receive an error if you try to modify or delete either of these special types of feature. You can reposition regular features relative to these special ones, for example by inserting them within the same rule, but each rule's sequence of special features needs to remain unchanged.

Higher-level [Rule](#rule) objects may also indicate the presence of these special features:

- A `uuid` member present on a [Rule](#rule) object indicates that at least one of its component behaviors or criteria is advanced and read-only. You need to preserve this `uuid` as well when modifying the rule tree.

- A `criteriaLocked` member enabled on a criteria rule by your Akamai representative means that you may _not_ insert additional criteria objects within the sequence. This typically keeps complex logical tests from breaking. Preserve the state of `criteriaLocked` when modifying the rule tree.