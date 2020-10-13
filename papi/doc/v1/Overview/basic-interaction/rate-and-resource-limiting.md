---
title: "Rate and resource limiting"
slug: "rate-and-resource-limiting"
hidden: false
createdAt: "2020-06-05T16:14:09.235Z"
updatedAt: "2020-06-10T02:48:22.339Z"
---
PAPI imposes various limits on some of the resources you can deploy. In some cases, you may have the option to override these limits. Contact your Akamai representative for more information.

Various responses include HTTP headers that provide details on your current limits:

- Custom headers suffixed `*-Limit` report on the overall limit.

- Corresponding headers suffixed `*-Remaining` tell you how many items you have left to deploy.

- For rate-limited activations, an additional `*-Reset` header lets you know when the current `*-Remaining` value rises to the original `*-Limit` value.

PAPI imposes these limits:

| Limit | Default Value | Description |
| :--- | :--: | :--- |
| `X-Limit-Properties-Per-Contract-Limit` | 1000 | Maximum number of activated property configurations per contract. Most customers use a single contract. |
| `X-Limit-Edgehostnames-Per-Contract-Limit` | 1000 | Maximum number of edge hostnames per contract. Most customers use a single contract. |
| `X-Limit-Hosts-Per-Property-Limit` | 1000 | Maximum number of hostnames you can assign to a property configuration. |
| `X-Limit-Elements-Per-Property-Limit` | 1500 | Maximum number of separate matches and behaviors per rule tree configuration. |
| `X-Limit-Max-Nested-Rules-Limit` | 6 | Maximum number of nested child rules to apply conditional logic. See [Rule trees](#ruletrees) for details on how nested rules work. |
| `X-Limit-Clientip-Per-Property-Limit` | 300 | Maximum number of separate [Client IP](https://developer.akamai.com/api/core_features/property_manager/vlatest.html#clientip) matches per rule tree configuration. |
| `X-Limit-Max-Clientip-Per-Match-Limit` | 10 | Maximum number of separate IP addresses allowed within each [Client IP](https://developer.akamai.com/api/core_features/property_manager/vlatest.html#clientip) match. |
| `X-RateLimit-Activations-Limit` | 100 | Maximum number of PAPI configurations you can activate each day on either staging or production networks. |