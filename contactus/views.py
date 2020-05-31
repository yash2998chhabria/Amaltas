from django.shortcuts import render
from .models import contact_info
from .forms import ContactForm
 #Create your views here.
def contactus(request):
	form = ContactForm(None)
	return render(request,"contact.html",{'form': form})

'''
def saveform(request):
	if request.method == 'POST':
		full_name = request.POST['full_name']
		email = request.POST['email']
		mobilenumber = request.POST['mobilenumber']
		message = request.POST['message']
		newcontactform = contact_info.objects.create(full_name=full_name,email=email,mobilenumber=mobilenumber,message=message)
		newcontactform.save()
		message = 'Thank you. We will get in touch with you soon'
		return render(request,"contact.html", {'message': message} )
'''

def saveform(request):
	form = ContactForm(request.POST)
	if form.is_valid():
		form.save()
		message = 'Thank you for the message. We will get in touch with you soon'
		context = {
		'form':form,
		'message': message
		}	
	return render(request,"contact.html",context)		