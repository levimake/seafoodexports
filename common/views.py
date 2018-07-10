from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.hashers import check_password

from .models import User
from .forms import RegistrationForm, LoginForm, ProfileForm, AddressForm, PhoneForm, PasswordForm
from .decorators import IsLoggedIn


def home(request):
    if request.method=="GET":
        request.session['logged_in'] = request.session.get('logged_in', False)
        return render(request, 'index.html', {'request':request})


@staff_member_required
def register(request):
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']

            if not User.objects.filter(username=username).exists():
                object = User.create(username, email,
                                     password)
            else:
                object = User.objects.get(username=username)

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
               request.session['user_id'] = user.id
               request.session.save()

               if user.completed:
                   return HttpResponseRedirect("/profile")

               else:
                   return HttpResponseRedirect("/submit")

            else:
                return render(request, 'login.html', {'form':form, 'error':error})

        except Exception as e:
            form = LoginForm()
            error="The username or password you've entered is invalid"
            return render(request, 'login.html', {'form':form, 'error':error})

    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form':form})


@IsLoggedIn
def logout(request) :
    if request.method == "GET" :
        request.session.flush()
        return redirect('/')


@IsLoggedIn
def profile(request):
    if request.method == "POST":
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            country = request.POST['country']
            password = request.POST['password']
            phone_number = request.POST['phone_number']
            address = request.POST['address']

            id = request.session['user_id']

            user = User.submit(id, first_name, last_name,
                               country, password,
                               phone_number, address)

            return HttpResponseRedirect('/orders')

        except Exception as e:
            print(e)
            return HttpResponse("Profile update failed")

    elif request.method == "GET":
        form = ProfileForm()
        return render(request, 'submit.html', {'form': form})

    else:
        return HttpResponse("Invalid request")


@IsLoggedIn
def profile_view(request):
    if request.method == "GET":

        id = request.session['user_id']
        user = User.objects.get(id=id)

        if user.completed:
            id = request.session['user_id']
            user = User.objects.get(id = id)
            return render(request, 'update.html', {'cur_user': user})

        else:
            return HttpResponseRedirect('/submit')


@IsLoggedIn
def update(request):
    if request.method == "POST":

        try:
            password = request.POST.get('password', False)
            address = request.POST.get('address', False)
            phone_number = request.POST.get('phone_number', False)

            id = request.session['user_id']
            user = User.objects.get(id=id)

            if password:
                old_password = request.POST['old_password']

                if check_password(old_password, user.password):
                    User.update_password(user.id, password)

            elif address:
                User.update_address(user.id, address)

            elif phone_number:
                User.update_phone(user.id, phone_number)

            else:
                return HttpResponseRedirect('/profile')

        except Exception as e:
            return HttpResponseRedirect('/profile')


    else:
        return HttpResponseRedirect('/profile')


@IsLoggedIn
def update_password(request):
    if request.method == "GET":
        form = PasswordForm()
        return render(request, 'update.html', {'form': form})


@IsLoggedIn
def update_address(request):
    if request.method == "GET":
        form = AddressForm()
        return render(request, 'update.html', {'form': form})


@IsLoggedIn
def update_phone_number(request):
    if request.method == "GET":
        form = PhoneForm()
        return render(request, 'update.html', {'form': form})


def error(request) :
    if request.method == "GET" :
        return render(request, "error.html")

def about(request) :
    if request.method == "GET" :
        return render(request, "about.html")
