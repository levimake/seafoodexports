from django.shortcuts import render
from django.http import HttpResponse

from .forms import OrderForm


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
