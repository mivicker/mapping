import json

with open("zips.json", "r") as f:
    zips_in_service_area = json.loads(f.read())

with open("zips_in_cbsa.json", "r") as f:
    zips_in_cbsa = json.loads(f.read())

print("In cbsa, not in service area")
print([ZIP for ZIP in zips_in_cbsa if ZIP not in zips_in_service_area])
print("In service area, not in cbsa")
print([ZIP for ZIP in zips_in_service_area if ZIP not in zips_in_cbsa])
