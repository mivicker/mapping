from collections.abc import Callable
import json
import urllib
import requests

"""
This very simple module allows for geocoding addresses while
using a basic json cache so we're not repeating calls.
"""

def file_cache(filename: str) -> Callable:
    """
    This saves all calls to geocoding service to a json file.
    """
    def decorator(geocoding_func: Callable) -> Callable:
        def check_func(address: str) -> str:
            with open(filename, "r+") as f:
                cache = json.load(f)
                try:
                    return cache[address]
                except:
                    result = geocoding_func(address)
                    cache[address] = result
                    f.seek(0)
                    json.dump(cache, f)
                    f.truncate()
                    return result
        return check_func
    return decorator


@file_cache("geocoded.json")
def geocode(address: str) -> tuple:
    """
    Given a street address, returns coordinates from OSM.
    """
    base_url = "https://nominatim.openstreetmap.org/"
    
    safe_address = urllib.parse.quote(address)
    query_template = f"search.php?q={safe_address}&format=jsonv2"

    response = requests.get(base_url + query_template)

    data = json.loads(response.content)

    return data[0]["lat"], data[0]["lon"]

