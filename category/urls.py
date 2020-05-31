from django.urls import path
from . import views

urlpatterns = [
	path('',views.display_all,name="display_all"),
    path('<name>',views.categorize,name="categorize")

]
