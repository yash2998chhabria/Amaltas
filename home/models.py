from django.db import models
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
import sys

# Create your models here.
class PageCounter( models.Model ):
	indexcounter = models.IntegerField()

class MakeVisible(models.Model):
	start_exhibition = models.BooleanField(default=False,null=False)

class Testimonials(models.Model):
	name = models.CharField(max_length=30,default="",null=False)
	testi = models.CharField(max_length=300,default="",null=False)	
	testi_image = models.ImageField(upload_to='testimonials',default="",null=False)
	make_visible = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		if not self.id:
			self.testi_image = self.compress(self.testi_image)
		super(Testimonials, self).save(*args, **kwargs)

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
