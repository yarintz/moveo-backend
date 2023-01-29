from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class CodeBlockViewSet(viewsets.ModelViewSet):
    queryset = CodeBlock.objects.all()
    serializer_class = CodeBlockSerializer 
    # permission_classes = (AllowAny,)

