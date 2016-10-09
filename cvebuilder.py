import json
from pprint import pprint
cves=[]
with open('cveWindow.json') as data_file:
    data = json.load(data_file)
    for d in data:
        cves.append(str(d['cve']))
print cves
