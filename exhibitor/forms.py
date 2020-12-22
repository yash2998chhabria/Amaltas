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
		'category',
		'second_category',
		'third_category',
		'contact_no',
		'contact_stall',
		'city',
		'stall_visible_on_website'
		]
		widgets={
				'stall_user': forms.TextInput({'id':'putstallname','value':'','type':'hidden'}),
				#'stall_visible_on_website': forms.TextInput(attrs={'disabled': True})
		}
		help_texts = {
				'contact_no':"Enter your Whatsapp contact number. Customers will contact you directly using this number",
				'name': "limit the name to one or two words",
				'cover':"please upload only a 1:1 sqaure aspect ratio image(if not, it will get cropped)",
				'description':"please restrict the description to around 30 words or less",
				'stall_visible_on_website': "This will work only during an exhibition",
				'contact_stall':"Additional Contact Details",
				'second_category':"If you dont want to choose a second category, leave this field as is",
				'third_category':"If you dont want to choose a third category, leave this field as is"
		}

class EditStallProductsForm(forms.ModelForm):
	class Meta:
		model = stall_products
		fields = [
		'product_name',
		'price',
		'product_image',
		'stall_name',
		'position',
		'weblink'
				]
		widgets = {
				'stall_name': forms.TextInput({'id':'putstallname','value':'','type':'hidden'}),
		}
		help_texts = {
				'product_name':'please do not to repeat product names. Do not use "/" in the product name ',
				'price':'if price is not required leave the field as 0',
				'product_image':'product images must be of a 1:1 sqaure aspect ratio(if not,it will get cropped)',
				'position':'leave position as 0 if its not neccessary',
				'weblink': "Enter your Product's website link(optional). As an alternative to using the whatsapp to connect to customers"
		}