from django.shortcuts import redirect
from django.views.generic import CreateView

from app.forms import AddOrderForm
from app.models import ProductInCart, Product, Order


class OrderCreate(CreateView):
    model = Order
    form_class = AddOrderForm

    def form_valid(self, form):
        cart_item = ProductInCart.objects.all()
        products_id = []
        product_qty = 0
        for item in cart_item:
            products_id.append(item.product_id)
            product_qty += item.qty
        create_order = Order.objects.create(
            name=form.instance.name,
            address=form.instance.address,
            phone=form.instance.phone,
        )
        create_order.products.set(products_id)
        create_order.save()
        for i in products_id:
            product = Product.objects.get(pk=i)
            cart_item = ProductInCart.objects.get(product_id=i)
            product.qty -= cart_item.qty
            cart_item.delete()
            product.save()
        return redirect('main')
