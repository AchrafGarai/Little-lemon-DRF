from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from booking.models import Booking, Menu
from booking.serializers import BookingSerializer, MenuSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html')

@api_view()
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['GET'])
def get_all_bookings(request):
    bookings = Booking.objects.all()
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_menus(request):
    menus = Menu.objects.all()
    serializer = MenuSerializer(menus, many=True)
    return Response(serializer.data)