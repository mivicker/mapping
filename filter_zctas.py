import json
import geopandas as gpd

with open("./zips.json") as f:
    zips = json.loads(f.read())

df = gpd.read_file("./zip-code-tabulation-area.json")

df[df["ZCTA5CE20"].isin(zips)].to_file("gleaners_zips.geojson", driver="GeoJSON")
