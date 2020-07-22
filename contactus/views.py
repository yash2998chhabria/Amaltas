from django.shortcuts import render
from .models import contact_info
from .forms import ContactForm
 #Create your views here.
def contactus(request):
	form = ContactForm(None)
	return render(request,"contact.html",{'form': form})


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