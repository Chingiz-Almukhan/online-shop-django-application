from django.shortcuts import redirect

from app.models import Product, Category


def delete_view(request, pk):
    product = Product.objects.get(pk=pk)
    product.delete()
    return redirect('main')


def category_delete_view(request, pk):
    category = Category.objects.get(pk=pk)
    try:
        product = Product.objects.get(category_id=pk)
        product.category_id = ''
        product.save()
    except Exception:
        pass
    category.delete()
    return redirect('categories')
