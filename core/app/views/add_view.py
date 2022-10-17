from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.forms import AddEditForm
from app.models import Product


class AddProductView(CreateView):
    template_name = 'add_product.html'
    success_url = reverse_lazy('main')
    model = Product
    form_class = AddEditForm
