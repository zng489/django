from rest_framework import serializers
from .models import BlogPost
from .models import Product
from .models import Data

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'published_date']


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'sale_price', 'my_discount']

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        



#####################################################################################
# GENERICS.LISTCREATEAPIVIEW 
#####################################################################################

from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = '__all__'



#####################################################################################
# API_VIEW['POST', 'GET', 'DELETE', 'PUT']
#####################################################################################

from rest_framework import serializers
from .models import DataRecord

class DataRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataRecord
        fields = '__all__'