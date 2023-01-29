from rest_framework import serializers
from .models import *

class CodeBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CodeBlock
        fields = ('id','title', 'code', 'solution') 