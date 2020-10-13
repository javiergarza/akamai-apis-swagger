---
title: "ID prefixes"
slug: "id-prefixes"
hidden: false
createdAt: "2020-06-05T16:10:04.642Z"
updatedAt: "2020-06-10T03:12:20.006Z"
---
By default, response data features various ID values with three-letter prefixes to help distinguish their function:

- `aid_` for `assetId`
- `act_` for `accountId`
- `atv_` for `activationId`
- `cpc_` for `cpcodeId`
- `ctr_` for `contractId`
- `ehn_` for `edgeHostnameId`
- `grp_` for `groupId`
- `msg_` for `messageId`
- `prd_` for `productId`
- `prp_` for `propertyId`

While these prefixes may help when exchanging data within PAPI, other Akamai APIs that share the same data don't use this convention. There are two ways to strip them out of data:

- Run [Update client settings](#putclientsettings) to set `"usePrefixes":false` as the default for all requests. This solution is persistent for each API client.

- You can temporarily override the client's default setting by including a `PAPI-Use-Prefixes` boolean header with each request. So if the client's settings are `"usePrefixes":true`, passing in a `PAPI-Use-Prefixes: false` header removes the values.

Both of these options determine whether ID prefixes appear in response data. However, you can always specify any of these IDs as input parameters or JSON data with or without the prefixes.