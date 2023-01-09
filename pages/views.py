from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from pages.models import Pages


# Create your views here.
class HomePageView(ListView):
    model = Pages
    template_name = 'pages/home.html'
    context_object_name = 'all_posts_list'


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
