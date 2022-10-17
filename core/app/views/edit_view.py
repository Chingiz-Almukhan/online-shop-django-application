from django.shortcuts import render, redirect

from app.models import Product, Category


def edit_view(request, pk):
    product = Product.objects.get(pk=pk)
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {'product': product,
                   'categories': categories}
        return render(request, 'edit_view.html', context)
    elif request.method == 'POST':
        product.name = request.POST.get('name')
        product.description = request.POST.get('description')
        product.cost = request.POST.get('cost')
        product.image = request.POST.get('image')
        product.category_id = request.POST.get('category')
        product.save()
        return redirect('main')


def category_edit_view(request, pk):
    category = Category.objects.get(pk=pk)
    if request.method == 'GET':
        context = {'category': category}
        return render(request, 'edit_category_view.html', context)
    elif request.method == 'POST':
        category.name = request.POST.get('name')
        category.description = request.POST.get('description')
        category.save()
        return redirect('categories')
