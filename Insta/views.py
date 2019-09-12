from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Post
# Create your views here.
# Listview enables master/detail framwork
# .model Post defined in app Insta (title + image post)

class HelloDjango(TemplateView):
    template_name = 'test.html'

class PostListView(ListView):
    model = Post
    template_name = 'index.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
