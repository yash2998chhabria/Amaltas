from django.db import models

# Create your models here.
class contact_info(models.Model):
	full_name = models.CharField(max_length=60,blank=False,null=False)
	email = models.EmailField(max_length=254,blank=False,null=False)
	mobilenumber = models.BigIntegerField(blank=False,null=False)
	message = models.TextField(blank=False,null=False)