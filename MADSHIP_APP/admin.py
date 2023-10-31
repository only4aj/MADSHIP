from django.contrib import admin
from .models import Customer,ProductItem,customerdetail
# from .models import Customer
# Register your models here.

admin.site.register(Customer)
admin.site.register(ProductItem)
admin.site.register(customerdetail)