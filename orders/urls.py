from django.urls import path

from .views import place_order

urlpatterns = [
        path('add', place_order,  name='place_order'),
        ]
