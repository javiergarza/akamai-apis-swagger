---
title: "Make conditional changes"
slug: "make-conditional-changes"
hidden: false
createdAt: "2020-06-05T18:20:37.347Z"
updatedAt: "2020-06-10T03:12:14.143Z"
---
As detailed in the sections above, you can incorporate conditional tests into your initial JSONPath expression. But in many cases you can offload that conditional logic to execute as part of the patch.

For example, you can use this simple expression to match all [`origin`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#origin) behaviors' `originCertificate` option values, regardless of whether the certificate string is empty:

```
$..behaviors[?(@.name == 'origin')].options.originCertificate
```

To test for empty values, place an initial `test` patch before the patch that executes the `replace` operation. This example tests to make sure the matched value is blank, then assigns a certificate only if that condition is met:

[block:code]
{
  "codes": [
    {
      "code": "{\n  \"patchPropertyVersions\": [\n    {\n      \"propertyId\": \"prp_123456\",\n      \"propertyVersion\": 4,\n      \"patches\": [\n        {\n          \"op\": \"test\",\n          \"value\": \"\",\n          \"path\": \"/rules/behaviors/0/options/originCertificate\"\n        },\n        {\n          \"op\": \"replace\",\n          \"value\": \"-----BEGIN CERTIFICATE-----\\nMIIFH ... b+kIw==\\n-----END CERTIFICATE-----\\n\",\n          \"path\": \"/rules/behaviors/0/options/originCertificate\"\n        }\n      ]\n    }\n  ]\n}\n",
      "language": "json"
    }
  ]
}
[/block]

When including `test` operations within patches, as long as the `path` expression is a valid JSON Pointer location, the bulk update succeeds regardless of whether the `replace` operation executes.