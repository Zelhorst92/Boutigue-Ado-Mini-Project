from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51KLSGGASIwXlGFmLcieHvS7Tw4hT9X5auF1a9Vq8Aj2MZOjtSFNeZXxtpOR2hvS4mth6LZmDkESq0N0mD3lIJjBS00RtuCIEnb',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
