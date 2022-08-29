import json
import requests
import pandas as pd

with open("key.json", "r") as f:
    key = json.load(f)["KEY"]

state = "26"

# Don't recall what data this refers to.
url = f"https://api.census.gov/data/2019/pep/charage?get=NAME,POP,AGE,AGE_DESC&for=state:{state}&key={key}"

# Decenial census (hardly any good info out yet) 
url = f"https://api.census.gov/data/2020/dec/pes?get=NAME,C_RRUS_COL1_R1&for=state:*&key={key}"

# American community survey 
url = f"https://api.census.gov/data/2020/acs/acs5?get=NAME,group(B17001A)&for=state:26&key={key}"

# Using zip code tabulation area
codes = [
    "B17001_028E", #Female v
    "B17001_029E",
    "B17001_030E",
    "B17001_014E", #Male v
    "B17001_015E",
    "B17001_016E",
]

code_str = ",".join(codes)

base_url = "https://api.census.gov/data"
year = "/2020"
product = "/acs/acs5"
query = f"?get=NAME,{code_str}&for=zip%20code%20tabulation%20area:*&key={key}"

url = "".join([base_url, year, product, query])

response = requests.request("GET", url)
header, *data = json.loads(response.text)
df = pd.DataFrame(data, columns=header)
df.to_csv("12_mo_poverty.csv")

code_str = "S0101_C01_001E"

base_url = "https://api.census.gov/data"
year = "/2020"
product = "/acs/acs5/subject"
query = f"?get=NAME,{code_str}&for=zip%20code%20tabulation%20area:*&key={key}"

url = "".join([base_url, year, product, query])

response = requests.request("GET", url)
header, *data = json.loads(response.text)
df = pd.DataFrame(data, columns=header)
# df.to_csv("full_pop_zip.csv")

codes = [
    "S0101_C01_001E",
    "S0102_C01_028E",
    "S0102_C01_029E",
    "S0102_C01_030E",
    "S0102_C01_031E",
    "S0103_C02_084E",
    "S0103_C02_085E",
    "S0103_C02_086E",
]

code_str = ",".join(codes)

# query for zips -> query = f"?get=NAME,{code_str}&for=zip%20code%20tabulation%20area:*&key={key}"

base_url = "https://api.census.gov/data"
year = "/2020"
product = "/acs/acs5/subject"
query = f"?get=NAME,{code_str}&for=metropolitan%20statistical%20area/micropolitan%20statistical%20area:19820&key={key}"

url = "".join([base_url, year, product, query])

response = requests.request("GET", url)
header, *data = json.loads(response.text)
df = pd.DataFrame(data, columns=header)
df.to_csv("data/test_tract.csv")
