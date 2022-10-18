from django.views.generic import ListView

from app.forms import AddOrderForm
from app.models import ProductInCart


class ListCartItem(ListView):
    model = ProductInCart
    context_object_name = 'products'
    template_name = 'list_cart.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        cart = ProductInCart.objects.all()
        total = 0
        item_qty = 0
        cart_id = 0
        for item in cart:
            total += item.qty * item.product.cost
            item_qty += item.qty
            cart_id = item.pk
        context['total'] = total
        context['item'] = item_qty
        context['form'] = AddOrderForm()
        return context
