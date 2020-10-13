---
title: "aggregatedReporting"
slug: "aggregatedreporting"
hidden: false
createdAt: "2020-06-15T20:25:17.997Z"
updatedAt: "2020-06-15T20:29:51.526Z"
---
__Property Manager name__: [Aggregated Reporting](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0010)

Configure attributes for your custom aggregated reports. You can configure up to four attributes.

__Options__:

<div class="option" markdown="1" id="aggregatedReporting.enabled" >

- `enabled` (_boolean_): Enables aggregated reporting.

</div>

<div class="option" markdown="1" id="aggregatedReporting.reportName" >

- `reportName` (_string_): The unique name of the aggregated report within the property. If you reconfigure any attributes or variables in the aggregated reporting behavior, update this field to a unique value to enable logging data in a new instance of the report.

</div>

<div class="option" markdown="1" id="aggregatedReporting.attributesCount" >

- `attributesCount` (_number within 1-4 range_): Select the number of attributes by which your report is grouped. You can add up to four attributes.

</div>

<div class="option" markdown="1" id="aggregatedReporting.attribute1" >

- `attribute1` (_string; allows [variables](#vf)_): Select a previously user-defined variable to be an attribute for the report. The values extracted for all attributes range from 0 to 20 characters.

</div>

<div class="option" markdown="1" id="aggregatedReporting.attribute2" >

- `attribute2` (_string; allows [variables](#vf)_): Select a previously user-defined variable to be an attribute for the report. The values extracted for all attributes range from 0 to 20 characters.

</div>

<div class="option" markdown="1" id="aggregatedReporting.attribute3" >

- `attribute3` (_string; allows [variables](#vf)_): Select a previously user-defined variable to be an attribute for the report. The values extracted for all attributes range from 0 to 20 characters.

</div>

<div class="option" markdown="1" id="aggregatedReporting.attribute4" >

- `attribute4` (_string; allows [variables](#vf)_): Select a previously user-defined variable to be an attribute for the report. The values extracted for all attributes range from 0 to 20 characters.

</div>
