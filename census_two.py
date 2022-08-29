import json
import pandas as pd

with open("zips.json", "r") as f:
    zips = json.load(f)

df = pd.read_csv("12_mo_poverty.csv")

codes = [
    "B17001_028E",  # Female v
    "B17001_029E",
    "B17001_030E",
    "B17001_014E",  # Male v
    "B17001_015E",
    "B17001_016E"
]

df["below poverty over 55"] = df[codes].sum(axis=1)
df["ZIP"] = df["NAME"].str.split(expand=True)[1]

service_area = df[df["ZIP"].isin(zips)]

service_area[["ZIP", "below poverty over 55"]].sort_values(
    "below poverty over 55", ascending=False
).to_csv("below_poverty_over_55.csv")
print(
    service_area[["ZIP", "below poverty over 55"]].sort_values(
        "below poverty over 55", ascending=False
    )
)
print(service_area["below poverty over 55"].sum())

df = pd.read_csv("full_pop_zip.csv")
df["ZIP"] = df["NAME"].str.split(expand=True)[1]
service_area = df[df["ZIP"].isin(zips)]

print(
    service_area[["ZIP", "S0101_C01_001E"]].sort_values(
        "S0101_C01_001E", ascending=False
    )
)
print(sum(service_area["S0101_C01_001E"]))
