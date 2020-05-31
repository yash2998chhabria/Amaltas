from django import forms
from accounts.models import EmailData

class EmailForm(forms.ModelForm):
	class Meta:
		model = EmailData
		fields = [
		'email'
		]
		
		widgets = {
					'email': forms.TextInput(attrs={'placeholder':"Enter your Email Id here"})
					}