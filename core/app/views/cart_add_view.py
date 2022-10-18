
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from app.forms import AddEditCartForm
from app.models import ProductInCart, Product


class CreateCartItem(CreateView):
    model = ProductInCart
    form_class = AddEditCartForm
    template_name = 'create_item.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        try:
            cart = ProductInCart.objects.get(product_id=self.kwargs.get('pk'))
            if cart:
                cart = get_object_or_404(ProductInCart, product_id=self.kwargs.get('pk'))
                cart.qty += form.instance.qty
                if cart.qty > product.qty:
                    cart.qty = product.qty
                    cart.save()
                return redirect('main')
        except Exception:
            form.instance.product = product
            if form.instance.qty > product.qty:
                form.instance.qty = product.qty
            form.save()
            return redirect('main')
