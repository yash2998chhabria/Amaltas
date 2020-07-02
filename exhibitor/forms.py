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
		'city',
		'stall_visible_on_website'
		]
		widgets={
				'stall_user': forms.HiddenInput(),
				#'stall_visible_on_website': forms.TextInput(attrs={'disabled': True})
		}
		help_texts = {
				'name': "stall name's should not be the same as product names, product names should not be repeated",
				'cover':"please upload only a 16:9 aspect ratio image(if not, it will get cropped)",
				'description':"please restrict the description to one line and around 10 words or less",
				'stall_visible_on_website': "This will work only during an exhibition"
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
		help_texts = {
				'product_name':'please try not to repeat product names. Product names should not be the same as stall names',
				'price':'if price is not required leave the field as 0',
				#'product_image':'product images must be of a sqaure aspect ratio(if not,it will get cropped)'
		}