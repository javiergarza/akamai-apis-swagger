---
title: "Launch a search"
slug: "launch-a-search"
hidden: false
createdAt: "2020-06-05T17:47:39.649Z"
updatedAt: "2020-06-10T03:19:56.649Z"
---
To launch the search, POST the [BulkSearch](#bulksearch) object to this URL:

```
POST /papi/v0/bulk/rules-search-requests
```

Add optional `contractId` or `groupId` parameters if you want to narrow down the set of results:

```
POST /papi/v0/bulk/rules-search-requests?contractId=1-1TJZFW&groupId=15166
```

The response's `Location` header, or the response JSON's `bulkSearchLink` member, both provide a navigable link to call the next operation.  Store this URL path value before proceeding to the next step:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"bulkSearchLink\": \"/papi/v0/bulk/rules-search-requests/737\"\n}",
      "language": "json"
    }
  ]
}
[/block]

For full details on the POST operation, see [Bulk search a set of properties](#postbulksearches).

[block:callout]
{
  "type": "info",
  "body": "If you provision an ordinary Akamai API token, search results apply to a single account.  Review [Get started](#getstarted) for a way to provision your API token to search properties across all your accounts."
}
[/block]