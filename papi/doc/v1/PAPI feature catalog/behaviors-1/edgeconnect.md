---
title: "edgeConnect"
slug: "edgeconnect"
hidden: false
createdAt: "2020-06-15T21:18:32.608Z"
updatedAt: "2020-06-15T21:18:32.608Z"
---
__Property Manager name__: [Cloud Monitor Instrumentation](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9021)

Configures traffic logs for the [Cloud Monitor](http://www.akamai.com/html/technology/cloud-monitor.html) push API.

__Options__:

<div class="option" markdown="1" id="edgeConnect.enabled" >

- `enabled` (_boolean_): Enables Cloud Monitor's log-publishing behavior.

</div>

<div class="option" markdown="1" id="edgeConnect.apiConnector" >

- `apiConnector` (_enum string_): Describes the API connector type, either `DEFAULT`, `BMC_APM`, or `SIEM_JSON`.

</div>

<div class="option" markdown="1" id="edgeConnect.apiDataElements" >

- `apiDataElements` (_array of string values_): Specifies the data set to log, any of the following values:

<pre style="-webkit-column-width:2in;-moz-column-width:2in;column-width:2in;margin-left:3pc">
 APM
 GEO
 HTTP
 NETWORK_PERFORMANCE
 NETWORK_V1
 REQUEST_HEADER
 RESPONSE_HEADER
 SEC_APP_V2
 SEC_RATE_DENY_V2
 SEC_RATE_WARN_V2
</pre>

</div>

<div class="option" markdown="1" id="edgeConnect.destinationHostname" >

- `destinationHostname` (_string_): Specifies the target hostname accepting push API requests.

</div>

<div class="option" markdown="1" id="edgeConnect.destinationPath" >

- `destinationPath` (_string_): Specifies the push API's endpoint.

</div>

<div class="option" markdown="1" id="edgeConnect.overrideAggregateSettings" >

- `overrideAggregateSettings` (_boolean_): When enabled, overrides default log settings.

</div>

<div class="option" markdown="1" id="edgeConnect.aggregateTime" >

- `aggregateTime` (_duration string_): With `overrideAggregateSettings` enabled, specifies how often logs are generated.

</div>

<div class="option" markdown="1" id="edgeConnect.aggregateLines" >

- `aggregateLines` (_string_): With `overrideAggregateSettings` enabled, specifies the maximum number of lines to include in each log.

</div>

<div class="option" markdown="1" id="edgeConnect.aggregateSize" >

- `aggregateSize` (_string_): With `overrideAggregateSettings` enabled, specifies the log's maximum size.

</div>

</div>

<div class="feature" data-feature="edgeImageConversion" markdown="1">
