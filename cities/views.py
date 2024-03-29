from django.shortcuts import render
from stalls.models import stall_city,stall_frame,product_category,stall_city
from home.models import MakeVisible
from home.forms import EmailForm

# Create your views here.
def all_cities(request):
	visibility = MakeVisible.objects.all()[0].start_exhibition
	cities = stall_city.objects.all()
	def get_name(city):
		return city.name
	sorted_cities=sorted(cities,key=get_name)
	city_list = {
	'cities':sorted_cities,
	'visibility':visibility,
	'categories':product_category.objects.all(),
    'cities': stall_city.objects.all()
	}
	return render(request,'cities.html',city_list)

def city_stalls(request,city_name):
	visibility = MakeVisible.objects.all()[0].start_exhibition
	stalls = stall_frame.objects.all()
	current_stalls=[]
	form = EmailForm(None)
	message = ''
	if request.method=='POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			form.save()
			message = 'Thank you. We will send you updates soon'		
	for stall in stalls:
		if str(stall.city) == str(city_name):
			current_stalls.append(stall)
	context = {
				'stalls':current_stalls,
				'visibility':visibility,
				'categories':product_category.objects.all(),
    			'cities': stall_city.objects.all(),
				'message':message,
				'form':form,
			}		
	return render(request,"stalls.html",context)
