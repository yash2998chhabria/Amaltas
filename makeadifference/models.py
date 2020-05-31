from django.db import models

# Create your models here.
class MakeADifference(models.Model):
	organisation_name =  models.CharField(max_length=100,default="",null=False)
	donation_cover = models.ImageField(upload_to='MakeADifference',default="",null=False)
	description = models.TextField(default="",null=False)
	contact_details = models.TextField(default="",null=False)