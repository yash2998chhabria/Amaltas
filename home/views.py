from django.shortcuts import render
from stalls.models import stall_frame, stall_products, product_category, stall_city
from accounts.models import EmailData
from .forms import EmailForm, TestiForm
from django_user_agents.utils import get_user_agent
from .models import PageCounter, MakeVisible, Testimonials
from contactus.forms import ContactForm
from makeadifference.models import MakeADifference

# Create your views here.


def index(request):
    visibility = MakeVisible.objects.all()[0].start_exhibition
    stalls = stall_frame.objects.all()
    products = stall_products.objects.all()
    present_categories = []
    check_categories = []
    message = ''
    messagetesti = ''
    form = ContactForm(None)
    testiform = TestiForm(None)
    '''
    for product in products:
        if (product.category not in check_categories):
            check_categories.append(product.category)
            present_categories.append(product)
    '''        
    if request.method == 'POST':
        if 'messageform' in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                message = 'Thank you for the message. We will get in touch with you soon'
        if 'testiform' in request.POST:
            testiform = TestiForm(request.POST, request.FILES)
            if testiform.is_valid():
                testiform.save()
                messagetesti = 'Thank you for the Testimonial. We will display it soon'            
    index_info = {
        'stalls': stalls,
        #'present_categories': present_categories,
        'message': message,
        'messagetesti': messagetesti,
        'form': form,
        'Testimonialform':testiform,
        'visibility': visibility,
        'categories': product_category.objects.all(),
        'cities': stall_city.objects.all(),
        'mads': MakeADifference.objects.all(),
        'Testimonials': Testimonials.objects.all()
    }
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return render(request, "mobile_index.html", index_info)
    else:
        return render(request, "index.html", index_info)


def aboutus(request):
    return render(request, "about_us.html")


def termsandconditions(request):
    context = {
        'categories': product_category.objects.all(),
        'cities': stall_city.objects.all(),
    }
    return render(request, "terms_and_conditions.html", context)
