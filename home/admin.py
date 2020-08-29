from django.contrib import admin
from .models import PageCounter,MakeVisible,Testimonials
# Register your models here.
admin.site.register(MakeVisible)
admin.site.register(PageCounter)
admin.site.register(Testimonials)