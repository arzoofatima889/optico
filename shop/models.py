from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(null=True,blank=True,max_length=15)
    def __str__(self):
        return self.name

class Brands(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Glasses_types(models.Model):
    brands = models.ForeignKey(Brands,null=True,blank=True,on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.brands}'  
   
class Products(models.Model):
    rack_choices = [('','-select-'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')]
    rack = models.CharField(max_length=20,null=True,blank=True,choices=rack_choices)
    glasses_types = models.ForeignKey(Glasses_types,null=True,blank=True,on_delete=models.SET_NULL)
    gender_choices = [('','-select-'),('male','Male'),('female','Female')]
    genders_in_glasses = models.CharField(max_length=20,null=True,blank=True,choices=gender_choices)
    name = models.CharField(max_length=20)
    purchase_price = models.IntegerField(null=True,blank=True)
    sale_price = models.IntegerField(null=True,blank=True)
    image = models.ImageField(null=True,blank=True,upload_to='documents')
    size_choices = [('','-select-'),('Small','Small'),('Medium','Medium'),('Large','Large')]
    size = models.CharField(max_length=15,null=True,blank=True,choices=size_choices)
    quantity = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return f'{self.name} {self.glasses_types}'

class Eyesight_farVision_chart(models.Model):
    customer = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    option_choices=[('','-Select-'),('Plano','Plano'),('Foggy','Foggy'),]
    r_spherical = models.CharField(max_length=20,null=True,blank=True)
    r_cylindrical = models.CharField(max_length=20,null=True,blank=True)
    r_axis = models.CharField(max_length=20)
    r_va = models.CharField(max_length=20,null=True,blank=True)
    r_option = models.CharField(max_length=20,null=True,blank=True,choices=option_choices)
    l_spherical = models.CharField(max_length=20,null=True,blank=True)
    l_cylindrical = models.CharField(max_length=20,null=True,blank=True)
    l_axis = models.CharField(max_length=20)
    l_va = models.CharField(max_length=20,null=True,blank=True)
    l_option = models.CharField(max_length=20,null=True,blank=True,choices=option_choices)

class Eyesight_nearVision_chart(models.Model):
    customer = models.ForeignKey(Customer,null=True,blank=True,on_delete=models.SET_NULL)
    option_choices=[('','-Select-'),('Plano','Plano'),('Foggy','Foggy'),]
    r_spherical = models.CharField(max_length=20,null=True,blank=True)
    r_cylindrical = models.CharField(max_length=20,null=True,blank=True)
    r_axis = models.CharField(max_length=20)
    r_va = models.CharField(max_length=20,null=True,blank=True)
    r_option = models.CharField(max_length=20,null=True,blank=True,choices=option_choices)
    l_spherical = models.CharField(max_length=20,null=True,blank=True)
    l_cylindrical = models.CharField(max_length=20,null=True,blank=True)
    l_axis = models.CharField(max_length=20)
    l_va = models.CharField(max_length=20,null=True,blank=True)
    l_option = models.CharField(max_length=20,null=True,blank=True,choices=option_choices)

class Payment(models.Model):
    products = models.ForeignKey(Products,null=True,blank=True,on_delete=models.SET_NULL)
    advance = models. IntegerField(null=True,blank=True)
    delivery_date = models.DateField(auto_now_add=True)
    balance = models.IntegerField(null=True,blank=True)

class Vendors(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(null=True,blank=True,max_length=15)
    address = models.CharField(null=True,blank=True,max_length=30)
    
    def __str__(self):
        return self.name 
    
class Purchase_Order(models.Model):
    vendors = models.ForeignKey(Vendors,null=True,blank=True,on_delete=models.SET_NULL)
    date = models.DateField(null=True,blank=True)
    order_number = models.CharField(max_length=20,null=True,blank=True)
    delivery_date = models.DateField(null=True,blank=True)
    remarks = models.CharField(max_length=20,null=True,blank=True)
    subtotal = models.IntegerField(null=True,blank=True)
    total_items = models.IntegerField(null=True,blank=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.vendors.name}'

class Purchase_Order_Detail_Item(models.Model):
    purchase_Order = models.ForeignKey(Purchase_Order,null=True,blank=True,on_delete=models.SET_NULL)
    products = models.ForeignKey(Products,null=True,blank=True,on_delete=models.SET_NULL)
    quantity = models.IntegerField(null=True,blank=True)
    amount = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return f'{self.products.name}' 
    

    