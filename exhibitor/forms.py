from django import forms
from stalls.models import stall_frame,stall_products

class EditStallFrameForm(forms.ModelForm):
	class Meta:
		model = stall_frame
		fields = [
		'stall_user',
		'name',
		'cover',
		'description',
		'contact_stall',
		'city'
		]
		widgets={
				'stall_user': forms.HiddenInput()
		}

class EditStallProductsForm(forms.ModelForm):
	class Meta:
		model = stall_products
		fields = [
		'product_name',
		'price',
		'product_image',
		'category',
		'stall_name'
				]
		widgets = {
				#'stall_name': forms.HiddenInput(),
				#'stall_name': forms.TextInput(attrs={'disabled': True}),
		}