from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *
from django import forms
from django.forms import modelformset_factory
# Create your views here.

def home(request):
    heading = 'Welcome'
    detail = Products.objects.all()
    data = {'heading': heading,'detail':detail}
    return render(request,'home.html',data)


def customer(request,customer_id=None):
    formset = modelformset_factory(Customer, extra=1, max_num=1,
                                   fields=('name', 'phone',), labels={'name': 'Name', 'phone': 'Phone'},
                                   widgets={'name': forms.TextInput(attrs={'placeholder': 'Enter Name', 'style': 'height: 40px;', 'class': 'form-control', 'required': False}), 
                                            'phone': forms.TextInput(attrs={'style': 'height: 40px;', 'class': 'form-control', 'required': False}), })
    if request.method == 'POST':
        formset_post = formset(request.POST)
        for form in formset_post:
            if form.is_valid():
                form.save()
        return redirect('customer')
    if customer_id is not None:
        formset = formset(queryset=Customer.objects.filter(id=customer_id))
    else:
        formset = formset(queryset=Customer.objects.none())
    detail = Customer.objects.all()
    data = {'formset': formset,'detail': detail}
    return render(request,'customer_list.html',data)



    
def brands(request,brands_id=None):
    formset = modelformset_factory(Brands, extra=1, max_num=1,
                                   fields=('name',), labels={'name': 'Name',},
                                   widgets={'name': forms.TextInput(attrs={'placeholder': 'Enter Name', 'style': 'height: 40px;', 'class': 'form-control', 'required': False}),})
    if request.method == 'POST':
        formset_post = formset(request.POST)
        for form in formset_post:
            if form.is_valid:
                form.save()
        return redirect('brands')
    if brands_id is not None:
        formset = formset(queryset=Brands.objects.filter(id=brands_id))
    else:
        formset = formset(queryset=Brands.objects.none())
    detail = Brands.objects.all()
    data = {'formset': formset,'detail': detail}
    return render(request,'brands.html',data)

def glassesTypeslist(request):
    detail = Glasses_types.objects.all()
    data = {'detail': detail}
    return render(request,'home.html',data)

def glassesTypes(request,glassesTypes_id=None):
    formset = modelformset_factory(Glasses_types, extra=1, max_num=1,
                                   fields=('name','brands'), labels={'name': 'Name','brands':'Brands'},
                                   widgets={'name': forms.TextInput(attrs={'placeholder': 'Enter Name', 'style': 'height: 40px;', 'class': 'form-control', 'required': False}),
                                            'brands': forms.Select(attrs={'placeholder': '-select-', 'style': 'height: 40px;', 'class': 'form-control', 'required': False})})
    if request.method == 'POST':
        formset_post = formset(request.POST)
        for form in formset_post:
            if form.is_valid:
                form.save()
        return redirect('glassesTypes')
    if glassesTypes_id is not None:
        formset = formset(queryset=Glasses_types.objects.filter(id=glassesTypes_id))
    else:
        formset = formset(queryset=Glasses_types.objects.none())
    detail = Glasses_types.objects.all()
    data = {'formset': formset,'detail': detail}
    return render(request,'glasses_type.html',data)


def products(request,product_id=None):
    # vision_list =[]
    # current_value = 0
    # current_sign = None
    # for i in range (144):
    #     current_value += 0.25
    #     if current_value > 18:
    #         if current_sign == None:
    #             current_sign = True
    #             current_value = 0
    #     if current_sign :
    #         vision_list.append(f"- {current_value}")
    #     else:
    #         vision_list.append(f"+ {current_value}")
    # print(vision_list)
    formset = modelformset_factory(Products, extra=1, max_num=1,
                                   fields=('rack','glasses_types','genders_in_glasses','name','purchase_price','sale_price','image','size','quantity'), labels={'rack':'Rack Number','glasses_types':'Glasses Type','genders_in_glasses':'Gender','name':'Product Name','purchase_price':'Purchase Price','sale_price':'Sale price','image':'Image','size':'Size','quantity':'Quantity'},
                                   widgets={'rack': forms.Select(attrs={'placeholder': 'Enter Name', 'required': False}), 
                                            'glasses_types': forms.Select(attrs={ 'required': False}),
                                            'genders_in_glasses': forms.Select(attrs={ 'required': False}),
                                            'name': forms.TextInput(attrs={ 'required': False}),
                                            'purchase_price': forms.TextInput(attrs={ 'required': False}),
                                            'sale_price': forms.TextInput(attrs={ 'required': False}),
                                            'image': forms.FileInput(attrs={ 'required': False}),
                                            'size': forms.Select(attrs={ 'required': False}),
                                            'quantity': forms.TextInput(attrs={ 'required': False}),
                                            })
    if request.method == 'POST':
        formset_post = formset(request.POST, request.FILES)
        for form in formset_post:
            if form.is_valid():
                form.save()
        return redirect('products')
    if product_id is not None:
        formset = formset(queryset=Products.objects.filter(id=product_id))
    else:
        formset = formset(queryset=Products.objects.none())
    detail = Products.objects.all()
    data = {'formset': formset, 'detail': detail}
    return render(request,'products.html',data)

def vendors(request,vendors_id=None):
    formset = modelformset_factory(Vendors, extra=1, max_num=1,
                                   fields=('name', 'phone','address'), labels={'name': 'Name', 'phone': 'Phone','address':'Address'},
                                   widgets={'name': forms.TextInput(attrs={'placeholder': 'Enter Name', 'style': 'height: 40px;', 'class': 'form-control', 'required': False}), 
                                            'phone': forms.TextInput(attrs={'style': 'height: 40px;', 'class': 'form-control', 'required': False}),
                                            'address': forms.TextInput(attrs={'style': 'height: 40px;', 'class': 'form-control', 'required': False}), })
    if request.method == 'POST':
        formset_post = formset(request.POST)
        for form in formset_post:
            if form.is_valid():
                form.save()
        return redirect('vendors')
    if vendors_id is not None:
        formset = formset(queryset=Vendors.objects.filter(id=vendors_id))
    else:
        formset = formset(queryset=Vendors.objects.none())
    heading = 'New Vendor'
    detail = Vendors.objects.all()
    data = {'formset': formset,'detail':detail,'heading':heading}
    return render(request,'vendors_list.html',data)

def purchaseOrder(request,purchase_order_id=None):
    formset = modelformset_factory(Purchase_Order, extra=1, max_num=1,
                                   fields=('date','vendors','delivery_date','remarks','order_number'),
                                   widgets={'date': forms.TextInput(attrs={'type':'date', 'required': False}),
                                            'vendors': forms.Select(attrs={  'required': False}),
                                            'delivery_date': forms.TextInput(attrs={'type':'date', 'required': False}),
                                            'order_number': forms.TextInput(attrs={  'required': False}),                                        
                                            'remarks': forms.TextInput(attrs={ 'required': False})
                                            })
    if request.method == 'POST':
        formset_post = formset(request.POST)
        for form in formset_post:
            if form.is_valid():
                form.save()
        return redirect('purchaseOrder')
    if purchase_order_id is not None:
        formset = formset(queryset=Purchase_Order.objects.filter(id=purchase_order_id))
    else:
        formset = formset(queryset=Purchase_Order.objects.none())
    detail = Purchase_Order.objects.all()
    data = {'formset': formset, 'detail': detail}
    return render(request,'store.html',data)

def purchase_Order_Detail_Item(request,purchaseOrder_id, purchase_order_detail_item_id=None):
    purchaseOrder_obj = Purchase_Order.objects.get(id=purchaseOrder_id)
    formset = modelformset_factory(Purchase_Order_Detail_Item, extra=1, max_num=1,
                                   fields=('products','quantity'),
                                   widgets={'products': forms.Select(attrs={'style': 'height: 40px;width:35%;margin-bottom:1%;margin-right:3%', 'class': 'form-control', 'required': False}),
                                            'quantity': forms.NumberInput(attrs={'style': 'height: 40px;width:35%;margin-bottom:1%;margin-right:3%', 'class': 'form-control', 'required': False}),
                                            })
    if request.method == 'POST':
        formset_post = formset(request.POST)
        for form in formset_post:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.purchase_Order = purchaseOrder_obj
                products_obj = Products.objects.get(id=obj.products.id)
                obj.amount = products_obj.purchase_price * obj.quantity
                obj.save()
        return HttpResponseRedirect(reverse('purchase_Order_Detail_Item', args=[purchaseOrder_id]))
    if purchase_order_detail_item_id is not None:
        formset = formset(queryset=Purchase_Order_Detail_Item.objects.filter(id=purchase_order_detail_item_id))
    else:
        formset = formset(queryset=Purchase_Order_Detail_Item.objects.none())
    detail = Purchase_Order_Detail_Item.objects.filter(purchase_Order=purchaseOrder_obj)
    items = 0
    subtotal = 0
    for i in detail:
        subtotal = subtotal + i.amount
        items = items + i.quantity
    purchaseOrder_obj.subtotal = subtotal
    purchaseOrder_obj.total_items = items
    purchaseOrder_obj.save()
    data = {'formset': formset, 'detail': detail,'subtotal':subtotal,'items':items}
    return render(request,'order_details.html',data)

def purchase_invoice(request,purchase_order_id):
    purchase_order_obj = Purchase_Order.objects.get(id=purchase_order_id)
    purchase_order_detail_obj = Purchase_Order_Detail_Item.objects.filter(purchase_Order=purchase_order_obj)
    seller_details = Purchase_Order.objects.filter(vendors=purchase_order_obj.vendors)
    data = {'detail':purchase_order_detail_obj,'seller_details':seller_details}
    return render(request,'invoice.html',data)

def purchase_order_process(request,purchase_order_id):
    purchase_order_obj = Purchase_Order.objects.get(id=purchase_order_id)
    purchase_order_detail_obj = Purchase_Order_Detail_Item.objects.filter(purchase_Order=purchase_order_obj)
    if purchase_order_obj.status == False:
        for i in purchase_order_detail_obj:
            product_obj = i.products
            product_obj.quantity += i.quantity
            product_obj.save()
        purchase_order_obj.status = True
        purchase_order_obj.save()
    purchase_order_detail_objs = Products.objects.all()
    data = {'detail':purchase_order_detail_objs}
    return render(request,'stock.html',data)