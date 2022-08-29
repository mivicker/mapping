import requests
import json
from census_key import HUD_TOKEN

"""
This script converts between various geographies using the HUD api.
"""

base_url = "https://www.huduser.gov/hudapi/public/usps"

# county-zip is type 7
# zip-tract

cbsa = "19820"

MI_fpis = "26"
five_counties = [
        "26163", # Wayne
        "26099", # Macomb
        "26093", # Livingston
        "26115", # Monroe
        "26125", # Oakland
]

headers = {
    "Authorization": f"Bearer {HUD_TOKEN}"
}

"""
# county zip
result = []
for county in five_counties:
    complete_url = base_url+f"?type=7&query={county}"
    r = requests.get(complete_url, headers=headers)

    data = json.loads(r.text)['data']
    new = [item['geoid'] for item in data['results']]
    result.extend(new)

with open("zips.json", "w") as f:
    f.write(json.dumps(result))

ZIPs = result
result = []
for ZIP in ZIPs:
    complete_url=base_url+f"?type=1&query={ZIP}"
    r = requests.get(complete_url, headers=headers)
    content = json.loads(r.text)
    try:
        data = content['data']
    except:
        print(content)
        continue
    new = [item['geoid'] for item in data['results']]
    result.extend(new)

with open("tracts.json", "w") as f:
    f.write(json.dumps(result))
"""
# cbsa -> zip is type 8
complete_url = base_url + f"?type=8&query={cbsa}"
r = requests.get(complete_url, headers=headers)

data = json.loads(r.text)['data']
zips = [item['geoid'] for item in data['results']]

with open("zips_in_cbsa.json", "w") as f:
    f.write(json.dumps(zips))
