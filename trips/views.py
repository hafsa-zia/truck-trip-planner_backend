from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import TripSerializer
from .services import get_route_data

from hos.calculator import calculate_hos
from logs.generator import generate_logs


class TripView(APIView):

    def post(self, request):

        serializer = TripSerializer(data=request.data)

        if serializer.is_valid():

            trip = serializer.save()

            route = get_route_data(
                trip.current_location,
                trip.pickup_location,
                trip.dropoff_location
            )
            if route is None:

                return Response(
        {
            "error":
            "One or more locations could not be found. Please check the spelling and try again."
        },
        status=400
    )
            hos = calculate_hos(
                route["distance"],
                route["duration"],
                trip.current_cycle_used
            )

            logs = generate_logs(
                route["duration"]
            )

            return Response({

                "trip_id": trip.id,

                "distance": route["distance"],
                "duration": route["duration"],

                "coordinates": route["coordinates"],

                "current_coordinates":
                    route["current_coordinates"],

                "pickup_coordinates":
                    route["pickup_coordinates"],

                "dropoff_coordinates":
                    route["dropoff_coordinates"],

                "total_days": hos["total_days"],
                "stops": hos["stops"],
                "logs": logs

            })

        return Response(
            serializer.errors,
            status=400
        )