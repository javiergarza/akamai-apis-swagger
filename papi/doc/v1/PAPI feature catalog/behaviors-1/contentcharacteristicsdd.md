---
title: "contentCharacteristicsDD"
slug: "contentcharacteristicsdd"
hidden: false
createdAt: "2020-06-15T20:58:39.647Z"
updatedAt: "2020-06-15T20:58:39.647Z"
---
__Property Manager name__: [Content Characteristics](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0029)

Specifies characteristics of the delivered content. Akamai uses this information to optimize your metadata configuration, which may result in better origin offload and end-user performance.

Along with other behaviors whose names are prefixed _contentCharacteristics_, this behavior is customized for a specific product set.  Use PAPI's [List available behaviors](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html#listavailablebehaviors) operation to determine the set available to you. See also the related [`clientCharacteristics`](#clientcharacteristics) and [`originCharacteristics`](#origincharacteristics) behaviors.

__Options__:

<div class="option" markdown="1" id="contentCharacteristicsDD.objectSize" >

- `objectSize` (_enum string_): Optimize based on the size of the object retrieved from the origin, either `LESS_THAN_1MB`, `ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, or `UNKNOWN` to defer this optimization. Specify `OTHER` as a fallback value.

</div>

<div class="option" markdown="1" id="contentCharacteristicsDD.popularityDistribution" >

- `popularityDistribution` (_enum string_): Optimize based on the content's expected popularity, either `ALL_POPULAR` for a high volume of requests over a short period, `LONG_TAIL` for a low volume of requests over a long period, or `UNKNOWN` to defer this optimization. Specify `OTHER` as a fallback value.

</div>

<div class="option" markdown="1" id="contentCharacteristicsDD.catalogSize" >

- `catalogSize` (_enum string_): Optimize based on the total size of the content library delivered, either `SMALL` (under 100GB), `MEDIUM` (100GB-1TB), `LARGE` (1TB-100TB), `EXTRA_LARGE` (more than 100TB), or `UNKNOWN` to defer this optimization. Specify `OTHER` as a fallback value.

</div>

<div class="option" markdown="1" id="contentCharacteristicsDD.contentType" >

- `contentType` (_enum string_): Optimize based on the type of content, either `VIDEO`, `SOFTWARE`, `SOFTWARE_PATCH`, `GAME`, `GAME_PATCH`, `OTHER_DOWNLOADS`, or `UNKNOWN` to defer this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsDD.optimizeOption" >

- `optimizeOption` (_boolean_): When enabled, optimizes the delivery throughput and download times for large files.

</div>

</div>

<div class="feature" data-feature="contentCharacteristicsWsdLargeFile" markdown="1">
