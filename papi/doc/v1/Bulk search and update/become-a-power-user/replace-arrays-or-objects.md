---
title: "Replace arrays or objects"
slug: "replace-arrays-or-objects"
hidden: false
createdAt: "2020-06-05T18:14:37.782Z"
updatedAt: "2020-06-11T13:00:52.628Z"
---
The bulk patches discussed above change simple scalar string, numeric, or boolean values, but you can also use JSON Patch to replace more complex object and array data structures. This advanced technique offers you great power and flexibility when modifying all your rule tree configurations.

Suppose you specify a [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html) origin to offload multimedia content, and you want to bulk-change the storage location and the CP code to track the traffic.  Unlike most other PAPI behavior options, the [`origin`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#origin) behavior's `netStorage` option specifies a complex nested object value:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"name\" : \"origin\",\n    \"options\" : {\n        \"originType\" : \"NET_STORAGE\",\n        \"httpsPort\" : 443,\n        \"netStorage\" : {\n            \"cpCode\" : 12345,\n            \"downloadDomainName\" : \"legacy.download.example.akamai.com\",\n            \"name\" : \"Legacy Storage Area\"\n        }\n    }\n}\n",
      "language": "json"
    }
  ]
}
[/block]

In this case, you could run three different bulk searches for each member of the `netStorage` object, and replace each in separate batches, but that would be very inefficient:

```
$..behaviors[?(@.name == 'origin'].options.netStorage.name
$..behaviors[?(@.name == 'origin'].options.netStorage.cpCode
$..behaviors[?(@.name == 'origin'].options.netStorage.downloadDomainName
```

You could also reconfigure a single set of bulk patch operations to `replace` all three `cpCode`, `downloadDomainName`, and `name` values separately.

As a much easier alternative, simply match the entire `netStorage` object:

```
$..behaviors[?(@.name == 'origin'].options.netStorage
```

Specify a replacement `value` that contains the entire object for the alternate NetStorage origin. This patch performs all the necessary changes at once:

[block:code]
{
  "codes": [
    {
      "code": "\"patches\": [\n    {\n        \"op\": \"replace\",\n        \"path\": \"/rules/behaviors/0/options/netStorage\",\n        \"value\": {\n            \"cpCode\": 54321,\n            \"downloadDomainName\": \"new.download.example.akamai.com\",\n            \"name\": \"Alternate Storage Area\"\n        }\n    }\n]\n",
      "language": "json"
    }
  ]
}
[/block]

You can use the same technique to replace arrays.  As a simple example, suppose you're already using a [`fileExtension`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#fileextension) criteria to respond to `.jpg` and `.gif` file extensions, and you want to add `.png` to the set.  The criteria specifies an array of `values`:

[block:code]
{
  "codes": [
    {
      "code": "\"criteria\": [\n    {\n        \"name\": \"fileExtension\",\n        \"options\": {\n            \"matchCaseSensitive\": true,\n            \"matchOperator\": \"IS_ONE_OF\",\n            \"values\": [\n                \"jpg\",\n                \"gif\"\n            ]\n        }\n    }\n]\n",
      "language": "json"
    }
  ]
}
[/block]

As detailed in the next section, you can `add` new values to the array.  But you can also replace the entire array with the full set of values you want.

This search matches the `values` of any `fileExtension` criteria that already specifies `jpg` as a value:

```
$..criteria[?(@.name == 'fileExtension'].options[?('jpg' in @.values)].values
```

You can follow up by patching in as a replacement `value` the entire array of file extensions you want to match:

[block:code]
{
  "codes": [
    {
      "code": "\"patches\": [\n    {\n        \"op\": \"replace\",\n        \"path\": \"/rules/children/0/criteria/1/options/values\",\n        \"value\": [\n            \"png\",\n            \"jpg\",\n            \"gif\"\n        ]\n    }\n]\n",
      "language": "json"
    }
  ]
}
[/block]