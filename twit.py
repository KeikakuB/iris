#!/usr/bin/env python

import json
import fileinput

from twython import Twython

data = {}
with open('secret/secret.json') as f:
    data = json.load(f)
CONSUMER_KEY = data['twitter']['CONSUMER_KEY']
CONSUMER_SECRET = data['twitter']['CONSUMER_SECRET']
ACCESS_KEY = data['twitter']['ACCESS_KEY']
ACCESS_SECRET = data['twitter']['ACCESS_SECRET']
api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
lines = [l.strip() for l in fileinput.input()]
message = '\n'.join(lines)
api.update_status(status=message)
