from django import forms
from accounts.models import EmailData
from .models import Testimonials

class EmailForm(forms.ModelForm):
	class Meta:
		model = EmailData
		fields = [
		'whatsapp'
		]
		
		widgets = {
					'whatsapp': forms.TextInput(attrs={'placeholder':"Enter your whatsapp number here",'value':""})
					}
		labels = {
					'whatsapp': ''
		}			

class TestiForm(forms.ModelForm):
	class Meta:
		model = Testimonials
		fields = [
			'name',
			'testi_image',
			'testi',
			#'make_visible'			
		]
		labels = {
					'name': 'NAME',
					'testi_image':'YOUR IMAGE',
					'testi':'TESTIMONIAL'
		}			
		help_texts = {
				'testi':'500 characters limit'
		}
