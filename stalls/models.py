from django.db import models

# Create your models here.
class stall_frame(models.Model):
	name = models.CharField(max_length=100,default="",null=False)
	cover = models.ImageField(upload_to='coverimages',default="",null=False) 
	description = models.TextField(default="",null=False)
	contact_stall = models.TextField(default="",null=False)
	premium = models.BooleanField(default=False,null=False)
	poweredby_stall = models.BooleanField(default=False,null=False)
	def __str__(self):
		return self.name	

class stall_products(models.Model):
	product_name = models.CharField(max_length=50,default="",null=False)
	price = models.IntegerField(default = 0,null=False)
	product_image = models.ImageField(upload_to='products_images',default="",null=False)
	category = models.CharField(max_length=30,default="",null=False)
	stall_name = models.ForeignKey(
        stall_frame,
        on_delete=models.CASCADE,
    )

