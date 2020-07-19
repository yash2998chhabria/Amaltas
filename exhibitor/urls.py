from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('login/',views.loginpage,name="login"),
path('logout/',views.logoutuser,name="logout"),
path('editstallframe/',views.editstallframe,name="editstallframe"),
path('createstallframe/',views.createstallframe,name="createstallframe"),
path('createstallproduct/<str:stallname>',views.createstallproduct,name="createstallproduct"),
path('editstallproduct/<int:pk>',views.editstallproduct,name="editstallproduct"),
path('deletestallproduct/<int:pk>',views.deletestallproduct,name="deletestallproduct"),
path('deletestallframe/<str:stall_name>',views.deletestallframe,name="deletestallframe"),
path('demo/<str:name>',views.demo,name="demo"),
] 
