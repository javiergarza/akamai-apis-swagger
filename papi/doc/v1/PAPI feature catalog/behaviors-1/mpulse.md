---
title: "mPulse"
slug: "mpulse"
hidden: false
createdAt: "2020-06-15T21:40:44.024Z"
updatedAt: "2020-06-15T21:40:44.024Z"
---
__Property Manager name__: [mPulse](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0055)

[mPulse](https://learn.akamai.com/en-us/products/web_performance/mpulse.html)
provides high-level performance analytics and predictive
recommendations based on real end user data. See the
[mPulse Quick Start](https://learn.akamai.com/en-us/webhelp/mpulse/mpulse-help/)
to set up mPulse on your website.

__Options__:

<div class="option" markdown="1" id="mPulse.enabled" >

- `enabled` (_boolean_): Applies performance monitoring to this behavior's set of content.

</div>

<div class="option" markdown="1" id="mPulse.requirePci" >

- `requirePci` (_boolean_): Suppresses gathering metrics for potentially sensitive end-user interactions. Enabling this omits data from some older browsers.

</div>

<div class="option" markdown="1" id="mPulse.apiKey" >

- `apiKey` (_string_): This generated value uniquely identifies sections of your website for you to analyze independently. To access this value, see [Enable mPulse in Property Manager](https://learn-qa.akamai.com/en-us/webhelp/mpulse/mpulse-help/GUID-8F356E35-C374-4598-90D7-5BE8CE770369.html).

</div>

<div class="option" markdown="1" id="mPulse.bufferSize" >

- `bufferSize` (_string_): Allows you to override the browser's default (150) maximum number of reported performance timeline entries.

</div>

<div class="option" markdown="1" id="mPulse.configOverride" >

- `configOverride` (_string_): A JSON string representing a configuration object passed to the JavaScript library under which mPulse runs. It corresponds at run-time to the `window.BOOMR_config` object. For example, this turns on monitoring of Single Page App frameworks: `"{\"history\": {\"enabled\": true, \"auto\": true}}"`.  See [Configuration Overrides](https://developer.akamai.com/tools/boomerang/#configuration-overrides) for more information.

</div>

</div>

<div class="feature" data-feature="netSession" markdown="1">
