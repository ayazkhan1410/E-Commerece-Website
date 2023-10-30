from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=30, default="")
    sub_category = models.CharField(max_length=30,default="")
    product_desc = models.CharField(max_length=300)
    price = models.IntegerField(max_length=8,default=0)
    publish_date = models.DateField()
    images = models.ImageField(upload_to='shop/images',default="")
    class Meta:
        ordering=['price']
        
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default=" ")
    email = models.EmailField(max_length=60, default=" ")
    phone = models.CharField(max_length=50, default=" ")
    desc = models.CharField(max_length=500, default=" ")
    
    def __str__(self):
        return self.name
    