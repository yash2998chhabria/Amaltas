from rest_framework import serializers
from stalls.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Article
        # permission_classes = [
        #     permissions.AllowAny
        # ]
        fields = ['id','title','content','snippet','featured','date','author','blogimg','slug']

