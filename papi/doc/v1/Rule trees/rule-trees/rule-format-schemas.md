---
title: "Rule format schemas"
slug: "rule-format-schemas"
hidden: false
createdAt: "2020-06-05T17:18:20.816Z"
updatedAt: "2020-06-11T13:01:01.624Z"
---
PAPI provides [rule format schema](#getruleformatschema) objects that define the features you may enable under a product. This section shows how to interpret a rule format and use it to validate a rule tree or research available features.

The schema's relevant content is nested within the outer object's `definitions` member, which is empty in this example:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"$schema\": \"http://json-schema.org/draft-04/schema#\",\n    \"type\": \"object\",\n    \"properties\": {\n        \"rules\": {\n            \"$ref\": \"#/definitions/toprule\"\n        }\n    },\n    \"required\": [ \"rules\" ],\n    \"definitions\": {\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

The top level of the schema specifies only that the rule tree must feature a `rules` member, specified indirectly within a large `definitions` section that this example doesn't display. The `toprule` itself specifies an object, which needs a `name`. While these specify the object's basic structure, the `definition`'s `catalog` member contains available features, separately within the `behaviors` and `criteria` sub-trees. Each of those object's keys list supported features, and the values define their components.

> __Note__. The features specified in the rule format represent _all_ the behaviors and criteria the product supports, not necessarily those currently enabled for your account. Each product specifies a baseline set, with other more specialized features enabled with add-on _modules_, as discussed in [PAPI concepts](#papiconcepts). To determine the set of features currently available on your account, saving a property that specifies them returns an error that notifies you otherwise.

This example shows a typical behavior definition for [`caching`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#caching), along with its component options, some of whose data types are referenced elsewhere within the schema.

[block:code]
{
  "codes": [
    {
      "code": "\"caching\": {\n    \"type\": \"object\",\n    \"properties\": {\n        \"name\": {\n            \"enum\": [ \"caching\" ]\n        },\n        \"uuid\": {\n            \"type\": \"string\"\n        },\n        \"options\": {\n            \"type\": \"object\",\n            \"properties\": {\n                \"behavior\": {\n                    \"default\": \"max-age\",\n                    \"enum\": [ \"max-age\", \"no-store\", \"bypass-cache\", \"both\", \"cc\", \"expires\" ]\n                },\n                \"mustRevalidate\": {\n                    \"default\": \"off\",\n                    \"enum\": [ \"off\", \"on\" ]\n                },\n                \"ttl\": {\n                    \"$ref\": \"#/definitions/catalog/option_types/duration\"\n                },\n                \"defaultTtl\": {\n                    \"$ref\": \"#/definitions/catalog/option_types/duration\"\n                }\n            }\n        }\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

Understand the limitations of the rule format's available data. While each option's basic data type is specified, additional validation logic isn't necessarily available within the schema, and may be implemented as part of the API's back end. The rule format also doesn't represent dependencies among the options. For example, many behaviors feature a high-level `enabled` switch. When disabled, the API typically ignores any other specified option. When `enabled`, there may be other contextual dependencies among the options. The [PAPI Feature Catalog Reference](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html) references detail most of these dependencies.

Rule formats often specify only minimal validation criteria. For example, the rule format's `option_types` section describes custom data formats, such as this example representing a CP code object with a required `id` member:

[block:code]
{
  "codes": [
    {
      "code": "\"cpCode\": {\n    \"type\": \"object\",\n    \"properties\": {\n        \"id\": {\n            \"type\": \"number\"\n        }\n    },\n    \"required\": [ \"id\" ]\n},\n",
      "language": "json"
    }
  ]
}
[/block]

The rule format doesn't specify the `name` member that also typically appears within a `cpcode` object. It doesn't specify what happens if you omit the `name`, or supply other members unknown to the API's back end. The back end may behave slightly differently over time, even if you freeze the API's set of features.