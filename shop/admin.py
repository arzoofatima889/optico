from django.contrib import admin
from shop.models import *
# Register your models here
admin.site.register(Customer)
admin.site.register(Brands)
admin.site.register(Glasses_types)
admin.site.register(Products)
admin.site.register(Purchase_Order)
admin.site.register(Purchase_Order_Detail_Item)
admin.site.register(Vendors)
