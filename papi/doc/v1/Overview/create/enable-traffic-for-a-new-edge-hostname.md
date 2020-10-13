---
title: "Enable traffic for a new edge hostname"
slug: "enable-traffic-for-a-new-edge-hostname"
hidden: false
createdAt: "2020-06-05T16:35:33.064Z"
updatedAt: "2020-06-10T03:12:20.606Z"
---
After [creating a new edge hostname](#postedgehostnames), [assigning it to a property](#putpropertyversionhostnames), and [activating the property](#postpropertyactivations), you still need to modify your DNS configuration to direct the origin's traffic to the new edge hostname, for your content to serve out.

Edge hostnames are formed from the combined `domainPrefix` and `domainSuffix` included in the [POST request](#postedgehostnames), in this case `custom.example.com.edgesuite.net` to indicate standard HTTP traffic:

[block:code]
{
  "codes": [
    {
      "code": "{\n    \"productId\": \"prd_PPP\",\n    \"domainPrefix\": \"custom.example.com\",\n    \"domainSuffix\": \"edgesuite.net\",\n    \"secure\": true,\n    \"ipVersionBehavior\": \"IPV4\",\n    \"slotNumber\": 12345\n}",
      "language": "json"
    }
  ]
}
[/block]

(HTTPS typically uses an `edgekey.net` suffix.)  The POST request
tells Akamai's network of DNS servers to map it to local server names,
but for the hostname to ultimately activate, you need to update your
own DNS record to map your origin hostname to the edge hostname. A
resulting DNS resolution looks like this:

[block:code]
{
  "codes": [
    {
      "code": "$ host -v custom.example.com\nTrying \"custom.example.com\"\n;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 14682\n;; flags: qr aa rd ra; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 0\n\n;; QUESTION SECTION:\n;custom.example.com. IN      A\n\n;; ANSWER SECTION:\ncustom.example.com.     300     IN      CNAME   custom.example.com.edgekey.net.\ncustom.example.com.edgekey.net. 3701 IN CNAME   e79.x.akamaiedge.net.\ne79.x.akamaiedge.net.   11      IN      A       72.246.8.105\n",
      "language": "shell"
    }
  ]
}
[/block]

The first CNAME entry maps your `custom.example.com` domain to the `custom.example.com.edgekey.net` edge hostname, allowing traffic to flow to Akamai's edge servers. POSTing the new edge hostname implements the second CNAME, which in this case maps the edge hostname to the local `e79.x.akamaiedge.net` hostname, and in turn to a local IP address.