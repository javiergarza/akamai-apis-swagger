---
title: "manifestPersonalization"
slug: "manifestpersonalization"
hidden: false
createdAt: "2020-06-15T21:34:29.800Z"
updatedAt: "2020-06-15T21:34:29.800Z"
---
__Property Manager name__: [Manifest Personalization](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5002)

Allows customers who use the Adaptive Media Delivery product to enhance content based on the capabilities of each end user's device.  This behavior configures a _manifest_ for both HLS Live and on-demand streaming. For more information, see the [Adaptive Media Delivery Implementation Guide](https://learn.akamai.com/en-us/webhelp/adaptive-media-delivery/adaptive-media-delivery-implementation-guide/).

__Options__:

<div class="option" markdown="1" id="manifestPersonalization.enabled" >

- `enabled` (_boolean_): Enables the Manifest Personalization feature.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsEnabled" >

- `hlsEnabled` (_boolean_): When enabled, allows you to customize the HLS master manifest that's sent to the requesting client.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsMode" >

- `hlsMode` (_enum string_): With `hlsEnabled` on, specify either the default `BEST_PRACTICE` mode, or a `CUSTOM` manifest.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsPreferredBitrate" >

- `hlsPreferredBitrate` (_string_): With `hlsMode` set to `CUSTOM`, sets the preferred bit rate in Kbps. This causes the media playlist specified in the `#EXT-X-STREAM-INF` tag that most closely matches the value to list first. All other playlists maintain their current position in the manifest.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsFilterInBitrates" >

- `hlsFilterInBitrates` (_string_): With `hlsMode` set to `CUSTOM`, specifies a comma-delimited set of preferred bit rates, such as `100,200,400`. Playlists specified in the `#EXT-X-STREAM-INF` tag with bit rates outside of any of those values by up to 100 Kbps are excluded from the manifest.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsFilterInBitrateRanges" >

- `hlsFilterInBitrateRanges` (_string_): With `hlsMode` set to `CUSTOM`, specifies a comma-delimited set of bit rate ranges, such as `100-400,1000-4000`. Playlists specified in the `#EXT-X-STREAM-INF` tag with bit rates outside of any of those ranges are excluded from the manifest.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsQueryParamEnabled" >

- `hlsQueryParamEnabled` (_boolean_): With `hlsEnabled` on, allows you to specify query parameters for the HLS master manifest to customize the manifest's content.  Any settings specified in the query string override those already configured in Property Manager.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsQueryParamSecretKey" >

- `hlsQueryParamSecretKey` (_string_): With `hlsQueryParamEnabled` on, specifies a primary key as a token to accompany the request.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsQueryParamTransitionKey" >

- `hlsQueryParamTransitionKey` (_string_): With `hlsQueryParamEnabled` on, specifies a transition key as a token to accompany the request.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsShowAdvanced" >

- `hlsShowAdvanced` (_boolean_): With `hlsEnabled` on, allows you to configure advanced settings.

</div>

<div class="option" markdown="1" id="manifestPersonalization.hlsEnableDebugHeaders" >

- `hlsEnableDebugHeaders` (_boolean_): With `hlsShowAdvanced` enabled, includes additional `Akamai-Manifest-Personalization` and `Akamai-Manifest-Personalization-Config-Source` debugging headers.

</div>

</div>

<div class="feature" data-feature="manualServerPush" markdown="1">
