from django.urls import path

from . import views

urlpatterns = [

    # fasisi.pythonanywhere.com/hotelapp/
    path('', views.login, name='login'),

    # fasisi.pythonanywhere.com/hotelapp/reservasi/
    path('reservasi/', views.reservasi, name='reservasi'),

    # fasisi.pythonanywhere.com/hotelapp/rooms/
    path('rooms/', views.rooms, name='rooms'),

    # fasisi.pythonanywhere.com/hotelapp/rooms_get/
    path('rooms_get/', views.rooms_get, name='rooms_get'),

    # fasisi.pythonanywhere.com/hotelapp/rooms_add/
    path('rooms_add/', views.rooms_add, name='rooms_add'),

    # fasisi.pythonanywhere.com/hotelapp/rooms_submit/
    path('rooms_submit/', views.rooms_submit, name='rooms_submit'),

    # fasisi.pythonanywhere.com/hotelapp/rooms_delete/
    path('rooms_delete/', views.rooms_delete, name='rooms_delete'),
]