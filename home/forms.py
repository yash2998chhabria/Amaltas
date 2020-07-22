from django import forms
from accounts.models import EmailData

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