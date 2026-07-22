def generate_logs(duration):

    logs = []

    day = 1

    while duration > 0:

        driving = min(
            11,
            duration
        )

        log = {
            "day": day,
            "driving": driving
        }

        # Pickup only on first day
        if day == 1:
            log["pickup"] = 1

        duration -= driving

        # Add rest if trip continues
        if duration > 0:
            log["rest"] = 10
        else:
            # Last day
            log["dropoff"] = 1

        logs.append(log)

        day += 1

    return logs