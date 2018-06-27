from django.urls import path

from .views import register, login, home, logout, error

urlpatterns = [
        path('register', register,  name='register'),
        path('login', login, name='login'),
        path('logout', logout, name='logout'),
        path('error', error, name='error'),
	    path('',home, name='home')
        ]
