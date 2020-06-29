from django.db import models

# Create your models here.
class EmailData(models.Model):
	whatsapp = models.BigIntegerField(blank=True,null=True)