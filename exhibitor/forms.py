from django import forms
from stalls.models import stall_frame

class EditStallFrame(forms.ModelForm):
	class Meta:
		model = stall_frame
		fields = [
		'name',
		'cover',
		'description',
		'contact_stall',
		'city'
		]