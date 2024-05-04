from django.shortcuts import redirect, render
from .models import Category, Products
from .forms import ProductForm
# Create your views here.


def get_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context)

def get_products(request, pk):
    products = Products.objects.filter(category_id=pk)
    context = {
        'products': products
    }
    return render(request, 'products.html', context)

def get_details(request, pk):
    product = Products.objects.get(id=pk)
    context = {
        'product': product
    }
    return render(request, 'details.html', context)


def add_product(request):
    form=ProductForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('get_categories')
    context = {
        'form': form
    }
    return render(request, 'create.html', context=context)

def delete_product(request, pk):
    product = Products.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('get_categories')
    context = {
        'product': product
    }
    return render(request, 'delete.html', context=context)


def update_product(request, pk):
    product = Products.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('get_categories')
    context = {
        'product': product,
        'form': form
    }
    return render(request, 'update.html', context=context)