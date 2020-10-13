---
title: "responseCode"
slug: "responsecode"
hidden: false
createdAt: "2020-06-15T21:54:36.187Z"
updatedAt: "2020-06-15T21:54:36.187Z"
---
__Property Manager name__: [Set Response Code](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0075)

Change the existing response code. For example, if your origin sends a `301` permanent redirect, this behavior can change it on the edge to a temporary `302` redirect.

__Options__:

<div class="option" markdown="1" id="responseCode.statusCode" >

- `statusCode` (_numeric enum_): The HTTP status code to replace the existing one, any of the following:

<pre style="-webkit-column-width:1in;-moz-column-width:1in;column-width:1in;margin-left:3pc">
100
101
102
103
122
200
201
202
203
204
205
206
207
226
300
301
302
303
304
305
306
307
308
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
422
423
424
425
426
428
429
431
444
449
450
499
500
501
502
503
504
505
506
507
509
510
511
598
599
</pre>

</div>

<div class="option" markdown="1" id="responseCode.override206" >

- `override206` (_boolean_): When enabled, allows any specified `200` success code to override a `206` partial-content code, in which case the response's content length matches the requested range length.

</div>

</div>

<div class="feature" data-feature="responseCookie" markdown="1">
