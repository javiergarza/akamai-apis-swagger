---
title: "salesForceCommerceCloudClient"
slug: "salesforcecommercecloudclient"
hidden: false
createdAt: "2020-06-15T21:57:52.485Z"
updatedAt: "2020-06-15T21:57:52.485Z"
---
__Property Manager name__: [Akamai Connector for Salesforce Commerce Cloud](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_3001)

If you use the Salesforce Commerce Cloud platform for your origin content, this behavior allows your edge content managed by Akamai to contact directly to origin.

__Options__:

<div class="option" markdown="1" id="salesForceCommerceCloudClient.enabled" >

- `enabled` (_boolean_): Enables the Akamai Connector for Salesforce Commerce Cloud.

</div>

<div class="option" markdown="1" id="salesForceCommerceCloudClient.connectorId" >

- `connectorId` (_string; allows [variables](#vf)_): An ID value that helps distinguish different types of traffic sent from Akamai to the Salesforce Commerce Cloud. Form the value as _instance-realm-customer_, where _instance_ is either `production` or `development`, _realm_ is your Salesforce Commerce Cloud service `$REALM` value, and _customer_ is the name for your organization in Salesforce Commerce Cloud.  You can use alphanumeric characters, underscores, or dot characters within dash-delimited segment values.

</div>

<div class="option" markdown="1" id="salesForceCommerceCloudClient.originType" >

- `originType` (_enum string_): Specifies whether to use a `DEFAULT` Salesforce origin, or a `CUSTOMER` defined origin.

</div>

<div class="option" markdown="1" id="salesForceCommerceCloudClient.sf3cOriginHost" >

- `sf3cOriginHost` (_string; allows [variables](#vf)_): With `originType` set to `CUSTOMER`, this specifies the hostname or IP address of the custom Salesforce origin.

</div>

<div class="option" markdown="1" id="salesForceCommerceCloudClient.originHostHeader" >

- `originHostHeader` (_enum string_): Specifies whether to use a `DEFAULT` or `CUSTOMER` defined Salesforce host header.

</div>

<div class="option" markdown="1" id="salesForceCommerceCloudClient.sf3cOriginHostHeader" >

- `sf3cOriginHostHeader` (_string; allows [variables](#vf)_): With `originHostHeader` set to `CUSTOMER`, this specifies the hostname or IP address of the custom Salesforce host header.

</div>

<div class="option" markdown="1" id="salesForceCommerceCloudClient.allowOverrideOriginCacheKey" >

- `allowOverrideOriginCacheKey` (_boolean_): When enabled, overrides the forwarding origin's cache key.

</div>

</div>

<div class="feature" data-feature="salesForceCommerceCloudProvider" markdown="1">
