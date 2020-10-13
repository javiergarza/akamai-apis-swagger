---
title: "clientCharacteristics"
slug: "clientcharacteristics"
hidden: false
createdAt: "2020-06-15T20:55:50.367Z"
updatedAt: "2020-06-15T20:55:50.367Z"
---
__Property Manager name__: [Client Characteristics](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0026)

Specifies characteristics of the client ecosystem. Akamai uses this information to optimize your metadata configuration, which may result in better end-user performance.

See also [`originCharacteristics`](#origincharacteristics) and various product-specific behaviors whose names are prefixed _contentCharacteristics_.

__Options__:

<div class="option" markdown="1" id="clientCharacteristics.country" >

- `country` (_enum string_): Specifies the client request's geographic region, or `UNKNOWN` to defer any optimizations based on geography. Possible global regions are `GLOBAL`, `GLOBAL_ASIA_CENTRIC`, `GLOBAL_EU_CENTRIC`, or `GLOBAL_US_CENTRIC`. More specific regions include `ASIA_PACIFIC`, `AUSTRALIA`, `EUROPE`, `GERMANY`, `INDIA`, `ITALY`, `JAPAN`, `NORDICS`, `NORTH_AMERICA`, `SOUTH_AMERICA`, `TAIWAN`, or `UNITED_KINGDOM`. Specify `OTHER` as a fallback value.

</div>

</div>

<div class="feature" data-feature="constructResponse" markdown="1">
