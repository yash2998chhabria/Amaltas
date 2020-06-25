from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import EditStallFrame
from stalls.models import stall_frame, stall_products
# Create your views here.
def loginpage(request):
	if request.user.is_authenticated:
		frame = stall_frame.objects.get(stall_user=request.user.id)
		if frame:	
			products = stall_products.objects.filter(stall_name=frame.id)
			print(products)

		context = {'frame':frame}
		return render(request,"admin.html",context)
	else:	
		if request.method == 'POST':
			username = request.POST.get('Exhibitor ID')
			password = request.POST.get('password')
			user = authenticate(request, username = username, password=password)
			if user is not None:
				login(request, user)
				frame = stall_frame.objects.get(stall_user=request.user.id)
				context = {'frame':frame}
				return render(request,"admin.html",context)
			else:
				messages.info(request,"Exhibitor ID or password is incorrect")	
				return 	render(request,"loginpage.html")
		return 	render(request,"loginpage.html")

def logoutuser(request):
	logout(request)
	return redirect('login')	