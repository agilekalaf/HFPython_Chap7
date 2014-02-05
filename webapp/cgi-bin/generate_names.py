#! /usr/local/bin/python3
__author__ = 'gjbelang'

import json
import athletemodel
import yate

names = athletemodel.get_names_from_store()

print(yate.start_response('application/json'))
print(json.dumps(sorted(names)))

