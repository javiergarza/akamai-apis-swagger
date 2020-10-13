---
title: "origin"
slug: "origin"
hidden: false
createdAt: "2020-06-15T21:42:47.153Z"
updatedAt: "2020-06-15T21:42:47.153Z"
---
__Property Manager name__: [Origin Server](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0058)

Specify the hostname and settings used to contact the origin once service begins. You can use your own origin, [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html), an [Edge Load Balancing](http://control.akamai.com/dl/customers/other/Edge_Load_Balancing/Terra_Alta_Edge_Load_Balancing.pdf) origin, or a [SaaS](https://control.akamai.com/dl/customers/SaaS/SaaS-User-Guide.pdf) dynamic origin.

__Options__:

<div class="option" markdown="1" id="origin.originType" >

- `originType` (_enum string_): Choose whether your content is retrieved from your own server (`CUSTOMER`), your [NetStorage](https://learn.akamai.com/en-us/products/media_delivery/netstorage.html) account (`NET_STORAGE`), any available [Edge Load Balancing](http://control.akamai.com/dl/customers/other/Edge_Load_Balancing/Terra_Alta_Edge_Load_Balancing.pdf) origin (`EDGE_LOAD_BALANCING_ORIGIN_GROUP`), a set of [Application Load Balancer](#applicationloadbalancer) origins (`APPLICATION_LOAD_BALANCER`), a SaaS dynamic origin (`SAAS_DYNAMIC_ORIGIN`) if SaaS acceleration is available on your contract, or `MEDIA_SERVICE_LIVE`. NetStorage is most appropriate for static content.

</div>

<div class="option" markdown="1" id="origin.netStorage" >

- `netStorage` (_object_): If the `originType` is `NET_STORAGE`, this option specifies the details of the netstorage server. For example:

        "netStorage": {
            "id"                 : "netstorage_id",
            "name"               : "Example Downloads",
            "downloadDomainName" : "download.example.com",
            "cpCode"             : 12345
        }

</div>

<div class="option" markdown="1" id="origin.originId" >

- `originId` (_string_): With the `originType` set to `EDGE_LOAD_BALANCING_ORIGIN_GROUP`, identifies the Edge Load Balancing origin. This must correspond to an [`edgeLoadBalancingOrigin`](#edgeloadbalancingorigin) behavior's `id` attribute within the same property.

</div>

<div class="option" markdown="1" id="origin.hostname" >

- `hostname` (_string; allows [variables](#vf)_): With the `originType` set to `CUSTOMER`, this specifies the hostname or IPv4 address of your origin server, from which edge servers can retrieve your content.

</div>

<div class="option" markdown="1" id="origin.mslorigin" >

- `mslorigin` (_string_): With `originType` set to `MEDIA_SERVICE_LIVE`, this specifies the media's origin server.

</div>

<div class="option" markdown="1" id="origin.saasType" >

- `saasType` (_enum string_): With `originType` set to `SAAS_DYNAMIC_ORIGIN`, specifies the part of the request that identifies this SaaS dynamic origin, either `PATH`, `COOKIE`, `QUERY_STRING`, or `HOSTNAME`.

</div>

<div class="option" markdown="1" id="origin.saasCnameEnabled" >

- `saasCnameEnabled` (_boolean_): With `saasType` set to `HOSTNAME`, enabling this allows you to use a _CNAME chain_ to determine the hostname for this SaaS dynamic origin.

</div>

<div class="option" markdown="1" id="origin.saasCnameLevel" >

- `saasCnameLevel` (_number_): With `saasType` set to `HOSTNAME` and `saasCnameEnabled` on, specifies the desired number of hostnames to use in the _CNAME chain_, starting backwards from the edge server.

</div>

<div class="option" markdown="1" id="origin.saasCookie" >

- `saasCookie` (_string_): With the `originType` set to `SAAS_DYNAMIC_ORIGIN` and the `saasType` set to `COOKIE`, this specifies the name of the cookie that identifies this SaaS dynamic origin.

</div>

<div class="option" markdown="1" id="origin.saasQueryString" >

- `saasQueryString` (_string_): With the `originType` set to `SAAS_DYNAMIC_ORIGIN` and the `saasType` set to `QUERY_STRING`, this specifies the name of the query parameter that identifies this SaaS dynamic origin.

</div>

<div class="option" markdown="1" id="origin.saasRegex" >

- `saasRegex` (_string_): With the `originType` set to `SAAS_DYNAMIC_ORIGIN`, this specifies the Perl-compatible regular expression match that identifies this SaaS dynamic origin.

</div>

<div class="option" markdown="1" id="origin.saasReplace" >

- `saasReplace` (_string_): Specifies replacement text for what `saasRegex` matches.

</div>

<div class="option" markdown="1" id="origin.saasSuffix" >

- `saasSuffix` (_string_): With the `originType` set to `SAAS_DYNAMIC_ORIGIN`, specifies the static part of the SaaS dynamic origin.

</div>

<div class="option" markdown="1" id="origin.forwardHostHeader" >

- `forwardHostHeader` (_enum string_): When the `originType` is set to either `CUSTOMER` or `SAAS_DYNAMIC_ORIGIN`, this specifies which `Host` header to pass to the origin:

    - `REQUEST_HOST_HEADER` passes the original request's header.
    - `ORIGIN_HOSTNAME` passes the current origin's `HOSTNAME`.
    - `CUSTOM` passes the value of `customForwardHostHeader`. Use this     option if you want requests handled by different properties to     converge on the same cached object.

</div>

<div class="option" markdown="1" id="origin.customForwardHostHeader" >

- `customForwardHostHeader` (_string; allows [variables](#vf)_): With `forwardHostHeader` set to `CUSTOM`, this specifies the name of the custom host header the edge server should pass to the origin.

</div>

<div class="option" markdown="1" id="origin.cacheKeyHostname" >

- `cacheKeyHostname` (_enum string_): With the `originType` set to `CUSTOM`, this specifies the hostname to use when forming a cache key. Specify `ORIGIN_HOSTNAME` if your origin server's responses do not depend on the hostname, otherwise specify `REQUEST_HOST_HEADER` when using a virtual server.

</div>

<div class="option" markdown="1" id="origin.useUniqueCacheKey" >

- `useUniqueCacheKey` (_boolean_): With `cacheKeyHostname` set to `ORIGIN_HOSTNAME` and a shared `hostname` such as provided by Amazon AWS, sets a unique cache key for your content.

</div>

<div class="option" markdown="1" id="origin.compress" >

- `compress` (_boolean_): Enables _gzip_ compression for non-NetStorage origins.

</div>

<div class="option" markdown="1" id="origin.enableTrueClientIp" >

- `enableTrueClientIp` (_boolean_): When enabled on non-NetStorage origins, allows you to send a custom header (the `trueClientIpHeader`) identifying the IP address of the immediate client connecting to the edge server. This may provide more useful information than the standard `X-Forward-For` header, which proxies may modify.

</div>

<div class="option" markdown="1" id="origin.trueClientIpHeader" >

- `trueClientIpHeader` (_string_): With `enableTrueClientIp` enabled, this specifies the name of the field that identifies the end client's IP address, for example `True-Client-IP`.

</div>

<div class="option" markdown="1" id="origin.trueClientIpClientSetting" >

- `trueClientIpClientSetting` (_boolean_): With `enableTrueClientIp` on along with this option, if a client sets the `True-Client-IP` header, the edge server allows it and passes the value to the origin. Otherwise the edge server removes it and sets the value itself.

</div>

<div class="option" markdown="1" id="origin.verificationMode" >

- `verificationMode` (_enum string_): For non-NetStorage origins, maximize security by controlling which certificates edge servers should trust, either `PLATFORM_SETTINGS`, `THIRD_PARTY` when your origin server references certain types of third-party hostname, or `CUSTOM`. The `CUSTOM` option only applies if the property is marked as secure. See [Secure property requirements](#sf) for guidance. Under some products, you may also need to enable the _Secure Delivery - Customer Cert_ module. Contact your Akamai representative for details.

</div>

<div class="option" markdown="1" id="origin.originSni" >

- `originSni` (_boolean_): For non-NetStorage origins, enabling this adds a Server Name Indication (SNI) header in the SSL request sent to the origin, with the origin hostname as the value.  Contact your Akamai representative for more information.

</div>

<div class="option" markdown="1" id="origin.customValidCnValues" >

- `customValidCnValues` (_array of string values_): With `verificationMode` set to `CUSTOM`, specifies values to look for in the origin certificate's `Subject Alternate Name` or `Common Name` fields. Specify `{{ "{{" }}Origin Hostname}}` and `{{ "{{" }}Forward Host Header}}` within the text in the order you want them to be evaluated. (Note that these two template items are not the same as in-line [variables](#vf), which use the same curly-brace syntax.)

</div>

<div class="option" markdown="1" id="origin.originCertsToHonor" >

- `originCertsToHonor` (_enum string_): With `verificationMode` set to `CUSTOM`, specifies whether to trust pinned origin server certificates (`CUSTOM_CERTIFICATES`), any certificate signed by an Akamai-managed authority set (`STANDARD_CERTIFICATE_AUTHORITIES`), or any certificate signed by a custom authority set you manage (`CUSTOM_CERTIFICATE_AUTHORITIES`). If set to `COMBO`, may rely on all three inputs.

</div>

<div class="option" markdown="1" id="origin.standardCertificateAuthorities" >

- `standardCertificateAuthorities` (_object_): With `originCertsToHonor` set to either `STANDARD_CERTIFICATE_AUTHORITIES` or `COMBO`, specifies an array of Akamai-managed certificate names. Currently, the only allowed value is `akamai-permissive`.

</div>

<div class="option" markdown="1" id="origin.customCertificateAuthorities" >

- `customCertificateAuthorities` (_object_): With `originCertsToHonor` set to either `CUSTOM_CERTIFICATE_AUTHORITIES` or `COMBO`, specifies an array of certification objects. Contact your Akamai representative for details on this object's requirements.

</div>

<div class="option" markdown="1" id="origin.customCertificates" >

- `customCertificates` (_object_): With `originCertsToHonor` set to either `CUSTOM_CERTIFICATES` or `COMBO`, specifies an array of certification objects. Contact your Akamai representative for details on this object's requirements.

</div>

<div class="option" markdown="1" id="origin.httpPort" >

- `httpPort` (_number_): Specifies the port on your origin server to which edge servers should connect for HTTP requests, customarily `80`.

</div>

<div class="option" markdown="1" id="origin.httpsPort" >

- `httpsPort` (_number_): Specifies the port on your origin server to which edge servers should connect for secure HTTPS requests, customarily `443`. This option only applies if the property is marked as secure. See [Secure property requirements](#sf) for guidance.

</div>

</div>

<div class="feature" data-feature="originCharacteristics" markdown="1">
