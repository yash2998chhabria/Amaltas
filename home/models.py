from django.db import models

# Create your models here.
class PageCounter( models.Model ):
	indexcounter = models.IntegerField()

class MakeVisible(models.Model):
	start_exhibition = models.BooleanField(default=False,null=False)