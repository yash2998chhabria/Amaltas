from django.shortcuts import render
from .models import stall_frame,stall_products
from django_user_agents.utils import get_user_agent
# Create your views here.
def stalls(request):
	stall= stall_frame.objects.all()
	return render(request,"stalls.html",{'stalls': stall})

def products(request,name):
	product = stall_products.objects.all()
	stalls = stall_frame.objects.all()
	for stall in stalls:
		if str(name) == str(stall.name):			
			current_products = []
			for pro in product:
				if str(pro.stall_name) == str(name):
					current_products.append(pro)			
			prod = {
			'products': current_products,
			'stall': stall
			}
			if user_agent.is_mobile:
				return render(request,"products_mobile.html",prod)
			else:	
				return render(request,'products.html',prod)	
	for pro in product:
		if str(name) == str(pro.product_name):
			for stall in stalls:
				if str(pro.stall_name)==str(stall.name):
					prod={
					'product': pro,
					'stall': stall
					} 				
					return render(request,"product_page.html",prod)