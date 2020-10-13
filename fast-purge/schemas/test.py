import jsonschema
from pdb import set_trace
import json

# with open('CPCodeRequest.json') as fh:
with open('UrlRequest.json') as fh:
    schema = json.loads(fh.read())

data = {'objects': ['111', '222']}

jsonschema.validate(data, schema)
set_trace()
