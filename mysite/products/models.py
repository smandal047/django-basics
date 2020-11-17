from django.db import models


# Create your models here.
class Product(models.Model):
    # mapping these with database
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    summary = models.TextField()
    featured = models.BooleanField()


"""
 new data can be entered from either the admin panel or
 from the 'shell' cm line
 >>> from products.models import Product
 >>> Product.objects.all()
 >>> Product.objects.create(title='demo', description='new demo 
     ... product', price='536.55', summary='learning')

 then after adding models register it in admin.py in app folder

 after experimenting delete the migrations content and database
 after deletion of database do run 'createsuperuser'
 
 blank vs null:
 blank is for django whether this field can be empty or not
 null id for database whether this field can be empty or not
"""
