from django.urls import path
from . import views

urlpatterns = [
    path('',views.stalls,name="stalls"),
    path('<str:stallname>',views.products,name="products"),
    path('<str:stallname>/<str:productname>',views.productpage,name="productpage"),
]
