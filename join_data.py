import os
import pandas as pd
import geopandas as gpd

df = pd.read_csv("./data/BelowPovertyOver55.csv")
df["ZIP"] = df["ZIP"].astype("str")

geometry = gpd.read_file("./data/gleaners_zips.geojson")
geometry["NAME20"] = geometry["NAME20"].astype("str")

merged = geometry.merge(df, left_on="NAME20", right_on="ZIP")
merged.to_file("./data/merged_data.json", driver="GeoJSON")
