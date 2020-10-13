---
title: "Possible mismatches"
slug: "possible-mismatches"
hidden: false
createdAt: "2020-06-05T18:13:14.118Z"
updatedAt: "2020-06-10T03:12:14.132Z"
---
This section summarizes potential errors you may encounter when crafting search queries. Unlike more obvious JSONPath parse errors for which you receive an explicit error response, these conceptual errors may result either in an empty set of search results, or far more search results than you intend:

- __Testing a location vs. its value__. The first expression below matches all origin hostname values. If you want to change a specific value, make sure to specify it, as in the second expression. Otherwise the range of your search results and subsequent patch operation may be wider than you intend:

        $..behaviors[?(@.name == 'origin')].options.hostname
        $..behaviors[?(@.name == 'origin')].options[?(@.hostname == 'old.example.com')].hostname

- __Testing existence vs. truth__. The first match expression below tests whether the `enabled` option exists, not as a shorthand for whether it evaluates as boolean `true` as in many programming environments. Like the second match expression, it matches both `true` and `false` values, likely a wider match than intended. Use the third type of expression to refine the test to specify a `true` value:

        $..behaviors[?(@.name == 'http2'].options[?(@.enabled)].enabled
        $..behaviors[?(@.name == 'http2'].options.enabled
        $..behaviors[?(@.name == 'http2'].options[?(@.enabled == true)].enabled

- __Mismatching type__. The data type of any value you're trying to match needs to be the same as the one in the rule configuration. This example yields no results because it matches a `'true'` string value rather than a `true` boolean value:

        $..behaviors[?(@.name == 'http2')].options[?(@.enabled == 'true')].enabled

- __Mismatching case__. String matches and regular expression tests are case-sensitive. The first match below yields no data because the behavior is named `cpCode`, not `cpcode`. The second pattern match yields either name, in case you're not sure:

        $..behaviors[?(@.name == 'cpcode'].options.value.id
        $..behaviors[?(@.name =~ /cp[Cc]ode/].options.value.id

- __Object values__. PAPI's implementation of JSONPath doesn't allow you to test an object's scalar value directly on the matched node. The first match below fails, but the second succeeds:

        $.behaviors[?(@.name == 'origin')].options.hostname[?(@ == 'old.example.com')]
        $.behaviors[?(@.name == 'origin')].options[?(@.hostname == 'old.example.com')].hostname

- __Matches execute within rules__. All JSONPath matches execute within a configuration's set of `rules`, not the outermost object from the [Get a rule tree](#getpropertyversionrules) JSON response. This example fails to match the top-level `default` rule, because the expression's initial `rules` segment is unnecessary:

        $.rules.behaviors[?(@.name == 'origin')].options.hostname[?(@ == 'old.example.com')]

    Note that although you don't specify `rules` at the start of your
    bulk search JSONPath query expression, the JSON Pointer search
    results still always include it as its first path segment:

        "matchLocations": [
            "/rules/behaviors/0/options/hostname"
        ]