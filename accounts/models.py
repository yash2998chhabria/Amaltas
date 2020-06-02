from django.db import models

# Create your models here.
class EmailData(models.Model):
	email = models.EmailField(max_length=254,blank=False,null=True)
	whatsapp = models.BigIntegerField(blank=False,null=True)