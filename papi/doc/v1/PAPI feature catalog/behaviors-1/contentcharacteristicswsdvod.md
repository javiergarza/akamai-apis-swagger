---
title: "contentCharacteristicsWsdVod"
slug: "contentcharacteristicswsdvod"
hidden: false
createdAt: "2020-06-15T21:01:42.113Z"
updatedAt: "2020-06-15T21:01:42.113Z"
---
__Property Manager name__: [Content Characteristics - Streaming Video On-demand](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5009)

Specifies characteristics of the delivered content, specifically targeted to delivering on-demand video. Akamai uses this information to optimize your metadata configuration, which may result in better origin offload and end-user performance.

Along with other behaviors whose names are prefixed _contentCharacteristics_, this behavior is customized for a specific product set.  Use PAPI's [List available behaviors](https://learn.akamai.com/en-us/api/core_features/adaptive_acceleration/v1.html#listavailablebehaviors) operation to determine the set available to you. See also the related [`clientCharacteristics`](#clientcharacteristics) and [`originCharacteristics`](#origincharacteristics) behaviors.

__Options__:

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.catalogSize" >

- `catalogSize` (_enum string_): Optimize based on the total size of the content library delivered, either `SMALL` (under 100GB), `MEDIUM` (100GB-1TB), `LARGE` (1TB-100TB), `EXTRA_LARGE` (more than 100TB), or `UNKNOWN` to defer this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.contentType" >

- `contentType` (_enum string_): Optimize based on the quality of media content, either `SD` (standard definition), `HD` (high definition), `ULTRA_HD`, `OTHER` for more than one level of quality, or `UNKNOWN` to defer this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.popularityDistribution" >

- `popularityDistribution` (_enum string_): Optimize based on the content's expected popularity, either `ALL_POPULAR` for a high volume of requests over a short period, `LONG_TAIL` for a low volume of requests over a long period, or `UNKNOWN` to defer this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.hls" >

- `hls` (_boolean_): Enable delivery of HLS media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentDurationHLS" >

- `segmentDurationHLS` (_enum string_): With the `hls` option enabled, specifies the duration of individual segments, either `SEGMENT_DURATION_2S`, `SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`, or `SEGMENT_DURATION_10S`.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentSizeHLS" >

- `segmentSizeHLS` (_enum string_): With the `hls` option enabled, specifies the size of the media object retrieved from the origin, either: `LESS_THAN_1MB`, `ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER` for sizes that straddle these ranges, or `UNKNOWN` to defer this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.hds" >

- `hds` (_boolean_): Enable delivery of HDS media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentDurationHDS" >

- `segmentDurationHDS` (_enum string_): With the `hds` option enabled, specifies the duration of individual fragments, either `SEGMENT_DURATION_2S`, `SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`, or `SEGMENT_DURATION_10S`.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentSizeHDS" >

- `segmentSizeHDS` (_enum string_): With the `hds` option enabled, specifies the size of the media object retrieved from the origin, either: `LESS_THAN_1MB`, `ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER` for sizes that straddle these ranges, or `UNKNOWN` to defer this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.dash" >

- `dash` (_boolean_): Enable delivery of DASH media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentDurationDASH" >

- `segmentDurationDASH` (_enum string_): With the `dash` option enabled, specifies the duration of individual segments, either `SEGMENT_DURATION_2S`, `SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`, or `SEGMENT_DURATION_10S`.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentSizeDASH" >

- `segmentSizeDASH` (_enum string_): With the `dash` option enabled, specifies the size of the media object retrieved from the origin, either: `LESS_THAN_1MB`, `ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER` for sizes that straddle these ranges, or `UNKNOWN` to defer this optimization.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.smooth" >

- `smooth` (_boolean_): Enable delivery of Smooth media.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentDurationSmooth" >

- `segmentDurationSmooth` (_enum string_): With the `smooth` option enabled, specifies the duration of individual fragments, either `SEGMENT_DURATION_2S`, `SEGMENT_DURATION_4S`, `SEGMENT_DURATION_6S`, `SEGMENT_DURATION_8S`, or `SEGMENT_DURATION_10S`.

</div>

<div class="option" markdown="1" id="contentCharacteristicsWsdVod.segmentSizeSmooth" >

- `segmentSizeSmooth` (_enum string_): With the `smooth` option enabled, specifies the size of the media object retrieved from the origin, either: `LESS_THAN_1MB`, `ONE_MB_TO_TEN_MB`, `TEN_MB_TO_100_MB`, `GREATER_THAN_100MB`, `OTHER` for sizes that straddle these ranges, or `UNKNOWN` to defer this optimization.

</div>

</div>

<div class="feature" data-feature="contentTargetingProtection" markdown="1">
