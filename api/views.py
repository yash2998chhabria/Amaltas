from rest_framework.generics import ListAPIView,RetrieveAPIView
from .serializers import ArticleSerializer
from stalls.models import Article
from rest_framework import viewsets




class ArticleView(viewsets.ModelViewSet):
   
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()





# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = 
