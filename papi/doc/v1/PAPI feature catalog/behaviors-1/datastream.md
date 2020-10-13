---
title: "datastream"
slug: "datastream"
hidden: false
createdAt: "2020-06-15T21:05:46.929Z"
updatedAt: "2020-06-15T21:05:46.929Z"
---
__Property Manager name__: [DataStream](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9005)

The [DataStream](https://learn.akamai.com/en-us/products/web_performance/datastream.html) reporting service provides real-time logs on application activity, including aggregated metrics on complete request and response cycles and origin response times.  Apply this behavior to report on this set of traffic.  Use the [DataStream API](https://developer.akamai.com/api/web_performance/datastream/v1.html) to aggregate the data.

__Options__:

<div class="option" markdown="1" id="datastream.streamType" >

- `streamType` (_enum string_): 2DO: `BEACON`, `BEACON_AND_LOG`, `LOG`

</div>

<div class="option" markdown="1" id="datastream.enabled" >

- `enabled` (_boolean_): Enables DataStream reporting.

</div>

<div class="option" markdown="1" id="datastream.datastreamIds" >

- `datastreamIds` (_string_): A set of dash-separated DataStream ID values to limit the scope of reported data. By default, all active streams report. Use the DataStream application to gather stream ID values that apply to this property configuration. Specifying IDs for any streams that don't apply to this property has no effect, and results in no data reported.

</div>

<div class="option" markdown="1" id="datastream.logEnabled" >

- `logEnabled` (_boolean_): 2DO

</div>

<div class="option" markdown="1" id="datastream.logStreamName" >

- `logStreamName` (_string_): 2DO

</div>

<div class="option" markdown="1" id="datastream.samplingPercentage" >

- `samplingPercentage` (_number_): 2DO

</div>

</div>

<div class="feature" data-feature="dcp" markdown="1">
