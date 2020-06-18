from django.shortcuts import render
from stalls.models import stall_frame,stall_products
from accounts.models import EmailData
from .forms import EmailForm
from django_user_agents.utils import get_user_agent
from .models import PageCounter
# Create your views here.

def index(request):
	stalls = stall_frame.objects.all()
	products = stall_products.objects.all()
	present_categories = []
	check_categories = []
	message = ''
	load_first = ['1','2']
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
		'form':form,
		'load_first': load_first
	}
	user_agent = get_user_agent(request)
	count= PageCounter.objects.all()[0] 
	count.indexcounter += 1
	if (count.indexcounter % 10) ==0:
		print(count.indexcounter)
	count.save()
	if user_agent.is_mobile:
		return render(request,"mobile_index.html",index_info)
	else:	
		return render(request,"index.html",index_info)

def aboutus(request):
	return render(request,"about_us.html")

def termsandconditions(request):
	return render(request,"terms_and_conditions.html")	
