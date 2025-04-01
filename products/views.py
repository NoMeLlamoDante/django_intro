from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product, Category


# Create your views here.
@login_required
def get_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'title': product.name,
        "product": product,
        }
    return render(request, 'products/detail.html', context)


def index(request):
    products = Product.objects.select_related("category").all()
    context = {'products': products}
    return render(request, "products/index.html", context)


@login_required
def get_products_by_category(request, category_id):
    category = Category.objects.prefetch_related("products").get(id=category_id)
    # products = Product.objects.select_related("category").filter(category=category)
    products = category.products.all()

    context = {
        'title': category.name,
        'category': category,
        'products': products,
    }
    return render(request, 'products/index.html', context)
