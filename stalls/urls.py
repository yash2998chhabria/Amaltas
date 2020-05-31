from django.urls import path
from . import views

urlpatterns = [
    path('',views.stalls,name="stalls"),
    path('<name>',views.products,name="products"),
]
