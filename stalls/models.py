import sys
from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image
from ckeditor.fields import RichTextField
from phonenumber_field.modelfields import PhoneNumberField
from django.core.files.uploadedfile import InMemoryUploadedFile
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

#has been changed to stall category
class product_category(models.Model):
	categories = models.CharField(max_length=30,default="",null=False)
	def __str__(self):
			return self.categories

class stall_city(models.Model):
	name = models.CharField(max_length=100,default="",null=False)
	city_image = models.ImageField(upload_to='City_images',default="",null=False)
	def __str__(self):
			return self.name

#image compression method
def compress(image):
    im = Image.open(image)
    im = im.convert('RGB')
    im_io = BytesIO() 
    im.save(im_io, 'JPEG', quality=60)
    im_io.seek(0)
    new_image = InMemoryUploadedFile(im_io,'ImageField', "%s.jpg" % image.name.split('.')[0], 'image/jpeg', sys.getsizeof(im_io), None)
    return new_image			

class stall_frame(models.Model):
	stall_user = models.OneToOneField(
        User ,
        on_delete=models.CASCADE, default=1
    )
	name = models.CharField(max_length=30,default="",null=False)
	cover = models.ImageField(upload_to='coverimages',default="",null=False) 
	description = models.CharField(max_length=300,default="",null=False)
	contact_no = PhoneNumberField(default="9999999999")
	contact_stall = models.CharField(max_length=300,default="",null=False)
	premium = models.BooleanField(default=False,null=False)
	poweredby_stall = models.BooleanField(default=False,null=False)
	city = models.ForeignKey(stall_city,on_delete=models.CASCADE,default =1)
	stall_visible_on_website = models.BooleanField(default=False,null=False)
	category = models.ForeignKey(product_category,on_delete=models.CASCADE,default=1) 

	def save(self, *args, **kwargs):
		if not self.id:
			self.cover = self.compress(self.cover)
		super(stall_frame, self).save(*args, **kwargs)

	def compress(self,image):
		im = Image.open(image)
		im = im.convert('RGB')
		im_io = BytesIO() 
		im.save(im_io, 'JPEG', quality=60)
		im_io.seek(0)
		new_image = InMemoryUploadedFile(im_io,'ImageField', "%s.jpg" % image.name.split('.')[0], 'image/jpeg', sys.getsizeof(im_io), None)
		return new_image		

	def __str__(self):
		return self.name

class stall_products(models.Model):
	product_name = models.CharField(max_length=50,default="",null=False)
	price = models.IntegerField(default = 0,null=False)
	product_image = models.ImageField(upload_to='products_images',default="",null=False)
	stall_name = models.ForeignKey(stall_frame,on_delete=models.CASCADE,default=1)

	def save(self, *args, **kwargs):
		if not self.id:
			self.product_image = self.compress(self.product_image)
		super(stall_products, self).save(*args, **kwargs)

	def compress(self,image):
		im = Image.open(image)
		im = im.convert('RGB')
		im_io = BytesIO() 
		im.save(im_io, 'JPEG', quality=60)
		im_io.seek(0)
		new_image = InMemoryUploadedFile(im_io,'ImageField', "%s.jpg" % image.name.split('.')[0], 'image/jpeg', sys.getsizeof(im_io), None)
		return new_image		


	def __str__(self):
			return self.product_name

class Article(models.Model):
	title = models.CharField(max_length=80)
	snippet= models.CharField(max_length=80)
	content = RichTextUploadingField()
	featured = models.BooleanField(default=False)
	date = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=20,default="")
	blogimg=models.ImageField(upload_to='blogimgs',default="",null=False) 

	def save(self, *args, **kwargs):
		if not self.id:
			self.blogimg = self.compress(self.blogimg)
		super(Article, self).save(*args, **kwargs)

	def compress(self,image):
		im = Image.open(image)
		im = im.convert('RGB')
		im_io = BytesIO() 
		im.save(im_io, 'JPEG', quality=60)
		im_io.seek(0)
		new_image = InMemoryUploadedFile(im_io,'ImageField', "%s.jpg" % image.name.split('.')[0], 'image/jpeg', sys.getsizeof(im_io), None)
		return new_image

	def __str__(self):
			return self.title
