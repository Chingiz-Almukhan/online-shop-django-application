from django.urls import reverse_lazy
from django.views.generic import UpdateView

from app.forms import AddEditForm
from app.models import Product


class EditView(UpdateView):
    template_name = "edit_view.html"
    form_class = AddEditForm
    model = Product
    success_url = reverse_lazy('main')
