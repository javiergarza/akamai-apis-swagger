---
title: "netSession"
slug: "netsession"
hidden: false
createdAt: "2020-06-15T21:41:07.516Z"
updatedAt: "2020-06-15T21:41:07.516Z"
---
__Property Manager name__: [NetSession](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9058)

This behavior enables various features of [NetSession](https://learn.akamai.com/en-us/products/media_delivery/netsession_download_manager.html), a client-side download manager application that's especially appropriate for large file downloads.  For the feature to work, the end user needs to download the DLM client.

__Options__:

<div class="option" markdown="1" id="netSession.enabled" >

- `enabled` (_boolean_): Enables NetSession DLM capabilities for this content.

</div>

<div class="option" markdown="1" id="netSession.enableDomain" >

- `enableDomain` (_boolean_): Enables Download Manager domains.

</div>

<div class="option" markdown="1" id="netSession.enableDownloadManager" >

- `enableDownloadManager` (_boolean_): When enabled, launches files once they are fully downloaded. For example, specify this option to run an executable application.

</div>

<div class="option" markdown="1" id="netSession.enableDownloadClients" >

- `enableDownloadClients` (_boolean_): When enabled, allows download clients to form a peer-to-peer network to reduce transmission time.

</div>

<div class="option" markdown="1" id="netSession.disableReporting" >

- `disableReporting` (_boolean_): Disable download state reporting via HTTP beacon messages. Otherwise when enabled, you can view the state of each download by choosing __Monitor__ &rArr; __Download Analytics__ on the DLM client.

</div>

<div class="option" markdown="1" id="netSession.resumeUrl" >

- `resumeUrl` (_array of string values_): Specify an alternate domain from which to resume a paused download. This generates a corresponding shortcut link on the end user's desktop that disappears after the download is complete.

</div>

<div class="option" markdown="1" id="netSession.organizationName" >

- `organizationName` (_string_): The name of the organization that displays in the NetSession client DLM interface.

</div>

<div class="option" markdown="1" id="netSession.supportUrl" >

- `supportUrl` (_string_): A supporting link to the `organizationName` that displays in the NetSession client DLM interface.

</div>

</div>

<div class="feature" data-feature="networkConditionsHeader" markdown="1">
