from django.shortcuts import render

from app.models import Product, Category


def index_view(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'main_page.html', context)


def product_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_view.html', context={
        'product': product
    })


def categories_view(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)
