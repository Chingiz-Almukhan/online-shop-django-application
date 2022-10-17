from django.views.generic import DetailView

from app.models import Product


class ProductView(DetailView):
    template_name = 'product_view.html'
    model = Product
    context_object_name = 'product'
