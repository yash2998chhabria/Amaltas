from django.shortcuts import render
from .models import stall_frame,stall_products,product_category,stall_city
from home.models import MakeVisible
from home.forms import EmailForm

# Create your views here.
def stalls(request):
	stall= stall_frame.objects.all()
	def get_position(stall):
		return stall.position
	stall=sorted(stall,key=get_position)
	visibility = MakeVisible.objects.all()[0].start_exhibition
	form = EmailForm(None)
	message = ''
	if request.method=='POST':
		form = EmailForm(request.POST)
		if form.is_valid():
			form.save()
			message = 'Thank you. We will send you updates soon'
	context = {
				'stalls': stall,
				'visibility':visibility,
				'message':message,
				'form':form,
				'categories':product_category.objects.all(),
				'cities': stall_city.objects.all()				
				}

	return render(request,"stalls.html",context)

'''
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
'''

def products(request,stallname):
	stall = stall_frame.objects.get(slug=stallname)
	product = stall_products.objects.filter(stall_name = stall)
	visibility = MakeVisible.objects.all()[0].start_exhibition
	prod = {
			'products': product,
			'stall': stall,
			'visibility':visibility,
			'categories':product_category.objects.all(),
			'cities': stall_city.objects.all(),
			'contactno': int(str(stall.contact_no)[1:])		
			}
	return render(request,'products.html',prod)



def productpage(request,stallname,productname):
	stall = stall_frame.objects.get(name=stallname)
	product = stall_products.objects.get(product_name=productname)
	visibility = MakeVisible.objects.all()[0].start_exhibition
	prod = {
		'product': product,
		'stall': stall,
		'visibility':visibility,
		'categories':product_category.objects.all(),
		'cities': stall_city.objects.all(),
		'contactno': int(str(stall.contact_no)[1:])
	}	

	return render(request,'product_page.html',prod)


