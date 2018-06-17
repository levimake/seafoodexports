from django.shortcuts import render
from django.http import HttpResponse

from .forms import OrderForm
from .models import Order

from common.decorators import IsLoggedIn

@IsLoggedIn
def home(request):
    if request.method == "GET":
        my_orders = Order.objects.filter(user = request.session['user_id'])
        print(my_orders)
        return render(request, 'myOrders.html', {'orders': my_orders})


@IsLoggedIn
def place_order(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Order Placed")
        else:
            return HttpResponse("Failed to place order")

    elif request.method == "GET":
        form = OrderForm()
        return render(request, 'addOrder.html', {'form': form})
