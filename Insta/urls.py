"""MyInstagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from Insta.views import HelloDjango, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', HelloDjango.as_view(), name='helloworld'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='make_post'),
    path('post/update/<int:pk>/', PostUpdateView.as_view(), name='update_post'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='delete_post'),
]



"""
urlpatterns = [
    url(r'^$', HelloDjango.as_view(), name='helloworld'),
    url(r'^posts', PostListView.as_view(), name='posts'),
    url(r'^post/(?P<pk>\d+)', PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/', PostCreateView.as_view(), name='make_post'),
    url(r'^post/update/(?P<pk>\d+)', PostUpdateView.as_view(), name='update_post'),
]

"""
