from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product


# Create your views here.
def get_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {"product": product})


def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, "products/index.html", context)
