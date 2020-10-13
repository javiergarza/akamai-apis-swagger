---
title: "Property hostname errors"
slug: "property-hostname-errors"
hidden: false
createdAt: "2020-06-05T21:17:18.526Z"
updatedAt: "2020-06-10T03:12:18.728Z"
---
| Code | Type | Problem |
| :--- | :--- | :--- |
| [400](https://httpstatuses.com/400) | `property-version-hostname/bad-cnameto` | The `cnameTo` value references an edge hostname that doesn't exist. |
| [400](https://httpstatuses.com/400) | `property-version-hostname/edgehostname-mismatch` | You supplied both a `cnameTo` and `edgeHostnameId` that reference different hostnames. [Learn more](#putpropertyversionhostnames). |
| [400](https://httpstatuses.com/400) | `property-version-hostname/missing-cnameto-or-edgehostnameid` | You need to specify either a `cnameTo` or a `edgeHostnameId` member. [Learn more](#putpropertyversionhostnames). |
| [501](https://httpstatuses.com/501) | `property-version-hostname/unsupported-cnametype` | You can only specify a property hostname whose `cnameType` is `EDGE_HOSTNAME`. [Learn more](#putpropertyversionhostnames). |

An additional set of errors may be listed within [Hostname](#hostname) objects that prevent you from activating the property version:

| Type | Description |
| :--- | :--- |
| `generic_behavior_issue.origin_name_hostname_overlap` | An origin may not specify the same hostname as a property. |
| `hostnames.bad_hostname_format` | The hostname isn't formatted properly. |
| `hostnames.disallowed_akamaihd_dot_net_hostname` | The AkamaiHD hostname is invalid. The prefix for `a.akamaihd.net` has a maximum 16 alphanumeric and underscore characters. |
| `hostnames.disallowed_akamaized_dot_net_hostname` | The hostname may not specify `akamaized.net`. |
| `hostnames.dualstack_dissuasion_warning` | Make sure your origin can handle IPv6 traffic. |
| `hostnames.duplicate_hostname` | The hostname is listed more than once. |
| `hostnames.empty_hostnames` | Specify at least one property hostname. |
| `hostnames.empty_string_hostname` | The hostname may not be empty. |
| `hostnames.enhancedtls_module_standard_cert` | Your contract features the Enhanced TLS module, but the property hostname uses a standard certificate, a potential PCI violation. |
| `hostnames.hostname_contains_underscore` | Avoid underscore characters in hostnames, which may cause problems for some DNS resolvers. |
| `hostnames.hostname_overlapping_certs` | Some domains are covered by both Enhanced TLS and Standard TLS certificates. Avoid this unless you're migrating properties. |
| `hostnames.insecure_module_standard_cert` | Your contract requires the Standard TLS module to select a hostname with a standard certificate. |
| `hostnames.insecure_property_secure_edge_hostname` | An Enhanced TLS edge hostname is incompatible with your non-secure property. |
| `hostnames.max_hostnames_limit_hard` | You have reached the maximum number of hostnames per property. Either reconfigure using the [`instantConfig`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#instantconfig) behavior, split your hostnames across more than one property, or consult with your account representative. |
| `hostnames.max_hostnames_limit_soft` | You have exceeded the optimal number of hostnames per property. Either reconfigure using the [`instantConfig`](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#instantconfig) behavior, split your hostnames across more than one property, or consult with your account representative. |
| `hostnames.mdc_subdomain_prefix` | The hostname is formatted incorrectly, and can't begin with a hyphen. |
| `hostnames.missing_edgehostname` | A property hostname needs to reference a corresponding edge hostname. |
| `hostnames.non_enhancedtls_module_enhanced_cert` | Your contract requires the Enhanced TLS module to select a hostname with an enhanced certificate. |
| `hostnames.secure_property_insecure_edge_hostname` | A Standard TLS edge hostname is incompatible with your secure property. |
| `hostnames.secure_property_insecure_edge_hostname_shared_cert` | An edge hostname is incompatible with your secure property. |
| `hostnames.secure_property_without_secure_modules` | Your contract requires secure modules to deploy a secure property. |
| `hostnames.shared_cert_subdomain_prefix` | The hostname is formatted incorrectly, and can't begin with a hyphen. |
| `hostnames.unknown_edge_hostname` | The edge hostname is unavailable, and may not exist. |