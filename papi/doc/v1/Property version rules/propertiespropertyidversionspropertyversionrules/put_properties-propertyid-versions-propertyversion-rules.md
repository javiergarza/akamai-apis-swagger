---
title: "Update a rule tree"
slug: "put_properties-propertyid-versions-propertyversion-rules"
excerpt: "To write a rule tree to a property version, make a PUT request\nto the same resource as the GET request that reads it, passing\nin the rule object in the body of the request. See the\n[Rule Trees](doc:rule-trees)\nsection for details on the rule tree's structure. Use this\noperation also to\n[freeze a set of rules](doc:freeze-a-rule-trees-feature-set)\nto a rule format version to ensure no change in a deployed\nactivation's behavior. Set the `validateRules` query parameter\nto `false` to bypass a set of validation tests that may\nsignificantly slow this operation's execution time. See\n[Fast validation and activation](doc:fast-validation)\nfor guidance on when to defer validation. See\n[JSON problems](doc:json-problem-responses)\nfor information on how validation data is embedded within the\nresponse object."
hidden: false
createdAt: "2020-06-05T13:10:51.784Z"
updatedAt: "2020-06-08T20:21:02.236Z"
---
