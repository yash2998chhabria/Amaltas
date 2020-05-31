from django.shortcuts import render
from stalls.models import stall_frame,stall_products

# Create your views here.

def categorize(request,name):
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
					'stall': stall
					} 				
					return render(request,"product_page.html",prod)
	if	len(prod_list) !=0:				
		prod_info ={
			'products':prod_list,
			'category':name
		}		
		return render(request,'specific_category.html',prod_info)	

def display_all(request):
	products = stall_products.objects.all()
	present_categories = []
	check_categories = []
	for product in products:
		if (product.category not in check_categories):
			check_categories.append(product.category)
			present_categories.append(product)		
	return render(request,"all_categories.html",{'present_categories':present_categories})
							