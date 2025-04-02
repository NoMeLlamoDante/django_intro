from django.contrib import admin
from .models import Product
from .models import Category
from products.models import Comments

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Comments)
