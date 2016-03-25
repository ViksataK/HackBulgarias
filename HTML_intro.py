import requests
import json


r = requests.get('http://astral.hacksoft.io/api/airline/')
airports = r.json()
c = requests.get('http://data.okfn.org/data/core/country-list/r/data.json')
countries = c.json()
result = {c['Name']: 0 for c in countries}
darjavi = {c['Code']: c['Name'] for c in countries}
for a in airports:
    # result[darjavi[a['country_code']]] != 'UK':
    if a['country_code'] != 'UK':
        result[darjavi[a['country_code']]] += 1
    else:
        result['United Kingdom'] += 1
with open('asd.json', 'w') as f:
    json.dump(result, f, sort_keys=True, indent=4)
