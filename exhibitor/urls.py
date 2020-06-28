from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('login/',views.loginpage,name="login"),
path('logout/',views.logoutuser,name="logout"),
path('editstallframe/',views.editstallframe,name="editstallframe"),
path('createstallframe/',views.createstallframe,name="createstallframe"),
path('createstallproduct/',views.createstallproduct,name="createstallproduct"),
path('editstallproduct/<str:product_name>',views.editstallproduct,name="editstallproduct"),
path('deletestallproduct/<str:product_name>',views.deletestallproduct,name="deletestallproduct"),
path('<str:name>',views.demo,name="demo"),
] 
