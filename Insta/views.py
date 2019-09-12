from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy # for success_url
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

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    # ask for provide all info
    fields = '__all__'

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = ['title'] # only title is allowed to be updated

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    # reverse would cause circular situation
    # reverse_lazy enables access and delete at the same time 
    success_url = reverse_lazy('posts')
