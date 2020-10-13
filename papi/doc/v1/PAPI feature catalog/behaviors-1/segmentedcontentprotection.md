---
title: "segmentedContentProtection"
slug: "segmentedcontentprotection"
hidden: false
createdAt: "2020-06-15T22:00:09.012Z"
updatedAt: "2020-06-15T22:00:09.012Z"
---
__Property Manager name__: [Segmented Media Protection](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0079)

Validates authorization tokens at the edge server to prevent unauthorized link sharing.

__Options__:

<div class="option" markdown="1" id="segmentedContentProtection.enabled" >

- `enabled` (_boolean_): Enables the segmented content protection behavior.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.key" >

- `key` (_string_): Specifies the encryption key to use as a shared secret to validate tokens.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.useAdvanced" >

- `useAdvanced` (_boolean_): When enabled, allows you to specify advanced `transitionKey` and `salt` options.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.transitionKey" >

- `transitionKey` (_string_): An alternate encryption key to match along with the `key` field, allowing you to rotate keys with no down time.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.salt" >

- `salt` (_string_): Specifies a salt as input into the token for added security. This value must match the salt used in the token generation code.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.headerForSalt" >

- `headerForSalt` (_array of string values_): With `useAdvanced` enabled, this allows you to include additional salt properties specific to each end user to strengthen the relationship between the session token and playback session. This specifies the set of request headers whose values generate the salt value, typically `User-Agent`, `X-Playback-Session-Id`, and `Origin`. Any specified header must appear in the player's request.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.sessionId" >

- `sessionId` (_boolean_): With `useAdvanced` enabled, enabling this option carries the `session_id` value from the access token over to the session token, for use in tracking and counting unique playback sessions.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.dataPayload" >

- `dataPayload` (_boolean_): With `useAdvanced` enabled, enabling this option carries the `data/payload` field from the access token over to the session token, allowing access to opaque data for log analysis for a URL protected by a session token.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.ip" >

- `ip` (_boolean_): With `useAdvanced` enabled, enabling this restricts content access to a specific IP address, only appropriate if it does not change during the playback session.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.acl" >

- `acl` (_boolean_): With `useAdvanced` enabled, enabling this option carries the `ACL` field from the access token over to the session token, to limit the requesting client's access to the specific URL or path set in the `ACL` field. Playback may fail if the base path of the master playlist (and variant playlist, plus segments) varies from that of the `ACL` field.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.enableTokenInURI" >

- `enableTokenInURI` (_boolean_): When enabled, passes tokens in HLS variant manifest URLs and HLS segment URLs, as an alternative to cookies.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.hlsMasterManifestFiles" >

- `hlsMasterManifestFiles` (_array of string values_): With `enableTokenInURI` enabled, specifies the set of filenames that form HLS master manifest URLs. You can use `*` wildcard characters, but make sure to specify master manifest filenames uniquely, to distinguish them from variant manifest files.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.tokenRevocationEnabled" >

- `tokenRevocationEnabled` (_boolean_): Enable this to deny requests from playback URLs that contain a `TokenAuth` token that uses specific token identifiers.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.blackListName" >

- `blackListName` (_string_): With `tokenRevocationEnabled` on, this selects the blacklist that contains the `TokenAuth` token identifiers to block from accessing your content.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.hlsMediaEncryption" >

- `hlsMediaEncryption` (_boolean_): Enables HLS Segment Encryption.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.encryptionMode" >

- `encryptionMode` (_enum string_): With `hlsMediaEncryption` enabled, specifies the encryption algorithm, the only valid value for which is `AES128`.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.useAdvancedOption" >

- `useAdvancedOption` (_boolean_): With `hlsMediaEncryption` enabled, allows you to use advanced encryption options.

</div>

<div class="option" markdown="1" id="segmentedContentProtection.iv" >

- `iv` (_string_): With `hlsMediaEncryption` and `useAdvancedOption` both enabled, this specifies the initialization vector used to generate the encryption key.

</div>

</div>

<div class="feature" data-feature="segmentedMediaOptimization" markdown="1">
