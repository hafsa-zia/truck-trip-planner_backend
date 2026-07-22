import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ORS_API_KEY")

def get_coordinates(place):

    url = "https://api.openrouteservice.org/geocode/search"

    params = {
        "api_key": API_KEY,
        "text": place
    }

    response = requests.get(url, params=params)

    data = response.json()

    coordinates = data["features"][0]["geometry"]["coordinates"]

    return coordinates

def get_route_data(
    current,
    pickup,
    dropoff
):

    current_coords = get_coordinates(current)
    pickup_coords = get_coordinates(pickup)
    dropoff_coords = get_coordinates(dropoff)

    url = "https://api.openrouteservice.org/v2/directions/driving-hgv"

    headers = {
        "Authorization": API_KEY
    }

    body = {
        "coordinates": [
            current_coords,
            pickup_coords,
            dropoff_coords
        ]
    }

    response = requests.post(
        url,
        json=body,
        headers=headers
    )

    data = response.json()

    summary = data["routes"][0]["summary"]

    return {
        "distance":
            round(summary["distance"] / 1609, 2),

        "duration":
            round(summary["duration"] / 3600, 2),

        "coordinates":
            data["routes"][0]["geometry"]
    }