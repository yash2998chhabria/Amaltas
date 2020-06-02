from django import forms
from .models import contact_info

class ContactForm(forms.ModelForm):
	class Meta:
		model = contact_info
		fields = [
		'full_name',
		'email',
		'mobilenumber',
		'message'
		]
		
		widgets = {
					'full_name': forms.TextInput(attrs={'placeholder':'Enter your Full Name here'}),
					'email': forms.TextInput(attrs={'placeholder':"Enter your Email Id here"}),
					'mobilenumber': forms.TextInput(attrs={'placeholder':"Enter your Mobile number here"}),
					'message': forms.TextInput(attrs={'placeholder':'Enter your Message here'})
					}

		labels = {
					'full_name': 'Full Name:',#Full Name:
					'email':'Email:',#Email:
					'mobilenumber':'Mobile Number:',#Mobile Number:
					'message':'Message:'#Message:


		}