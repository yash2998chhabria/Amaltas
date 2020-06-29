from django.shortcuts import render
from stalls.models import stall_city,stall_frame
from home.models import MakeVisible
# Create your views here.
def all_cities(request):
	visibility = MakeVisible.objects.all()[0].start_exhibition
	cities = stall_city.objects.all()
	def get_name(city):
		return city.name
	sorted_cities=sorted(cities,key=get_name)
	city_list = {
	'cities':sorted_cities,
	'visibility':visibility
	}
	return render(request,'cities.html',city_list)

def city_stalls(request,city_name):
	visibility = MakeVisible.objects.all()[0].start_exhibition
	stalls = stall_frame.objects.all()
	current_stalls=[]
	for stall in stalls:
		if str(stall.city) == str(city_name):
			current_stalls.append(stall)
	context = {
				'stalls':current_stalls,
				'visibility':visibility
			}		
	return render(request,"stalls.html",context)
