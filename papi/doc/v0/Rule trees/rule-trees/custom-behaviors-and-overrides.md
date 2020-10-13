---
title: "Custom behaviors and overrides"
slug: "custom-behaviors-and-overrides"
hidden: false
createdAt: "2020-06-05T17:08:42.970Z"
updatedAt: "2020-06-05T17:10:51.248Z"
---
The main problem with the [_advanced_ features](#advancedfeatures)
described above is that
they need to be customized separately for each property in which they
appear. To address this issue, PAPI's alternative _custom features_
are defined outside the rule tree. You can reference these common
objects from within many different rule trees.

Suppose you have an `advanced` behavior whose `xml` does something
useful:
[block:code]
{
  "codes": [
    {
      "code": "{\n  \"name\": \"advanced\",\n  \"uuid\": \"6c192451-f35f-4a8d-ad70-0e8fec521d99\",\n  \"options\": {\n    \"description\": \"Setting custom download receipt. Uses PMUSER_LOG variable.\",\n    \"xml\": \"<reporting:edge-logging.send-receipt name=\\\"DLR\\\"><hostname>logs.customer.com</hostname><url>/dlr</url><allow-cacheh>off</allow-cacheh><status>on</status><port>443</port><format>stuff=%(PMUSER_LOG)&amp;time=%t&amp;url=%u</format><method>POST</method></reporting:edge-logging.send-receipt>\"\n  }\n}\n",
      "language": "json"
    }
  ]
}
[/block]
To apply it to many properties, contact your Akamai representative to
configure the XML as a custom behavior. Once ready, you run the
[List custom behaviors](#getcustombehaviors) operation, choose the
appropriate custom behavior, and store its `behaviorId` value:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"accountId\": \"act_1-1TJZFB\",\n    \"customBehaviors\": {\n        \"items\": [\n            {\n                \"behaviorId\": \"cbe_12345\",\n                \"name\": \"DLR\",\n                \"displayName\": \"Custom Download Receipt\",\n                \"description\": \"Setting custom download receipt. Uses PMUSER_LOG variable.\",\n                \"status\": \"ACTIVE\",\n                \"xml\": \"<reporting:edge-logging.send-receipt name=\\\"DLR\\\"><hostname>logs.customer.com</hostname><url>/dlr</url><allow-cacheh>off</allow-cacheh><status>on</status><port>443</port><format>stuff=%(PMUSER_LOG)&amp;time=%t&amp;url=%u</format><method>POST</method></reporting:edge-logging.send-receipt>\",\n                \"updatedDate\": \"2017-04-24T12:34:56Z\",\n                \"updatedByUser\": \"jsikkela\"\n            }\n        ]\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]
You can then insert a
[`customBehavior`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#custombehavior)
to reference the common metadata from within any rule tree, with no
need to preserve a `uuid` value when exchanging the rule:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"name\": \"customBehavior\",\n    \"options\": {\n        \"behaviorId\": \"cbe_12345\",\n        \"name\": \"mdc\"\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]
Custom overrides work much the same way as custom behaviors, but are
meant to execute last in the rule tree, typically to restore some
state that the rule tree may have modified along the way. Your Akamai
representative creates a custom override on your behalf, which you
then access with the
[List custom overrides](#getcustomoverrides)
operation. After choosing an `overrideId` from the list, you insert it
into a `customOverride` region directly on the outer
[Rule](#rule) object:
[block:code]
{
  "codes": [
    {
      "code": "{\n    \"rules\": {\n        \"name\": \"default\",\n        \"options\": {\n            \"is_secure\": false\n        }\n    },\n    \"customOverride\": {\n        \"overrideId\": \"cbo_12345\",\n        \"name\": \"mdc\"\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]