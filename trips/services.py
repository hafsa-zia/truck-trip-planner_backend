import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEOAPIFY_API_KEY")

def get_coordinates(place):

    url = (
        f"https://api.geoapify.com/v1/geocode/search?"
        f"text={place}&apiKey={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    return data["features"][0]["geometry"]["coordinates"]

def get_route_data(current, pickup, dropoff):

    current_coords = get_coordinates(current)
    pickup_coords = get_coordinates(pickup)
    dropoff_coords = get_coordinates(dropoff)

    url = (
        "https://api.geoapify.com/v1/routing?"
        f"waypoints="
        f"{current_coords[1]},{current_coords[0]}|"
        f"{pickup_coords[1]},{pickup_coords[0]}|"
        f"{dropoff_coords[1]},{dropoff_coords[0]}"
        f"&mode=drive&apiKey={API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    route = data["features"][0]["properties"]

    return {
        "distance": round(route["distance"] / 1609, 2),
        "duration": round(route["time"] / 3600, 2),
        "coordinates": data["features"][0]["geometry"]["coordinates"]
    }