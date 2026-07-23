import math


def calculate_hos(distance, duration, cycle_hours):

    remaining_hours = duration
    remaining_distance = distance

    day = 1

    stops = []

    # Pickup
    stops.append({
        "day": day,
        "type": "Pickup",
        "duration": 1
    })

    fuel_counter = 0

    while remaining_hours > 0:

        driving_today = min(11, remaining_hours)

        stops.append({
            "day": day,
            "type": "Driving",
            "duration": round(driving_today, 2)
        })

        if driving_today >= 8:

            stops.append({
                "day": day,
                "type": "30 Minute Break",
                "duration": 0.5
            })

        fuel_counter += driving_today * 55

        if fuel_counter >= 1000:

            stops.append({
                "day": day,
                "type": "Fuel Stop",
                "duration": 0.5
            })

            fuel_counter = 0

        remaining_hours -= driving_today

        remaining_distance -= driving_today * 55

        if remaining_hours > 0:

            stops.append({
                "day": day,
                "type": "10 Hour Rest",
                "duration": 10
            })

            day += 1

    stops.append({
        "day": day,
        "type": "Dropoff",
        "duration": 1
    })

    return {
        "stops": stops,
        "total_days": day
    }