from django.urls import path
from . import views

urlpatterns = [
    path('',views.reactor,name="reactor"),
]
