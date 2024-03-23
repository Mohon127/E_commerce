from django.views import generic
from django.shortcuts import render, redirect

from .form import CheckoutForm


class Checkout(generic.View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        context = {
            'form': form
        }
        return render(self.request, 'order/checkout.html', context)

