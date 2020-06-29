from django.shortcuts import render
from .models import stall_frame,stall_products
from home.models import MakeVisible

# Create your views here.
def stalls(request):
	stall= stall_frame.objects.all()
	visibility = MakeVisible.objects.all()[0].start_exhibition
	context = {
				'stalls': stall,
				'visibility':visibility
				}

	return render(request,"stalls.html",context)

def products(request,name):
	product = stall_products.objects.all()
	stalls = stall_frame.objects.all()
	visibility = MakeVisible.objects.all()[0].start_exhibition
	for stall in stalls:
		if str(name) == str(stall.name):			
			current_products = []
			for pro in product:
				if str(pro.stall_name) == str(name):
					current_products.append(pro)			
			prod = {
			'products': current_products,
			'stall': stall,
			'visibility':visibility
			}
			return render(request,'products.html',prod)	
			
	for pro in product:
		if str(name) == str(pro.product_name):
			for stall in stalls:
				if str(pro.stall_name)==str(stall.name):
					prod={
					'product': pro,
					'stall': stall,
					'visibility':visibility
					} 				
					return render(request,"product_page.html",prod)