---
title: "Built-in system variables"
slug: "built-in-system-variables"
hidden: false
createdAt: "2020-06-05T17:22:03.359Z"
updatedAt: "2020-06-05T17:22:03.359Z"
---
This table lists all the built-in system variables available to you.
For any of these items that are optional, such as filename extensions,
the inserted variable may yield a blank string. Note that the `AKA`
prefix for the first variable listed varies from all others.

| Name | Description |
| :--- | :--- |
| `AKA_PM_CACHEABLE_OBJECT` | Either `true` if the requested object is cacheable, or `false` if not. |
| `AK_BASE_URL` | The incoming request's URL path, without filename and extension. |
| `AK_CLIENT_IP` | Client IP address as seen by the Akamai server, possibly overridden by `X-Forwarded-For` or `Akamai-Client-IP` request headers. |
| `AK_CLIENT_REAL_IP` | The client IP address as seen by the Akamai server, ignoring any request headers. |
| `AK_CLIENT_RTT` | Milliseconds elapsed for the TCP round-trip (RTT) between client and edge server. |
| `AK_CLIENT_TRANSFER_TIME` | Milliseconds elapsed to transfer content from edge to client. This value is only available after the client response completes. Applies only to [custom log fields]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#report.customLogField). |
| `AK_CLIENT_TURNAROUND_TIME` | Milliseconds elapsed for the combined initial request (`AK_CLIENT_RTT`) plus the response's transfer time (`AK_CLIENT_TRANSFER_TIME`). This value is only available after the client response completes. Applies only to [custom log fields]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#report.customLogField). |
| `AK_CONNECTED_CLIENT_IP` | The IP on the TCP socket, either client or a redirecting ghost. |
| `AK_CPCODE` | The CP code assigned to the request. |
| `AK_CURRENT_TIME` | The epoch time when edge metadata is applied to the request. If necessary, use the [`setVariable`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#setvariable) behavior to convert epoch time values to other time formats. |
| `AK_DOMAIN` | The hostname without the initial subdomain, such as `example.com` when requesting `www.example.com`. |
| `AK_EXTENSION` | The filename extension of the incoming request. |
| `AK_FILENAME` | The complete filename of the incoming request. |
| `AK_FIREWALL_ALERTED_RULES` | With [`webApplicationFirewall`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#webapplicationfirewall) enabled, a colon-separated list of IDs for firewall rules that triggered an alert for the current request. |
| `AK_FIREWALL_DENY_RULEID` | With [`webApplicationFirewall`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#webapplicationfirewall) enabled, the ID for a firewall rule set to `deny` the request when the rule triggers. |
| `AK_FIREWALL_DETECTED_RULES` | With [`webApplicationFirewall`]({{base.url}}/{{page.language}}/api/core_features/property_manager/vlatest.html#webapplicationfirewall) enabled, a colon-separated list of IDs for all firewall rules that apply to the request. |
| `AK_FIREWALL_MITIGATED_RULES` | A colon-separated list of IDs for firewall rules that were mitigated for the current request. |
| `AK_FIREWALL_TRIGGERED_RULES` | A colon-separated list of IDs for firewall rules that were triggered for the current request. |
| `AK_GHOST_IP` | The IP address on which end client requests are received, and ultimately resolve for the end user. |
| `AK_GHOST_SERVICE_IP` | The edge server IP address used to forward a request, also commonly known as the _machine IP_. This is the IP address the origin server sees as the client IP when it receives a request from the edge. |
| `AK_HOST_CNAME_CHAIN` | A space-delimited list of the CNAME chain provided by DNS lookup on the incoming `Host` header. |
| `AK_HOST` | The incoming request's hostname. |
| `AK_MAPRULE` | The maprule for the incoming request, such as `a123.g.akamai.net`. |
| `AK_METHOD` | The request method, such as `GET`, `PUT`, `POST`, or `HEAD`. |
| `AK_ORIGINAL_URL` | The original URL before any processing by Akamai Edge servers. |
| `AK_ORIGIN_DNS_NAME` | The hostname the Akamai server resolved to go forward to the origin. |
| `AK_PATH` | The original URL path as seen by the Akamai Edge server. |
| `AK_PROTOCOL_NEGOTIATION` | The protocol negotiated with the client when NPN or ALPN is in use. Under HTTP, possible values are `http/1.1` or `http/1.0`. For HTTP2, values are `h2-14` or `h2`. For SPDY, values are `spdy/3.1`, `spdy/3` or `spdy/2`. |
| `AK_QUERY` | The URL's entire query string. |
| `AK_REQUEST_ID` | Unique identifier for each request on the edge server, the same as reported in logs. |
| `AK_SCHEME` | The request scheme, either `http` or `https`. |
| `AK_SLOT` | The incoming request's slot number. |
| `AK_TLS_CIPHER_NAME` | For HTTPS and SPDY requests, specifies the name of the cipher used for the SSL connection, otherwise `NO-CIPHER` for HTTP requests. |
| `AK_TLS_ENCRYPTION_BITS` | Bits of encryption used for the request. |
| `AK_TLS_PREFERRED_CIPHERS` | The value of the request's `security:essl.slot-assignment.preferred-ciphers` tag. |
| `AK_TLS_SNI_NAME` | The SNI name submitted by the client. |
| `AK_TLS_VERSION` | The TLS version used for the connection. |
| `AK_URL` | The incoming request's entire URL. |