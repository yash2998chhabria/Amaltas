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
		'contact_no',
		'contact_stall',
		'city',
		'stall_visible_on_website'
		]
		widgets={
				'stall_user': forms.HiddenInput(),
				#'stall_visible_on_website': forms.TextInput(attrs={'disabled': True})
		}
		help_texts = {
				'contact_no':"Enter your Whatsapp contact number. Customers will contact you directly using this number",
				'name': "limit the name to one or two words",
				'cover':"please upload only a 16:9 aspect ratio image(if not, it will get cropped)",
				'description':"please restrict the description to one line and around 10 words or less",
				'stall_visible_on_website': "This will work only during an exhibition",
				'contact_stall':"Additional Contact Details"
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
				'stall_name': forms.TextInput({'id':'putstallname','value':'','type':'hidden'}),
		}
		help_texts = {
				'product_name':'please try not to repeat product names. Product names should not be the same as stall names',
				'price':'if price is not required leave the field as 0',
				#'product_image':'product images must be of a sqaure aspect ratio(if not,it will get cropped)'
		}