from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import EditStallFrameForm,EditStallProductsForm
from stalls.models import stall_frame, stall_products
# Create your views here.
def loginpage(request):
	if request.user.is_authenticated:
		frame = stall_frame.objects.filter(stall_user=request.user.id)
		products = None
		if frame:	
			products = stall_products.objects.filter(stall_name=frame[0].id)
			context = {'frame':frame[0],
				    'products':products
				 }
			return render(request,"admin.html",context)
		else:
			context= {'frame':None}
			return render(request,"admin.html",context)	
	else:	
		if request.method == 'POST':
			username = request.POST.get('Exhibitor ID')
			password = request.POST.get('password')
			user = authenticate(request, username = username, password=password)
			if user is not None:
				login(request, user)
				frame = stall_frame.objects.filter(stall_user=request.user.id)
				products = None
				if frame:	
					products = stall_products.objects.filter(stall_name= frame[0].id)		
					context = { 'frame':frame[0],
						    'products':products
						 }
					return render(request,"admin.html",context)		 
				else:		 
					context= {'frame':None}		 
					return render(request,"admin.html",context)		 
			else:
				messages.info(request,"Exhibitor ID or password is incorrect")	
				return 	render(request,"loginpage.html")
		return 	render(request,"loginpage.html")

def logoutuser(request):
	logout(request)
	return redirect('login')

def editstallframe(request):
	frame = stall_frame.objects.get(stall_user=request.user.id)
	form = EditStallFrameForm(instance=frame)
	if request.method== 'POST':
		form = EditStallFrameForm(request.POST, request.FILES, instance=frame)
		if form.is_valid():
			form.save()
			return redirect('login')		
	context = {
				'form':form,
				'heading': 'Edit Your Stall Frame'
			}	
	return render(request,"edit_stall.html",context)

def editstallproduct(request,product_name):
	product = stall_products.objects.get(product_name=product_name)
	form = EditStallProductsForm(instance=product)
	if request.method== 'POST':
		form = EditStallProductsForm(request.POST, request.FILES, instance=product)
		if form.is_valid()
			form.save()
			frame = stall_frame.objects.filter(stall_user=request.user.id)
			stall_products.objects.filter(product_name=product_name).update(stall_name=frame[0].id)
			return redirect('login')
	context= {
			'form':form,
			'heading':'Edit Your Product Information'
	}
	return render(request,"edit_stall.html",context)

def createstallframe(request):
	form = EditStallFrameForm()
	if request.method=='POST':
		form = EditStallFrameForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			stall_frame.objects.filter(stall_user=1).update(stall_user=request.user.id)
			return redirect('login')
	context = {
				'form':form,
				'heading': 'Create Your Stall Frame'
			 }					
	return render(request,"edit_stall.html",context)	

def createstallproduct(request):
	form = EditStallProductsForm()
	if request.method=='POST':
		form = EditStallProductsForm(request.POST, request.FILES)
		if form.is_valid():
			contact_stall = form.cleaned_data['contact_stall']
			form.save()
			frame = stall_frame.objects.filter(stall_user=request.user.id)
			stall_products.objects.filter(product_name=product_name).update(stall_name=frame[0].id)
			return redirect('login')
	context = {
			'form':form,
			'heading': 'Create Your Stall Product'
			}
	return render(request,"edit_stall.html",context)

def deletestallproduct(request,product_name):
	product = stall_products.objects.get(product_name=product_name)
	product.delete()
	return redirect('login')

