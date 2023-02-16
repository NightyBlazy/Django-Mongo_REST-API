from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="blogapi-Overview"),
    path('getblogs/', views.getBlogs, name="blogs-all"),
    path('getblog/<str:pk>/', views.getBlog, name="blog-detail"),
    path('blogadd/', views.blogAdd, name="task-create"),
    path('blogdelete/<str:pk>/', views.blogDelete, name="task-delete"),
]