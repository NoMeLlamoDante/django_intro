from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .models import Category


# Create your views here.
def get_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {"product": product})


def index(request):
    products = Product.objects.select_related("category").all()
    context = {
        'products': products
    }
    return render(request, "products/index.html", context)


def get_products_by_category(request, category_id):
    category = Category.objects.prefetch_related("products").get(id=category_id)
    # products = Product.objects.select_related("category").filter(category=category)
    products = category.products.all()

    context = {
        'category': category,
        'products': products,
    }

    return render(request, 'products/category.html', context)
