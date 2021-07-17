from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JEK3sJmBj0nWvdjF5cQ9EWifIyBEYc59riK8RUqXSBtd73ZXWkdHL6xGLQIhXr4FTejDbs9wreu4QuhrsljMCdg00V5dPDyHm',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
