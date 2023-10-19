from django.contrib import admin
from .models import Customer,ProductItem
# from .models import Customer
# Register your models here.

admin.site.register(Customer)
admin.site.register(ProductItem)