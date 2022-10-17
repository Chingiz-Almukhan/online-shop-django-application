from django.urls import path

from app.views.add_view import add_view, category_view
from app.views.base import index_view, product_view, categories_view
from app.views.delete_view import delete_view, category_delete_view
from app.views.edit_view import edit_view, category_edit_view

urlpatterns = [
    path('', index_view, name='main'),
    path('products/<int:pk>', product_view, name='product'),
    path('products/add', add_view, name='add'),
    path('categories/add', category_view, name='category_add'),
    path('products/<int:pk>/edit', edit_view, name='edit'),
    path('products/<int:pk>/delete', delete_view, name='delete'),
    path('categories/', categories_view, name='categories'),
    path('categories/<int:pk>/edit', category_edit_view, name='category_edit'),
    path('categories/<int:pk>/delete', category_delete_view, name='category_delete'),

]