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
        my_orders = Order.objects.filter(user = request.session['user_id'])
        return render(request, 'myOrders.html', {'orders': my_orders})


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
        form = OrderForm()
        return render(request, 'addOrder.html', {'form': form})
