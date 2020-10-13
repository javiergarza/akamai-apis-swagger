---
title: "The default rule"
slug: "the-default-rule"
hidden: false
createdAt: "2020-06-05T17:03:13.362Z"
updatedAt: "2020-06-10T03:12:22.886Z"
---
The JSON object for the API's [Rules](#propertyversionrulesgroup) interface features a top-level `rules` element that specifies a default rule object. As discussed in the [Errors](#errors) section, responses may also include top-level `warnings`, `errors`, and other [contextual members](#rule), hence the additional layer of data. In the interest of clarity, extraneous data members are removed from the JSON examples in this section.

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"rules\": {\n        \"name\": \"default\",\n        \"options\": {\n            \"is_secure\": false\n        }\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

The rule's `default` name is more than simply a default. The top-level rule _must_ be named that way.

The only nominally mandatory member when saving a rule is its `name`, so you don't have to pass in the `options` object, as in this example that displays default behavior. The [Create a new edge hostname](#postedgehostnames) operation shows how to specify hostnames as `secure`. When the property's `is_secure` is set to `true`, it means you want to apply a shared certificate for all hostnames, possibly supplementing hostname-specific certificates. With `is_secure` enabled within the rule tree, you may receive warnings about any non-`secure` hostnames to which the rule applies. Note that some behaviors may only be available within the rule when `is_secure` is `true`.