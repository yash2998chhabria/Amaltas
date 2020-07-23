from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import EditStallFrameForm,EditStallProductsForm
from stalls.models import stall_frame, stall_products
from django.contrib.auth.decorators import login_required
# Create your views here.

def loginpage(request):
	if request.user.is_authenticated:
		frame = stall_frame.objects.filter(stall_user=request.user.id)
		products = None
		if frame:
			disabled = False	
			products = stall_products.objects.filter(stall_name=frame[0].id)
			check_premium = frame[0].premium
			check_poweredby = frame[0].poweredby_stall
			if check_poweredby and len(products)>49:
				disabled = True
			elif check_premium and len(products)>39:
				disabled = True 	
			elif check_poweredby == False and check_premium == False and len(products)>29:
				disabled = True

			context = {
					   'frame':frame[0],
				       'products':products,
				       'disabled':disabled
					 }

			return render(request,"exhibitor-admin.html",context)
		else:
			context= {'frame':None}
			return render(request,"exhibitor-admin.html",context)	
	else:	
		if request.method == 'POST':
			username = request.POST.get('Exhibitor')
			password = request.POST.get('password')
			user = authenticate(request, username = username, password=password)
			if user is not None:
				login(request, user)
				frame = stall_frame.objects.filter(stall_user=request.user.id)
				products = None
				if frame:
					disabled = False	
					products = stall_products.objects.filter(stall_name=frame[0].id)
					check_premium = frame[0].premium
					check_poweredby = frame[0].poweredby_stall
					if check_poweredby and len(products)>49:
						disabled = True
					elif check_premium and len(products)>39:
						disabled = True 	
					elif check_poweredby == False and check_premium == False and len(products)>29:
						disabled = True

					context = {
							   'frame':frame[0],
						       'products':products,
						       'disabled':disabled
							 }
					return render(request,"exhibitor-admin.html",context)		 
				else:		 
					context= {'frame':None}		 
					return render(request,"exhibitor-admin.html",context)		 
			else:
				messages.info(request,"Exhibitor ID or password is incorrect")	
				return 	render(request,"loginpage.html")
		return 	render(request,"loginpage.html")


@login_required(login_url='login')
def logoutuser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
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

@login_required(login_url='login')
def editstallproduct(request,pk):
	product = stall_products.objects.get(id=pk)
	form = EditStallProductsForm(instance=product)
	if request.method== 'POST':
		form = EditStallProductsForm(request.POST, request.FILES, instance=product)
		if form.is_valid():
			form.save()
			frame = stall_frame.objects.filter(stall_user=request.user.id)
			#stall_products.objects.filter(id=pk).update(stall_name=frame[0].id)
			return redirect('login')
	context= {
			'stall': stall_frame.objects.get(name=product.stall_name),
			'form':form,
			'heading':'Edit Your Product Information'
	}
	return render(request,"edit_products.html",context)

@login_required(login_url='login')
def createstallframe(request):
	form = EditStallFrameForm(None)
	if request.method=='POST':
		form = EditStallFrameForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			#stall_frame.objects.filter(stall_user=1).update(stall_user=request.user.id)
			return redirect('login')
	context = {
				'form':form,
				'heading': 'Create Your Stall Frame'
			 }					
	return render(request,"edit_stall.html",context)


@login_required(login_url='login')
def createstallproduct(request,stallname):
	form = EditStallProductsForm(None)
	if request.method=='POST':
		form = EditStallProductsForm(request.POST, request.FILES)
		if form.is_valid():
			product_name = form.cleaned_data['product_name']
			form.save()
			#frame = stall_frame.objects.filter(stall_user=request.user.id)
			#stall_products.objects.filter(product_name=product_name).update(stall_name=frame[0].id)
			return redirect('login')
	context = {
			'stall': stall_frame.objects.get(name=stallname),
			'form':form,
			'heading': 'Create Your Stall Product'
			}
	return render(request,"edit_products.html",context)

@login_required(login_url='login')
def deletestallproduct(request,pk):
	product = stall_products.objects.get(id=pk)
	if request.method=='POST':
		product.delete()
		return redirect('login')
	context = { 'name': product.product_name,
				'warning': 'The product will be permanently deleted if you choose to delete' }
	return render(request,"admin-delete.html",context)	

@login_required(login_url='login')
def deletestallframe(request,stall_name):
	if request.method=='POST':
		stall = stall_frame.objects.get(name=stall_name)
		stall.delete()
		return redirect('login')
	context = { 'name':stall_name,
				'warning':'If you delete the stall all the products will also get deleted' }
	return render(request,"admin-delete.html",context)

@login_required
def demo(request,name):
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
			'stall': stall,
			'contactno': int(str(stall.contact_no)[1:])
			}
			return render(request,'admin-products.html',prod)	
			
	for pro in product:
		if str(name) == str(pro.product_name):
			for stall in stalls:
				if str(pro.stall_name)==str(stall.name):
					prod={
					'product': pro,
					'stall': stall,
					'contactno': int(str(stall.contact_no)[1:])
					} 				
					return render(request,"admin-product_page.html",prod)