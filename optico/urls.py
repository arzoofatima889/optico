"""
URL configuration for opticalShop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from shop.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('customer',customer,name='customer'),
    path('customer_edit/<int:customer_id>',customer,name='customer_edit'),
    path('brands',brands,name='brands'),
    path('brands_edit/<int:brands_id>',brands,name='brands_edit'),
    path('glassesTypes',glassesTypes,name='glassesTypes'),
    path('glassesTypes_edit/<int:glassesTypes_id>',glassesTypes,name='glassesTypes_edit'),
    path('products',products,name='products'),
    path('products_edit/<int:product_id>',products,name='products_edit'),
    path('vendors',vendors,name='vendors'),
    path('vendors_edit/<int:vendors_id>',vendors,name='vendors_edit'),
    path('purchaseOrder',purchaseOrder, name='purchaseOrder'),
    path('purchaseOrder_edit/<int:purchase_order_id>',purchaseOrder, name='purchaseOrder_edit'),
    path('purchase_Order_Detail_Item/<int:purchaseOrder_id>',purchase_Order_Detail_Item, name='purchase_Order_Detail_Item'),
    path('purchase_Order_Detail_Item_edit/<int:purchaseOrder_id>/<int:purchase_order_detail_item_id>',purchase_Order_Detail_Item, name='purchase_Order_Detail_Item_edit'),
    path('purchase_invoice/<int:purchase_order_id>',purchase_invoice, name='purchase_invoice'),
    path('purchase_order_process/<int:purchase_order_id>',purchase_order_process, name='purchase_order_process'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
