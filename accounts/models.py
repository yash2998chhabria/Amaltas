from django.db import models

# Create your models here.
class EmailData(models.Model):
	email = models.EmailField(max_length=254,blank=False,null=False)