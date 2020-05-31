from django.shortcuts import render
from .models import MakeADifference

# Create your views here.
def makeadifference(request):
	mads = MakeADifference.objects.all()
	return render(request,"make_a_difference.html",{'mads':mads})