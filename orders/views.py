from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .forms import OrderForm
from .models import Order
from .models import User

from common.decorators import IsLoggedIn
from common.models import User


@IsLoggedIn
def home(request):
    if request.method == "GET":
        id = request.session['user_id']
        user = User.objects.get(id=id)
        
        if user.completed:
            my_orders = Order.objects.filter(user=user)
            return render(request, 'myOrders.html', {'orders': my_orders})
        
        else:
            return HttpResponseRedirect('/submit')

@IsLoggedIn
def place_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            user = User.objects.get(id = request.session['user_id'])
            order.user = user
            order.save()
            return HttpResponseRedirect("/orders")
        else:
            error="Sorry we couldn't place the order. An unexpected error has occured. Please try again later."
            return render(request, 'error.html', {'error':error})

    elif request.method == "GET":
        id = request.session['user_id']
        user = User.objects.get(id=id)
        
        if user.completed:
            form = OrderForm()
            return render(request, 'addOrder.html', {'form': form})

        else:
            return HttpResponseRedirect('/submit')
