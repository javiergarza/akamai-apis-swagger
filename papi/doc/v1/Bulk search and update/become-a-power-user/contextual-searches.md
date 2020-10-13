---
title: "Contextual searches"
slug: "contextual-searches"
hidden: false
createdAt: "2020-06-05T18:10:56.316Z"
updatedAt: "2020-06-10T03:30:47.189Z"
---
The [Sample bulk updates](#samplebulkupdates) section briefly summarizes some of the PAPI behaviors you may want to search for in your configuration.  This section provides a fuller set of examples showing different techniques to help refine your search.

Examples in the table below demonstrate how to restrict matches to [top-level default rules](#cxloc), child rules, or match based on nearby [criteria or behaviors](#cxrel).  It shows how to match or exclude [string values](#cxstr), pattern-match a regular expression, or test [boolean](#cxbool), [numeric](#cxnum), or [array](#cxarr) values.

The additional section on [Possible mismatches](#matcherr) provides further guidance on potential conceptual errors to help you avoid matching content incorrectly.

| Match | JSONPath syntax |
| :--- | :--- |
| <b id="cxloc">Location within rules</b> ||
| [Origin](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#origin) hostname in top-level default rule. | `$.behaviors[?(@.name == 'origin')].options.hostname` |
| Origin hostname in any rule. | `$..behaviors[?(@.name == 'origin')].options.hostname` |
| Origin hostname, only in child rules. | `$..children[*].behaviors[?(@.name == 'origin')].options.hostname` |
| <b id="cxbool">Boolean values</b> ||
| Toggle [HTTP/2](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#edgeredirector), when either enabled or disabled. | `$..behaviors[?(@.name == 'http2')].options.enabled` |
| [Edge Redirector](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#edgeredirector), disabled. | `$..behaviors[?(@.name == 'edgeRedirector')].options[?(@.enabled == false)].enabled` |
| Edge Redirector, enabled. | `$..behaviors[?(@.name == 'edgeRedirector')].options[?(@.enabled == true)].enabled` |
| [Forward Rewrite](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#forwardrewrite) or Edge Redirector, enabled or disabled. | `$..behaviors[?(@.name == 'forwardRewrite' || @.name == 'edgeRedirector')].options.enabled` |
| <b id="cxstr">String values</b> ||
| [Origin](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#origin) hostname of `www.example.com`. | `$..behaviors[?(@.name == 'origin')].options[?(@.hostname == 'www.example.com')].hostname` |
| Any origin hostname that matches an `example.com` substring. | `$..behaviors[?(@.name == 'origin')].options[?(@.hostname =~ /example.com/)].hostname` |
| Any origin hostname that starts with `www.` and ends `.com`. | `$..behaviors[?(@.name == 'origin')].options[?(@.hostname =~ /www\..*\.com/)].hostname` |
| Default [caching](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#caching) TTL. | `$..behaviors[?(@.name == 'caching')].options.defaultTtl` |
| Same, but cached 1 to 9 hours. | `$..behaviors[?(@.name == 'caching' && @.options.defaultTtl =~ /^[1-9]h$/)].options.defaultTtl` |
| <b id="cxnum">Numeric values</b> ||
| Any [response code](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#responsecode). | `$..behaviors[?(@.name == 'responseCode')].options.statusCode` |
| Response code is 200. | `$..behaviors[?(@.name == 'responseCode')].options[?(@.statusCode == 200)].statusCode` |
| Error response codes. | `$..behaviors[?(@.name == 'responseCode')].options[?(@.statusCode >= 400)].statusCode` |
| Redirect responses in 3xx range. | `$..behaviors[?(@.name == 'responseCode')].options[?(@.statusCode >= 300 && @.statusCode < 400)].statusCode` |
| <b id="cxarr">Array values</b> ||
| [Path](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#path) criteria match that includes `/catalog`. | `$..criteria[?(@.name == 'path')].options.value[?(@ == '/catalog')]` |
| All path match values except `/catalog`. | `$..criteria[?(@.name == 'path')].options.value[?(@ != '/catalog')]` |
| All path match values. | `$..criteria[?(@.name == 'path')].options.value[*]` |
| First path match value. | `$..criteria[?(@.name == 'path')].options.value[0]` |
| Last path match value. | `$..criteria[?(@.name == 'path')].options.value[-1]` |
| Any `/catalog` path value in the same set as an `/about` value. | `$..criteria[?(@.name == 'path')].options[?('/about' in @.value)].value[?(@ == '/catalog')]` |
| Any `/catalog` path value where `/blog` isn't in the same set. | `$..criteria[?(@.name == 'path')].options[?('/blog' nin @.value)].value[?(@ == '/catalog')]` |
| Specific set of path values. | `$..criteria[?(@.name == 'path')].options.value[?(@ == '/catalog' || @ == '/about')]` |
| <b id="cxrel">Relative location</b> ||
| Toggle [Image Manager](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#imagemanager) within any rule with `image` in its name. | `$..children[?(@.name =~ /[Ii]mage/)].behaviors[?(@.name == 'imageManager')].options.enabled` |
| Toggle a `matchWildcard` option within a `contentType` match that enables a `gzipResponse` behavior. | `$.[?(@.criteria.[?(@.name == 'contentType')] && @.behaviors.[?(@.name == 'gzipResponse')])].criteria[?(@.name == 'contentType')].options.matchWildcard` |
| Set the [Downstream Cacheability](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#downstreamcache) behavior when triggered by a [Response Cacheability](https://learn.akamai.com/en-us/api/core_features/property_manager/vlatest.html#cacheability) criteria match. | `$..children[?(@.criteria[?(@.name == 'cacheability')] && @.behaviors[?(@.name == 'downstreamCache')] )].behaviors[?(@.name == 'downstreamCache')].options.behavior` |