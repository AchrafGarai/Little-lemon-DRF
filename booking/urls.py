from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('hello/', views.hello_world),
    path('api/bookings/', views.get_all_bookings, name='bookings'),
    path('api/menu/', views.get_all_menus, name='menus'),
]