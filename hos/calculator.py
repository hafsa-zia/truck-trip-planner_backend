def calculate_hos(
        distance,
        duration,
        cycle_hours
):

    stops = []
    day = 1

    while duration > 0:

        # Maximum legal driving in a day
        drive = min(
            11,
            duration
        )

        # Driving event
        stops.append({
            "day": day,
            "type": "Driving",
            "duration": drive
        })

        # Add 30-minute break after 8+ hours
        if drive >= 8:
            stops.append({
                "day": day,
                "type": "30 Min Break",
                "duration": 0.5
            })

        duration -= drive

        # Add overnight rest if trip continues
        if duration > 0:
            stops.append({
                "day": day,
                "type": "10 Hour Rest",
                "duration": 10
            })

        day += 1

    # Pickup and Dropoff
    stops.insert(0, {
        "day": 1,
        "type": "Pickup",
        "duration": 1
    })

    stops.append({
        "day": day - 1,
        "type": "Dropoff",
        "duration": 1
    })

    return {
        "distance": distance,
        "stops": stops
    }