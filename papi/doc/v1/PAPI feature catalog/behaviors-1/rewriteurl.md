---
title: "rewriteUrl"
slug: "rewriteurl"
hidden: false
createdAt: "2020-06-15T21:56:18.732Z"
updatedAt: "2020-06-15T21:56:18.732Z"
---
__Property Manager name__: [Modify Outgoing Request Path](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0077)

Modifies the path of incoming requests to forward to the origin. This helps you offload URL-rewriting tasks to the edge to increase the origin server's performance, allows you to redirect links to different targets without changing markup, and hides your original directory structure.

Except for regular expression replacements, this behavior manipulates _path expressions_, which start and end with a `/` character.

__Options__:

<div class="option" markdown="1" id="rewriteUrl.behavior" >

- `behavior` (_enum string_): The action to perform on the path:

    - If set to `PREPEND`, specify the `targetPathPrepend`. For     example, if set to `/prefix/`, `/path1/page.html` changes to     `/prefix/path1/page.html`.

    - If set to `REPLACE`, specify the `match` and `targetPath`. For     example, a `match` of `/path1/` and a `targetPath` of     `/path1/path2/` changes `/path1/page.html` to     `/path1/path2/page.html`.

    - If set to `REGEX_REPLACE`, specify the `matchRegex` and     `targetRegex`. For example, specifying `logo\\.(png|gif|jpe?g)`     and `brand\$1` changes `logo.png` to `brand.png`.

    - If set to `REWRITE`, specify the `targetUrl`. For example, you     can direct traffic to `/error/restricted.html`.

    - If set to `REMOVE`, specify the `match`. For example, a     `match` of `/path2/` changes `/path1/path2/page.html` to     `/path1/page.html`.

</div>

<div class="option" markdown="1" id="rewriteUrl.match" >

- `match` (_string_): When `behavior` is `REMOVE` or `REPLACE`, specifies the part of the incoming path you'd like to remove or modify.

</div>

<div class="option" markdown="1" id="rewriteUrl.matchRegex" >

- `matchRegex` (_string_): When `behavior` is set to `REGEX_REPLACE`, specifies the Perl-compatible regular expression to replace with `targetRegex`.

</div>

<div class="option" markdown="1" id="rewriteUrl.targetRegex" >

- `targetRegex` (_string; allows [variables](#vf)_): When `behavior` is set to `REGEX_REPLACE`, this replaces whatever the `matchRegex` field matches, along with any captured sequences from `\$1` through `\$9`.

</div>

<div class="option" markdown="1" id="rewriteUrl.targetPath" >

- `targetPath` (_string; allows [variables](#vf)_): When `behavior` is set to `REPLACE`, this path replaces whatever the `match` field matches in the incoming request's path.

</div>

<div class="option" markdown="1" id="rewriteUrl.targetPathPrepend" >

- `targetPathPrepend` (_string; allows [variables](#vf)_): When `behavior` is set to `PREPEND`, specifies a path to prepend to the incoming request's URL.

</div>

<div class="option" markdown="1" id="rewriteUrl.targetUrl" >

- `targetUrl` (_string; allows [variables](#vf)_): When `behavior` is set to `REWRITE`, specifies the full path to request from the origin.

</div>

<div class="option" markdown="1" id="rewriteUrl.matchMultiple" >

- `matchMultiple` (_boolean_): When enabled, replaces all potential matches rather than only the first.

</div>

<div class="option" markdown="1" id="rewriteUrl.keepQueryString" >

- `keepQueryString` (_boolean_): When enabled, retains the original path's query parameters.

</div>

</div>

<div class="feature" data-feature="rmaOptimization" markdown="1">
