---
title: "httpStrictTransportSecurity"
slug: "httpstricttransportsecurity"
hidden: false
createdAt: "2020-06-15T21:29:00.488Z"
updatedAt: "2020-06-15T21:29:00.488Z"
---
__Property Manager name__: [HTTP Strict Transport Security](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_1000)

Applies HTTP Strict Transport Security (HSTS), disallowing insecure HTTP traffic. Apply this to hostnames managed with Standard TLS or Enhanced TLS certificates.

__Options__:

<div class="option" markdown="1" id="httpStrictTransportSecurity.enable" >

- `enable` (_boolean_): Applies HSTS to this set of requests.

</div>

<div class="option" markdown="1" id="httpStrictTransportSecurity.maxAge" >

- `maxAge` (_enum string_): Specifies the duration for which to apply HSTS for new browser connections, either `TEN_MINS`, `ONE_DAY`, `ONE_MONTH`, `THREE_MONTHS`, `SIX_MONTHS`, or `ONE_YEAR`.  A value of `ZERO_MINS` effectively disables HSTS, without affecting any existing browser connections.

</div>

<div class="option" markdown="1" id="httpStrictTransportSecurity.includeSubDomains" >

- `includeSubDomains` (_boolean_): When enabled, applies HSTS to all subdomains.

</div>

<div class="option" markdown="1" id="httpStrictTransportSecurity.preload" >

- `preload` (_boolean_): When enabled, adds this domain to the browser's preload list. You still need to declare the domain at [hstspreload.org](https://hstspreload.org/).

</div>

<div class="option" markdown="1" id="httpStrictTransportSecurity.redirect" >

- `redirect` (_boolean_): When enabled, redirects all HTTP requests to HTTPS.

</div>

<div class="option" markdown="1" id="httpStrictTransportSecurity.redirectStatusCode" >

- `redirectStatusCode` (_numeric enum_): With `redirect` enabled, specifies a `301` or `302` response code.

</div>

</div>

<div class="feature" data-feature="httpToHttpsUpgrade" markdown="1">
