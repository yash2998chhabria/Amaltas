from django.contrib import admin
from .models import PageCounter,MakeVisible
# Register your models here.
admin.site.register(MakeVisible)
admin.site.register(PageCounter)