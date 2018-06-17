from django.urls import path

from .views import register, login, home

urlpatterns = [
        path('register', register,  name='register'),
        path('login', login, name='login'),
	    path('',home, name='home')
        ]
