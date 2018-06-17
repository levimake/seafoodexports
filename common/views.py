from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import User
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login


def home(request):
    if request.method=="GET":
        return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            password = request.POST['password']
            email = request.POST['email']
            country = request.POST['country']
            phone_number = request.POST['phone_number']

            if request.POST['address']:
                address = request.POST['address']
            else:
                address = None

            if not User.objects.filter(username=username).exists():
                object = User.create(username, first_name, last_name, country,
                                     email, phone_number, password, address)
            else:
                object = User.objects.get(username=username)

            print(object)

            return HttpResponse("Success")

        except Exception as e:
            print(e)
            print("Error: Cannot create user")
            return HttpResponse("Error")

    if request.method == "GET":
        form = RegistrationForm()
        return render(request, 'register.html', {'form':form})


def login(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']

            user = User.objects.get(username=username)

            if user.login(username, password):
               request.session['logged_in'] = True
               request.session['username'] = objects.username
               request.session.save()
               return HttpResponse("Login Success")

            else:
                return redirect('login')

        except Exception as e:
            print(e)
            return HttpResponse("Exception")

    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form':form})
