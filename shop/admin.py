from django.contrib import admin
from .models import Product, Contact
# Register your models here.
# admin.site.register(Product)
@admin.register(Product)

class Product(admin.ModelAdmin):
    list_display = ['product_name','product_id','category','sub_category','price','publish_date','product_desc']
    
@admin.register(Contact)
class Contact(admin.ModelAdmin):
    list_display = ['name','email','phone','desc']
