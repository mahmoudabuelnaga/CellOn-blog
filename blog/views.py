from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from .models import Blog
# Create your views here.
class BlogListView(ListView):
    model = Blog
    template_name='home.html'

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'detail.html'

class BlogCreateView(CreateView): # new
    model = Blog
    template_name = 'post_new.html'
    fields = '__all__'