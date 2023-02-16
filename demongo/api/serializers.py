from rest_framework_mongoengine import serializers
from rest_framework_mongoengine.fields import ObjectIdField
from .models import TsunBlog

class BlogSerializer(serializers.DocumentSerializer):
    class Meta:
        model = TsunBlog
        fields = ('__all__')