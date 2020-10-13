---
title: "subCustomer"
slug: "subcustomer"
hidden: false
createdAt: "2020-06-15T22:05:04.938Z"
updatedAt: "2020-06-15T22:05:04.938Z"
---
__Property Manager name__: [Subcustomer Enablement](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5000)

When positioned in a property's top-level default rule, enables various [Cloud Embed](https://learn.akamai.com/en-us/products/media_delivery/cloud_embed.html) features that allow you to leverage Akamai's CDN architecture for your own subcustomers.  This behavior's options allow you to use Cloud Embed to configure your subcustomers' content.  Once enabled, you can use the [Akamai Cloud Embed API](https://developer.akamai.com/api/media_delivery/cloud_embed/v2.html) (ACE) to assign subcustomers to this base configuration, and to customize policies for them.  See also the [`dynamicWebContent`](#dynamicwebcontent) behavior to configure subcustomers' dynamic web content.

__Options__:

<div class="option" markdown="1" id="subCustomer.enabled" >

- `enabled` (_boolean_): Allows Cloud Embed to dynamically modify your subcustomers' content.

</div>

<div class="option" markdown="1" id="subCustomer.origin" >

- `origin` (_boolean_): Allows you to assign origin hostnames for customers.

</div>

<div class="option" markdown="1" id="subCustomer.partnerDomainSuffix" >

- `partnerDomainSuffix` (_string_): With `origin` enabled, this specifies the appropriate domain suffix, which you should typically match with your property hostname. It identifies the domain as trustworthy on the Akamai network, despite being defined within Cloud Embed, outside of your base property configuration. Include this domain suffix if you want to purge subcustomer URLs. For example, if you provide a value of `suffix.example.com`, then to purge `subcustomer.com/some/path`, specify `subcustomer.com.suffix.example.com/some/path` as the purge request's URL.

</div>

<div class="option" markdown="1" id="subCustomer.caching" >

- `caching` (_boolean_): Modifies content caching rules.

</div>

<div class="option" markdown="1" id="subCustomer.referrer" >

- `referrer` (_boolean_): Sets subcustomers' referrer whitelists or blacklist.

</div>

<div class="option" markdown="1" id="subCustomer.ip" >

- `ip` (_boolean_): Sets subcustomers' IP whitelists or blacklists.

</div>

<div class="option" markdown="1" id="subCustomer.geoLocation" >

- `geoLocation` (_boolean_): Sets subcustomers' location-based whitelists or blacklists.

</div>

<div class="option" markdown="1" id="subCustomer.refreshContent" >

- `refreshContent` (_boolean_): Allows you to reschedule when content validates for subcustomers.

</div>

<div class="option" markdown="1" id="subCustomer.modifyPath" >

- `modifyPath` (_boolean_): Modifies a subcustomer's request path.

</div>

<div class="option" markdown="1" id="subCustomer.cacheKey" >

- `cacheKey` (_boolean_): Allows you to set which query parameters are included in the cache key.

</div>

<div class="option" markdown="1" id="subCustomer.tokenAuthorization" >

- `tokenAuthorization` (_boolean_): When enabled, this allows you to configure edge servers to use tokens to control access to subcustomer content.  Use Cloud Embed to configure the token to appear in a cookie, header, or query parameter.

</div>

<div class="option" markdown="1" id="subCustomer.siteFailover" >

- `siteFailover` (_boolean_): When enabled, allows you to configure unique failover sites for each subcustomer's policy.

</div>

<div class="option" markdown="1" id="subCustomer.contentCompressor" >

- `contentCompressor` (_boolean_): Allows compression of subcustomer content.

</div>

<div class="option" markdown="1" id="subCustomer.accessControl" >

- `accessControl` (_boolean_): When enabled, this allows you to deny requests to a subcustomer's content based on specific match conditions, which you use Cloud Embed to configure in each subcustomer's policy.

</div>

<div class="option" markdown="1" id="subCustomer.dynamicWebContent" >

- `dynamicWebContent` (_boolean_): When enabled, allows you to apply the [`dynamicWebContent`](#dynamicwebcontent) behavior to further modify how dynamic content behaves for subcustomers.

</div>

<div class="option" markdown="1" id="subCustomer.onDemandVideoDelivery" >

- `onDemandVideoDelivery` (_boolean_): Enables delivery of media assets to subcustomers.

</div>

<div class="option" markdown="1" id="subCustomer.largeFileDelivery" >

- `largeFileDelivery` (_boolean_): Enables large file delivery for subcustomers.

</div>

<div class="option" markdown="1" id="subCustomer.liveVideoDelivery" >

- `liveVideoDelivery` (_boolean_): Enables live media streaming for subcustomers.

</div>

<div class="option" markdown="1" id="subCustomer.webApplicationFirewall" >

- `webApplicationFirewall` (_boolean_): 2DO

</div>

</div>

<div class="feature" data-feature="sureRoute" markdown="1">
