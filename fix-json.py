#!/usr/bin/python3
import json
import sys
filename = sys.argv[1]
with open(filename, 'r') as f:
    json_form = f.read()
structure = json.loads(json_form)
old_stdout = sys.stdout
sys.stdout = open('tmp.gd.json', 'w')
print(json.dumps(structure, indent = 4))
sys.stdout = old_stdout