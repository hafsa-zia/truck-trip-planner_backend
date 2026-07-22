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

            hos = calculate_hos(
                route["distance"],
                route["duration"],
                trip.current_cycle_used
            )

            logs = generate_logs()

            return Response({
                "trip_id": trip.id,
                "distance": route["distance"],
                "duration": route["duration"],
                "coordinates": route["coordinates"],
                "stops": hos["stops"],
                "logs": logs
            })

        return Response(serializer.errors, status=400)