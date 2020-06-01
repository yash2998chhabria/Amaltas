from django.shortcuts import render
from stalls.models import stall_frame,stall_products
from accounts.models import EmailData
from .forms import EmailForm
# Create your views here.

def index(request):
	stalls = stall_frame.objects.all()
	products = stall_products.objects.all()
	present_categories = []
	check_categories = []
	message = ''
	form = EmailForm(None)
	for product in products:
		if (product.category not in check_categories):
			check_categories.append(product.category)
			present_categories.append(product)
	if request.method=='POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			form.save()
			message = 'Thank you. We will send you updates soon'
	index_info = {
		'stalls':stalls,
		'present_categories':present_categories,
		'message':message,
		'form':form
	}
	return render(request,"index.html",index_info)

def aboutus(request):
	return render(request,"about_us.html")

def termsandconditions(request):
	return render(request,"terms_and_conditions.html")	
