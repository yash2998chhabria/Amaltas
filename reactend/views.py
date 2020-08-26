from django.shortcuts import render

# Create your views here.
def reactor(request):
    return render(request, "blog.html")
