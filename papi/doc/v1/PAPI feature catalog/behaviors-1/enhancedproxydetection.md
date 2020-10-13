---
title: "enhancedProxyDetection"
slug: "enhancedproxydetection"
hidden: false
createdAt: "2020-06-15T21:22:48.746Z"
updatedAt: "2020-06-15T21:22:48.746Z"
---
__Property Manager name__: [Enhanced Proxy Detection with GeoGuard](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_5006)

This behavior allows you to apply proxy detection and location spoofing protection from Akamai's data provider, GeoGuard. Configure it to identify unwanted requests redirected from four types of proxy: anonymous VPN, public proxy, The Onion Router (Tor) exit node, and smart DNS proxy. Configure your edge content to deny or redirect requests, or allow them to pass through so that you can log and audit the traffic.

__Options__:

<div class="option" markdown="1" id="enhancedProxyDetection.enabled" >

- `enabled` (_boolean_): Applies GeoGuard proxy detection.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.enableConfigurationMode" >

- `enableConfigurationMode` (_enum string_): Sets either a default `BEST_PRACTICE` mode to apply a single action to the four different categories of traffic, or `ADVANCED` to configure them separately. Choose the latter only if you are thoroughly familiar in GeoGuard proxy detection.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.bestPracticeAction" >

- `bestPracticeAction` (_enum string_): With `enableConfigurationMode` set to `BEST_PRACTICE`, specifies whether to `ALLOW`, `DENY`, or `REDIRECT` the proxy request.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.bestPracticeRedirecturl" >

- `bestPracticeRedirecturl` (_string_): With `bestPracticeAction` set to `REDIRECT`, this specifies the URL to which to redirect requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectAnonymousVpn" >

- `detectAnonymousVpn` (_boolean_): With `enableConfigurationMode` set to `ADVANCED`, this enables detection of requests from anonymous VPNs.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectAnonymousVpnAction" >

- `detectAnonymousVpnAction` (_enum string_): With `detectAnonymousVpn` enabled, specifies whether to `ALLOW`, `DENY`, or `REDIRECT` anonymous VPN requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectAnonymousVpnRedirecturl" >

- `detectAnonymousVpnRedirecturl` (_string_): With `detectAnonymousVpnAction` set to `REDIRECT`, this specifies the URL to which to redirect anonymous VPN requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectPublicProxy" >

- `detectPublicProxy` (_boolean_): With `enableConfigurationMode` set to `ADVANCED`, this enables detection of requests from public proxies.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectPublicProxyAction" >

- `detectPublicProxyAction` (_enum string_): With `detectPublicProxy` enabled, specifies whether to `ALLOW`, `DENY`, or `REDIRECT` public proxy requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectPublicProxyRedirecturl" >

- `detectPublicProxyRedirecturl` (_string_): With `detectPublicProxyAction` set to `REDIRECT`, this specifies the URL to which to redirect public proxy requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectTorExitNode" >

- `detectTorExitNode` (_boolean_): With `enableConfigurationMode` set to `ADVANCED`, this enables detection of requests from Tor exit nodes.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectTorExitNodeAction" >

- `detectTorExitNodeAction` (_enum string_): With `detectTorExitNode` enabled, specifies whether to `DENY`, `ALLOW`, or `REDIRECT` requests from Tor exit nodes.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectTorExitNodeRedirecturl" >

- `detectTorExitNodeRedirecturl` (_string_): With `detectTorExitNodeAction` set to `REDIRECT`, this specifies the URL to which to redirect requests from Tor exit nodes.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectSmartDNSProxy" >

- `detectSmartDNSProxy` (_boolean_): With `enableConfigurationMode` set to `ADVANCED`, this enables detection of requests from smart DNS proxies.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectSmartDNSProxyAction" >

- `detectSmartDNSProxyAction` (_enum string_): With `detectSmartDNSProxy` enabled, specifies whether to `DENY`, `ALLOW`, or `REDIRECT` smart DNS proxy requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectSmartDNSProxyRedirecturl" >

- `detectSmartDNSProxyRedirecturl` (_string_): With `detectSmartDNSProxyAction` set to `REDIRECT`, this specifies the URL to which to redirect DNS proxy requests.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectVpnDataCenter" >

- `detectVpnDataCenter` (_boolean_): With `enableConfigurationMode` set to `ADVANCED`, this enables detection of requests from VPN data centers. You should learn more about this GeoGuard category before enabling it.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectVpnDataCenterAction" >

- `detectVpnDataCenterAction` (_enum string_): With `detectVpnDataCenter` enabled, specifies whether to `DENY`, `ALLOW`, or `REDIRECT` requests from VPN data centers.

</div>

<div class="option" markdown="1" id="enhancedProxyDetection.detectVpnDataCenterRedirecturl" >

- `detectVpnDataCenterRedirecturl` (_string_): With `detectVpnDataCenterAction` set to `REDIRECT`, this specifies the URL to which to redirect requests from VPN data centers. ...

</div>

</div>

<div class="feature" data-feature="failAction" markdown="1">
