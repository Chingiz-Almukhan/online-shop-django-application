from django.urls import path

from app.views.add_view import AddProductView
from app.views.base import IndexView
from app.views.cart_add_view import CreateCartItem
from app.views.cart_view import ListCartItem
from app.views.delete_cart_item import DeleteCartItem

from app.views.delete_view import Delete
from app.views.edit_view import EditView
from app.views.product_view import ProductView

urlpatterns = [
    path('', IndexView.as_view(), name='main'),
    path('products/<int:pk>', ProductView.as_view(), name='product'),
    path('products/add', AddProductView.as_view(), name='add'),
    path('products/<int:pk>/edit', EditView.as_view(), name='edit'),
    path('products/<int:pk>/delete', Delete.as_view(), name='delete'),
    path('add/<int:pk>', CreateCartItem.as_view(), name='add_to_cart'),
    path('cart', ListCartItem.as_view(), name='cart'),
    path('delete/<int:pk>', DeleteCartItem.as_view(), name='delete_position')

]
