from django.urls import path

from .views import place_order, home

urlpatterns = [
        path('add', place_order,  name='place_order'),
        path('', home, name='order_home')
        ]
