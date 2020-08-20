from django.contrib import admin
from .models import Article,stall_frame,stall_products,stall_city,product_category
# Register your models here.
admin.site.register(stall_frame)
admin.site.register(stall_products)
admin.site.register(stall_city)
admin.site.register(product_category)
admin.site.register(Article)