---
title: "Insert a variable"
slug: "insert-a-variable"
hidden: false
createdAt: "2020-06-05T17:20:51.390Z"
updatedAt: "2020-06-12T14:53:41.332Z"
---
Throughout the [PAPI Feature Catalog Reference](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html), any option fields that allow you to inject variable text are marked _allows variables_. Within any of those option's string values, you invoke variable names within pairs of `{{` ... `}}` delimiters. This example of a [`redirectPlus`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#redirectplus) behavior option invokes the original request's filename and concatenates it after a static string:
[block:code]
{
  "codes": [
    {
      "code": "\"destination\": \"/fixed/path/to/{{builtin.AK_FILENAME}}\"",
      "language": "json"
    }
  ]
}
[/block]
Note that, to accommodate the injection of variable strings, some options that reference conceptually numeric data are implemented instead as string types.

When inserting variables into text, you refer to them within a common namespace, in this case `builtin` for read-only system variables, followed by the unique variable name that's ultimately distributed in the XML metadata. The `{{builtin.AK_FILENAME}}` variable inserted above translates to `%(AK_FILENAME)` in XML metadata.