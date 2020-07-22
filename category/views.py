from django.shortcuts import render
from stalls.models import stall_frame,stall_products,product_category,stall_city
from home.models import MakeVisible
# Create your views here.

def categorize(request,name):
	visibility = MakeVisible.objects.all()[0].start_exhibition
	products = stall_products.objects.all()
	stalls = stall_frame.objects.all()
	prod_list = []
	for product in products:
		if str(product.category) == str(name):
			prod_list.append(product)
		elif str(product.product_name) == str(name):
			for stall in stalls:
				if str(product.stall_name)==str(stall.name):
					prod={
					'product': product,
					'stall': stall,
					'visibility':visibility,
					'categories':product_category.objects.all(),
					'cities': stall_city.objects.all()
					} 				
					return render(request,"product_page.html",prod)
	if	len(prod_list) !=0:				
		prod_info ={
			'products':prod_list,
			'category':name,
			'visibility':visibility,
			'categories':product_category.objects.all(),
			'cities': stall_city.objects.all()
		}		
		return render(request,'specific_category.html',prod_info)	

def display_all(request):
	visibility = MakeVisible.objects.all()[0].start_exhibition
	print(visibility)
	products = stall_products.objects.all()
	present_categories = []
	check_categories = []
	for product in products:
		if (product.category not in check_categories):
			check_categories.append(product.category)
			present_categories.append(product)
	context = {
				'present_categories':present_categories,
				'visibility':visibility,
				'categories':product_category.objects.all(),
				'cities': stall_city.objects.all()				
				}				
	return render(request,"all_categories.html",context)
							