from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from pages.models import Pages


# Create your views here.
class HomePageView(ListView):
    model = Pages
    template_name = 'pages/home.html'
    context_object_name = 'all_posts_list'


class PostDetailView(DetailView):
    model = Pages
    template_name = 'pages/post_detail.html'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'


class PostCreateView(CreateView):
    model = Pages
    template_name = 'pages/post_new.html'
    fields = ['uuid', 'text', 'author', 'body']


class PostEditView(UpdateView):
    model = Pages
    template_name = 'pages/post_edit.html'
    fields = ['uuid', 'text', 'body']


class PostDeleteView(DeleteView):
    model = Pages
    template_name = 'pages/post_delete.html'
    success_url = reverse_lazy('home')
