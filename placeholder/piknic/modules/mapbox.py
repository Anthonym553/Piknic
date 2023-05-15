import os
import requests
from dotenv import load_dotenv
load_dotenv()

MAPBOX_KEY = os.getenv("MAPBOX_KEY")

# Get the locations of food places within a certain radius of a given location
def get_locations(Lat: float, Lng: float, Radius: int) -> list[dict]:
    # Replace MAPBOX_KEY with your Bing Maps API key
    BING_MAPS_KEY = "AqLuCb-O4yrulO_OTvCPhEg3glzF8_eJwiufA4dC2BynKbsZv6GQ75rPYG1C3Caj"

    # Construct the URL for the Bing Maps REST API search query
    url = f"https://dev.virtualearth.net/REST/v1/LocalSearch?query=food&userLocation={Lat},{Lng}&maxRes=8&radius={Radius}&key={BING_MAPS_KEY}"

    # Send the request and get the response from the Bing Maps REST API
    result = requests.get(url).json()

    # Return a list of dictionaries containing information about the food locations found
    ret = [{
        "name": place["name"],
        "location": [place["point"]["coordinates"][1], place["point"]["coordinates"][0]],
        "address": place["Address"]["formattedAddress"],
        "category": place["Website"]
    } for place in result["resourceSets"][0]["resources"]]
    return ret


if __name__ == "__main__":
    test = get_locations(-77.3665, 35.6069, 1000)
    print(test)
