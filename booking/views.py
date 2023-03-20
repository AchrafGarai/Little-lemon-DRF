from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from booking.models import Booking, Menu
from booking.serializers import BookingSerializer, MenuSerializer
from rest_framework.decorators import permission_classes
from rest_framework import status
# Create your views here.
def index(request):
    return render(request, 'index.html')

@api_view()
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_all_bookings(request):
    if request.method == 'GET':
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid Format"} ,status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_all_menus(request):
    if request.method == 'GET':
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid Format"} ,status.HTTP_404_NOT_FOUND)