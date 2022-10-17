from django.shortcuts import render, redirect

from app.models import Category, Product


def add_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'add_product.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        cost = request.POST.get('cost')
        image = request.POST.get('image')
        category = request.POST.get('category')
        product = Product.objects.create(name=name, description=description, cost=cost, image=image,
                                         category_id=category)
        return redirect('product', pk=product.pk)


def category_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'add_category.html', context)
    elif request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = Category.objects.create(name=name, description=description)
        return redirect('main')
