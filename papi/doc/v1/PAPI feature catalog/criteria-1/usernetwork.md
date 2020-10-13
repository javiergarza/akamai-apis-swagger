---
title: "userNetwork"
slug: "usernetwork"
hidden: false
createdAt: "2020-06-15T22:30:04.762Z"
updatedAt: "2020-06-15T22:30:04.762Z"
---
__Property Manager name__: [User Network Data](https://control.akamai.com/wh/CUSTOMER/AKAMAI/en-US/WEBHELP/property-manager/property-manager-help/csh_lookup.html?id=PM_0019)

Matches details of the network over which the request was made, determined by looking up the IP address in a database.

__Options__:

- `field` (_enum string_): The type of information to match, either `BANDWIDTH`, a specific `NETWORK`, or a more general `NETWORK_TYPE`.

- `matchOperator` (_enum string_): Matches the specified set of values when set to `IS_ONE_OF`, otherwise `IS_NOT_ONE_OF` reverses the match.

- `networkTypeValues` (_array of string values_): Specifies the basic type of network, either `CABLE`, `DIALUP`, `DSL`, `FIOS`, `ISDN`, `MOBILE`, or `UVERSE`.

- `networkValues` (_array of string values_): Any set of specific networks:

<pre style="-webkit-column-width:2in;-moz-column-width:2in;column-width:2in;margin-left:3pc">
airtel
alpha_internet
altitudetelecom
aol
arnet
asahi
att
bellcanada
biglobe
bitmailer
bouygues
brighthouse
bskyb
bt
cablevision
cernet
chinamobile
chinanet
chinaunicom
clearwire
colt
comcast
completel
compuserve
covad
dion
dreamnet
dtag
dti
earthlink
easynet
eurociber
fastweb
fibertel
francetelecom
free
freecom
h3g
hinet
ibm
idecnet
iij4u
infosphere
janet
jazztell
justnet
livedoor
mci
mediacom
mediaone
microsoft
mil
nerim
newnet
@nifty
numericable
ocn
odn
ono
panasonic-hi-ho
plala
plusnet
prodigy
qwest
rediris
renater
reserved
retevision
roadrunner
rogers
seednet
seikyo_internet
sfr
shaw
so-net
sprint
suddenlink
talktalk
telefonica
telstra
terramexico
ti
tikitiki
timewarner
tiscali
tmobile
turktelekom
uni2
uninet
upc
uunet
verizon
virginmedia
vodafone
wakwak
wind
windstream
zero
</pre>

- `bandwidthValues` (_array of string values_): Bandwidth range in bits per second, either `1`, `57`, `257`, `1000`, `2000`, or `5000`.

- `checkIps` (_enum string_): Specifies which IP addresses determine the user's network:

    - `CONNECTING` considers the connecting client's IP address.
    - `HEADERS` considers IP addresses specified in the     `X-Forwarded-For` header, succeeding if any of them match.
    - `BOTH` behaves like `HEADERS`, but also considers the connecting     client's IP address.

- `useOnlyFirstXForwardedForIp` (_boolean_): When connecting via a proxy server as determined by the `X-Forwarded-For` header, enabling this option matches the end client specified in the header. Disabling it matches the connecting client's IP address.
