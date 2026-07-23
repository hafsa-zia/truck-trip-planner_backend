def generate_logs(duration):

    logs = []

    day = 1

    remaining = duration

    while remaining > 0:

        driving = min(11, remaining)

        logs.append({
            "day": day,
            "off_duty": 24 - driving,
            "driving": round(driving, 2),
            "on_duty": 1
        })

        remaining -= driving

        day += 1

    return logs