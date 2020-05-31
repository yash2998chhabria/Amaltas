from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import EmailData

'''
def registeremail:
	if request.method=='POST'
		email = request.POST['email']
		newemail  = EmailData.objects.create(email=email)
		newemail.save()
		message = 'Thank you. We will get in touch with you soon'
		return render(request,'index.html',{'message':message})
'''
# Create your views here.
def login(request):
	return render(request,"login.html")

def register(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		user= User.objects.create_user(password=password1,email=email,first_name=first_name,last_name=last_name)
		user.save();
		print('user_created')
		return redirect('/')
	else:
		return render(request,"login.html")	

