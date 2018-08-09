#!/usr/bin/env python

import json
import os
import sys


OBJECT_EXPORT_DIR = sys.argv[1]

print(os.path.join(OBJECT_EXPORT_DIR, 'imagestreams.json'))

###############################################################################
# ImageStreams
###############################################################################

imagestreams = []
with open(os.path.join(OBJECT_EXPORT_DIR, 'imagestreams.json'), 'r') as f:
    imagestreams = json.load(f)

for imagestream in imagestreams['items']:
    if imagestream['metadata']['name'] == 'demo-app':
        for imagestream_tag in imagestream['spec']['tags']:
            if imagestream_tag['name'] == 'prod':
                imagestream_tag['from']['name'] = 'quay.io/jhocutt/demo-app:prod'

with open(os.path.join(OBJECT_EXPORT_DIR, 'imagestreams.json'), 'w') as f:
    f.write(json.dumps(imagestreams))

###############################################################################
# Routes
###############################################################################

routes = []
with open(os.path.join(OBJECT_EXPORT_DIR, 'routes.json'), 'r') as f:
    routes = json.load(f)

for route in routes['items']:
    route['spec']['host'] = ''

with open(os.path.join(OBJECT_EXPORT_DIR, 'routes.json'), 'w') as f:
    f.write(json.dumps(routes))