from django.urls import reverse_lazy
from django.views.generic import DeleteView

from app.models import Product


class Delete(DeleteView):
    model = Product

    def get_success_url(self):
        return reverse_lazy('main')
