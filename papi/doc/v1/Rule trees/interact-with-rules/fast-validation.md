---
title: "Fast validation"
slug: "fast-validation"
hidden: false
createdAt: "2020-06-05T17:01:22.076Z"
updatedAt: "2020-06-10T03:12:22.287Z"
---
PAPI's most important function is to modify rule trees assigned to sets of hostnames, and to activate them on Akamai's networks of edge servers. As described in the [Rule Trees](#ruletrees) section, rule trees are potentially very large, complex objects that often require frequent, iterative optimizations.

Under PAPI's traditional development cycle, each time you modify and save a rule tree, you'd need to wait for a lengthy set of validation tests to complete, making an iterative development cycle more difficult. The current API release provides shortcuts to accelerate development. One option allows you to defer validation until you're ready:

- When running the [Update a rule tree](#putpropertyversionrules) operation, set the `validateRules` query parameter to `false`.

- When running the [Update a property's hostnames](#putpropertyversionhostnames) operation, set the `validateHostnames` query parameter to `false`.

Both the rule tree and the set of hostnames are part of the same property definition, for which there's a single validation process. The benefits of routinely deferring validation increases along with the size of the rule tree, and with the number of hostnames you assign it to. When you defer validation, the response object comes to you more quickly, and without its usual `errors` and `warnings` arrays described in the [JSON problems](#jsonproblems) section. Note that you'd still need to fix any `errors`, and to either fix or acknowledge any `warnings`. To get this information, you need to enable validation again before activating the property.

Instead of skipping validation when running the [Update a rule tree](#putpropertyversionrules) operation, you can also accelerate validation, or run the operation simply to gather errors rather than modify the rule tree. For both of these options, you need to set the `validateHostnames` query parameter to the default `true` value:

- Setting the `validateMode` query parameter to `FAST` performs a more superficial JSON syntax check. This focuses on the errors that are more likely during frequent iteration. It skips a lengthier set of execution tests on the converted XML metadata.

- Alternately, setting the `dryRun` query parameter to `true` performs the full validation check, but without saving the rule tree. The response provides any resulting `errors` and `warnings`, without committing changes to the rule tree. You can only specify `dryRun` with `validateMode` set to the default `FULL` validation.

Before [activating a revised rule tree](#postpropertyactivations), you need to fix any `errors` from a full validation. As part of the activation, you either set the `acknowledgeAllWarnings` flag or pass in an array of `acknowledgeWarnings` warning IDs. Activation is much faster if the property's set of hostnames doesn't change.

You may also have the option to quickly revert an activation:

- If you detect a problem with the rule tree within an hour of its activation, POST another activation with `useFastFallback` set to `true`. Within a few seconds, it disables the current activation and falls back to the previous version. Fallback may also occur automatically if the activated metadata fails various execution tests on edge servers. The fallback option isn't available if you've changed the set of property hostnames, or if this is the property's first activation. When [polling the activation's status](#getpropertyactivation), the `canFastFallback` flag indicates whether fallback is possible.

- If the fast fallback option isn't available as indicated by `"canFastFallback":false`, you need to separately activate the previous version of the rule tree known not to cause problems.

Contact your Akamai representative for guidance on expected latency, both to validate your property's rule tree and to activate it worldwide.