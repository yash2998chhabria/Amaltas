from .views import ArticleView
from django.urls import path,include


from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleView, basename='userviewset')
urlpatterns = router.urls

