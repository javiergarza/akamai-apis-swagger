---
title: "Rule tree warnings"
slug: "rule-tree-warnings"
hidden: false
createdAt: "2020-06-05T21:09:06.147Z"
updatedAt: "2020-06-10T03:12:18.121Z"
---
The API may release a wide range of validation errors based on the content of rule trees, many of which are detailed in subsequent sections. A few unusual error scenarios are unique to PAPI:

- As discussed in the Resources section, you can [freeze the API](doc:freeze-a-rule-trees-feature-set) to use a specific set of behavior and criteria versions. If instead you specify the rule format that uses the `latest` versions, behaviors and criteria silently update, and may produce errors if their validation requirements change. Other validation errors may remain even when properly updating from one rule format version to another.

- As discussed in the [Advanced and locked features](doc:advanced-and-locked-features) section, some behaviors and criteria are locked and _read-only_, and can only be modified with assistance from Akamai Professional Services. You get an error if you try to modify or move them elsewhere within the rule tree.

- As discussed in the [Rule Trees](doc:rule-trees) section and detailed in the [PAPI Feature Catalog Reference](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html), some options may be required depending on the values of others. It's much easier to accidentally omit necessary values in the API than in the Control Center interface.

- Some errors may reference [Schema](#schemasgroup) objects, which you can examine to determine each product's support for behaviors and criteria. They also list the full set of options for each, along with their expected data types. However, schemas don't represent dependencies among options.

Aside from errors, PAPI more often returns a set of `warnings` after checking your chosen set of behaviors and criteria for identifiable logical inconsistencies. Here is a typical warning, whose `errorLocation` is a URL fragment that can be interpreted as a [JSON Pointer expression](https://tools.ietf.org/html/rfc6901) to help you locate the problem within the JSON tree you submitted:

[block:code]
{
  "codes": [
    {
      "code": "\"warnings\": [\n    {\n        \"type\": \"https://problems.luna.akamaiapis.net/papi/v0/validation/need_feature\",\n        \"errorLocation\": \"#/rules/behaviors/5\",\n        \"detail\": \"`Tiered Distribution` only applies to cacheable\n              content, but caching was never turned on.\"\n    }\n]\n",
      "language": "json"
    }
  ]
}
[/block]

Behaviors such as [`tieredDistribution`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#tiereddistribution) and [`prefreshCache`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#prefreshcache) can only operate on cached content on edge servers, so the warning identifies when the [`caching`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#caching) behavior isn't enabled. As another example, the [`cacheKeyIgnoreCase`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#cachekeyignorecase) behavior allows requests for files and query parameters with mixed upper- and lower-case letters to resolve to the same cache key. If you pair that behavior with a criteria that doesn't also specify a case-insensitive match, the warning alerts you not to apply different behaviors to the same cached object based on random variations in case among incoming requests.

These warnings often identify obvious logical problems, such as exclusive sets of criteria when `criteriaMustSatisfy` is set to `all`, or nested criteria that can never execute because they're logically exclusive with their ancestor rules' criteria. However, as in all programming environments, no validation mechanism can identify all potential bugs, so you need to carefully step through the code. You can also request `text/xml` rather than `application/json` from the [Property versions](#propertyversionsgroup) interface if you'd rather look at how a version's combined set of rules and hostnames translate to the Akamai metadata that's ultimately distributed to edge servers. Contact your Akamai Professional Services representative if you need help understanding the metadata syntax.

[block:callout]
{
  "type": "warning",
  "body": "As in the Property Manager Control Center application, the API requires you to acknowledge each warning before you activate a property. Pay careful attention to any warnings before you activate a property version, or your site can experience serious problems."
}
[/block]