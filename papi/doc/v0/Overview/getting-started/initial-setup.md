---
title: "Initial setup"
slug: "initial-setup"
hidden: false
createdAt: "2020-06-05T16:00:28.234Z"
updatedAt: "2020-06-05T20:42:18.413Z"
---
Before using PAPI for the first time:

- Review [Get Started with APIs]({{base.url}}/{{page.language}}/learn_akamai/getting_started_with_akamai_d\
evelopers/developer_tools/getstartedapis.html)
for details on how to set up client tokens to access any Akamai API.
These tokens appear as custom hostnames that look like this:
`https://akzz-XXXXXXXXXXXXXXXX-XXXXXXXXXXXXXXXX.luna.akamaiapis.net`.

- If you need to perform bulk search operations across many accounts,
there's a different procedure to set up your client token.  For
details, see [Manage many accounts with one API
client]({{base.url}}/{{page.language}}/learn_akamai/getting_started_with_akamai\
_developers/developer_tools/accountSwitch.html).

- To enable this API, choose the API service named __Property
Manager__ and set the access level to __READ-WRITE__.

- Once you have a custom domain token, you can gather other
prerequisite data used throughout the API: the relevant
[contract](#getcontracts) and [group](#getgroups) to access other PAPI
objects, and a [product](#getproducts) to create new ones. See the
[API summary](#apisummary) for PAPI's full range of capabilities.

- Client tools such as
[edgegrid-curl](https://github.com/akamai-open/edgegrid-curl) and
[edgegrid-python](https://github.com/akamai-open/AkamaiOPEN-edgegrid-python)
assume a maximum message body size of 2048 bytes, which for PAPI needs
to increase to 128K. How you do so depends on your chosen tool, for
example by setting `max-body:131072` in the `.egcurl` file, or in
python by passing in `max_body:131072` as part of the `EdgeGridAuth()`
call.

- Review the API's [Known issues](#knownissues).

- Get help from the
[Akamai developer community](https://developer.akamai.com/community)
and provide feedback. You can also contact your Akamai representative
for support. We want to hear from you!