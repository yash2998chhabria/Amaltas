from django.shortcuts import render
from stalls.models import stall_city,stall_frame
# Create your views here.
def all_cities(request):
	cities = stall_city.objects.all()
	def get_name(city):
		return city.name
	sorted_cities=sorted(cities,key=get_name)
	city_list = {
	'cities':sorted_cities
	}
	return render(request,'cities.html',city_list)

def city_stalls(request,city_name):
	stalls = stall_frame.objects.all()
	current_stalls=[]
	for stall in stalls:
		if str(stall.city) == str(city_name):
			current_stalls.append(stall)
			
	return render(request,"stalls.html",{'stalls':current_stalls})
