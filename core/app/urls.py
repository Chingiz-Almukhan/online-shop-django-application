from django.urls import path

from app.views.add_view import AddProductView
from app.views.base import IndexView

from app.views.delete_view import Delete
from app.views.edit_view import EditView
from app.views.product_view import ProductView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('products/<int:pk>', ProductView.as_view(), name='product'),
    path('products/add', AddProductView.as_view(), name='add'),
    path('products/<int:pk>/edit', EditView.as_view(), name='edit'),
    path('products/<int:pk>/delete', Delete.as_view(), name='delete'),

]
