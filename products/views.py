from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from products.models import Product, Category
from .forms import CommentForm


# Create your views here.
# @login_required
def get_detail(request, product_id):
    product = Product.objects.prefetch_related("comments__user").get(id=product_id)

    comments = product.comments.order_by('creation_date').all()

    form = CommentForm()

    context = {
        'title': product.name,
        "product": product,
        "form": form,
        'comments': comments,
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


@login_required
def add_new_comment(request, product_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            user = request.user
            new_comment = form.save(commit=False)
            new_comment.user = user
            new_comment.product = Product.objects.get(id=product_id)
            new_comment.save()
        return redirect('detail', product_id=product_id)
    else:
        return redirect('detail', product_id=product_id)
