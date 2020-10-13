---
title: "mediaOriginFailover"
slug: "mediaoriginfailover"
hidden: false
createdAt: "2020-06-15T21:37:37.541Z"
updatedAt: "2020-06-15T21:37:37.541Z"
---
__Property Manager name__: [Media Origin Failover](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_9039)

Specifies how edge servers respond when the origin is unresponsive, or suffers from server or content errors. You can specify how many times to retry, switch to a backup origin hostname, or configure a redirect.

__Options__:

<div class="option" markdown="1" id="mediaOriginFailover.detectOriginUnresponsive" >

- `detectOriginUnresponsive` (_boolean_): When enabled, allows you to configure what happens when the origin is unresponsive.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveDetectionLevel" >

- `originUnresponsiveDetectionLevel` (_enum string_): With `detectOriginUnresponsive` enabled, specify whether your response to slow origin connections should be `AGGRESSIVE`, `MODERATE`, or `CONSERVATIVE`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveBlacklistOriginIp" >

- `originUnresponsiveBlacklistOriginIp` (_boolean_): With `detectOriginUnresponsive` enabled, enabling this blacklists the origin's IP address.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveBlacklistWindow" >

- `originUnresponsiveBlacklistWindow` (_enum string_): With `originUnresponsiveBlacklistOriginIp` enabled, this sets the delay before blacklisting an IP address, either `ONE_S`, `TEN_S`, or `THIRTY_S`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveRecovery" >

- `originUnresponsiveRecovery` (_enum string_): With `detectOriginUnresponsive` enabled, this sets the recovery option, either `RETRY_X_TIMES`, `SWITCH_TO_BACKUP_ORIGIN`, or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveRetryLimit" >

- `originUnresponsiveRetryLimit` (_enum string_): With `originUnresponsiveRecovery` set to `RETRY_X_TIMES`, sets whether to retry `ONE`, `TWO`, or `THREE` times.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveBackupHost" >

- `originUnresponsiveBackupHost` (_string_): With `originUnresponsiveRecovery` set to `SWITCH_TO_BACKUP_ORIGIN`, this specifies the origin hostname.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveAlternateHost" >

- `originUnresponsiveAlternateHost` (_string_): With `originUnresponsiveRecovery` set to `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, this specifies the redirect's destination hostname.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveModifyRequestPath" >

- `originUnresponsiveModifyRequestPath` (_boolean_): With `originUnresponsiveRecovery` set to `SWITCH_TO_BACKUP_ORIGIN` or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, enabling this allows you to modify the request path.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveModifiedPath" >

- `originUnresponsiveModifiedPath` (_string_): With `originUnresponsiveModifyRequestPath` enabled, this specifies the path to form the new URL.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveIncludeQueryString" >

- `originUnresponsiveIncludeQueryString` (_boolean_): With `originUnresponsiveModifyRequestPath` enabled, enabling this includes the original set of query parameters.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveRedirectMethod" >

- `originUnresponsiveRedirectMethod` (_numeric enum_): With `originUnresponsiveRecovery` set to `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, specifies either a `301` or `302` redirect response code.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveChangeProtocol" >

- `originUnresponsiveChangeProtocol` (_boolean_): With `originUnresponsiveRecovery` set to `SWITCH_TO_BACKUP_ORIGIN`, or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, enabling this allows you to change the request protocol.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnresponsiveProtocol" >

- `originUnresponsiveProtocol` (_enum string_): With `originUnresponsiveChangeProtocol` enabled, specifies either the `HTTP` or `HTTPS` protocol.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.detectOriginUnavailable" >

- `detectOriginUnavailable` (_boolean_): When enabled, allows you to configure failover settings when the origin server responds with errors.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableDetectionLevel" >

- `originUnavailableDetectionLevel` (_enum string_): With `detectOriginUnavailable` enabled, specify `RESPONSE_CODES`, the only available option.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableResponseCodes" >

- `originUnavailableResponseCodes` (_array of string values_): With `detectOriginUnavailable` enabled, specifies the set of response codes identifying when the origin responds with errors.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableBlacklistOriginIp" >

- `originUnavailableBlacklistOriginIp` (_boolean_): With `detectOriginUnavailable` enabled, enabling this blacklists the origin's IP address.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableBlacklistWindow" >

- `originUnavailableBlacklistWindow` (_enum string_): With `originUnavailableBlacklistOriginIp` enabled, this sets the delay before blacklisting an IP address, either `ONE_S`, `TEN_S`, or `THIRTY_S`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableRecovery" >

- `originUnavailableRecovery` (_enum string_): With `detectOriginUnavailable` enabled, this sets the recovery option, either `RETRY_X_TIMES`, `SWITCH_TO_BACKUP_ORIGIN`, or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableRetryLimit" >

- `originUnavailableRetryLimit` (_enum string_): With `originUnavailableRecovery` set to `RETRY_X_TIMES`, sets whether to retry `ONE`, `TWO`, or `THREE` times.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableBackupHost" >

- `originUnavailableBackupHost` (_string_): With `originUnavailableRecovery` set to `SWITCH_TO_BACKUP_ORIGIN`, this specifies the origin hostname.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableAlternateHost" >

- `originUnavailableAlternateHost` (_string_): With `originUnavailableRecovery` set to `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, this specifies the redirect's destination hostname.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableModifyRequestPath" >

- `originUnavailableModifyRequestPath` (_boolean_): With `originUnavailableRecovery` set to `SWITCH_TO_BACKUP_ORIGIN` or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, enabling this allows you to modify the request path.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableModifiedPath" >

- `originUnavailableModifiedPath` (_string_): With `originUnavailableModifyRequestPath` enabled, this specifies the path to form the new URL.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableIncludeQueryString" >

- `originUnavailableIncludeQueryString` (_boolean_): With `originUnavailableModifyRequestPath` enabled, enabling this includes the original set of query parameters.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableRedirectMethod" >

- `originUnavailableRedirectMethod` (_numeric enum_): With `originUnavailableRecovery` set to `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, specifies either a `301` or `302` redirect response code.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableChangeProtocol" >

- `originUnavailableChangeProtocol` (_boolean_): With `originUnavailableRecovery` set to `SWITCH_TO_BACKUP_ORIGIN` or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, enabling this allows you to modify the request protocol.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.originUnavailableProtocol" >

- `originUnavailableProtocol` (_enum string_): With `originUnavailableChangeProtocol` enabled, specifies either the `HTTP` or `HTTPS` protocol.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.detectObjectUnavailable" >

- `detectObjectUnavailable` (_boolean_): When enabled, allows you to configure failover settings when the origin has content errors.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableDetectionLevel" >

- `objectUnavailableDetectionLevel` (_enum string_): With `detectObjectUnavailable` enabled, specify `RESPONSE_CODES`, the only available option.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableResponseCodes" >

- `objectUnavailableResponseCodes` (_array of string values_): With `detectObjectUnavailable` enabled, specifies the set of response codes identifying when there are content errors.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableBlacklistOriginIp" >

- `objectUnavailableBlacklistOriginIp` (_boolean_): With `detectObjectUnavailable` enabled, enabling this blacklists the origin's IP address.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableBlacklistWindow" >

- `objectUnavailableBlacklistWindow` (_enum string_): With `objectUnavailableBlacklistOriginIp` enabled, this sets the delay before blacklisting an IP address, either `ONE_S`, `TEN_S`, or `THIRTY_S`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableRecovery" >

- `objectUnavailableRecovery` (_enum string_): With `detectObjectUnavailable` enabled, this sets the recovery option, either `RETRY_X_TIMES`, `SWITCH_TO_BACKUP_ORIGIN`, or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableRetryLimit" >

- `objectUnavailableRetryLimit` (_enum string_): With `objectUnavailableRecovery` set to `RETRY_X_TIMES`, sets whether to retry `ONE`, `TWO`, or `THREE` times.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableBackupHost" >

- `objectUnavailableBackupHost` (_string_): With `objectUnavailableRecovery` set to `SWITCH_TO_BACKUP_ORIGIN`, this specifies the origin hostname.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableAlternateHost" >

- `objectUnavailableAlternateHost` (_string_): With `objectUnavailableRecovery` set to `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, this specifies the redirect's destination hostname.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableModifyRequestPath" >

- `objectUnavailableModifyRequestPath` (_boolean_): With `objectUnavailableRecovery` set to `SWITCH_TO_BACKUP_ORIGIN` or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, enabling this allows you to modify the request path.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableModifiedPath" >

- `objectUnavailableModifiedPath` (_string_): With `objectUnavailableModifyRequestPath` enabled, this specifies the path to form the new URL.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableIncludeQueryString" >

- `objectUnavailableIncludeQueryString` (_boolean_): With `objectUnavailableModifyRequestPath` enabled, enabling this includes the original set of query parameters.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableRedirectMethod" >

- `objectUnavailableRedirectMethod` (_numeric enum_): With `objectUnavailableRecovery` set to `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, specifies either a `301` or `302` redirect response code.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableChangeProtocol" >

- `objectUnavailableChangeProtocol` (_boolean_): With `objectUnavailableRecovery` set to `SWITCH_TO_BACKUP_ORIGIN` or `REDIRECT_TO_DIFFERENT_ORIGIN_LOCATION`, enabling this allows you to change the request protocol.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.objectUnavailableProtocol" >

- `objectUnavailableProtocol` (_enum string_): With `objectUnavailableChangeProtocol` enabled, specifies either the `HTTP` or `HTTPS` protocol.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.clientResponseCode" >

- `clientResponseCode` (_string_): Specifies the response code served to the client.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.cacheErrorResponse" >

- `cacheErrorResponse` (_boolean_): When enabled, caches the error response.

</div>

<div class="option" markdown="1" id="mediaOriginFailover.cacheWindow" >

- `cacheWindow` (_enum string_): With `cacheErrorResponse` enabled, this sets error response's TTL, either `ONE_S`, `TEN_S`, or `THIRTY_S`.

</div>

</div>

<div class="feature" data-feature="metadataCaching" markdown="1">
