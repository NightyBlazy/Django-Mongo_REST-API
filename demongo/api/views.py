from django.http import QueryDict
from django.shortcuts import render
from datetime import datetime

from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import BlogSerializer

from .models import TsunBlog
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
		'Get All Blogs':'/getblogs/',
		'Get One Blog':'/getblog/<str:pk>/',
		'Create Blog':'/blogadd/',
		'Delete Blog':'/blogdelete/<str:pk>/',
		}
    return Response(api_urls)


@api_view(['GET'])
def getBlogs(request):
    blogs = TsunBlog.objects.all()
    serializer = BlogSerializer(blogs, many=True)  
    return Response(serializer.data)


@api_view(['GET'])
def getBlog(request, pk):
    blog = TsunBlog.objects.get(id = pk)
    
    serializer = BlogSerializer(blog, many=False)  
    return Response(serializer.data)

@api_view(['POST'])
def blogAdd(request):
    if isinstance(request.data, QueryDict): # optional
        request.data._mutable = True
    now = datetime.now();
    request.data['preview'] = request.data['body'][0:30]
    request.data['date'] = now.strftime("%Y/%m/%d, %H:%M:%S")
    
     
    serializer = BlogSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.data)
        print(type(serializer.data))
    
    blogs = TsunBlog.objects.all()
    serializer = BlogSerializer(blogs, many=True)    
    return Response(serializer.data)

@api_view(['DELETE'])
def blogDelete(request, pk):
    blog = TsunBlog.objects.get(id = pk)
    blog.delete()
    
    blogs = TsunBlog.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)