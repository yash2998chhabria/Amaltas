from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_cities,name="all_cities"),
    path('<city_name>',views.city_stalls,name="city_stalls")
]
