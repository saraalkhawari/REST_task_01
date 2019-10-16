from .models import Flight, Booking
from rest_framework.generics import ListAPIView
from .serializers import FlightListSerializer, BookingListSerializer
from datetime import datetime


class FlightListView(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightListSerializer


class BookingListView(ListAPIView):
	today = datetime.today()
	queryset = Booking.objects.filter(date__gte=today)
	serializer_class = BookingListSerializer



