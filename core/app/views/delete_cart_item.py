from django.urls import reverse_lazy
from django.views.generic import DeleteView

from app.models import Product, ProductInCart


class DeleteCartItem(DeleteView):
    model = ProductInCart

    def get_success_url(self):
        return reverse_lazy('cart')
