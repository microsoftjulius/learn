from django.contrib import admin
from django.urls import path, include

from pages.views import home_page_view

urlpatterns = [
    path('',home_page_view, name="home"),
]