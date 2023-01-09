from django.contrib import admin
from django.urls import path, include

from pages.views import HomePageView, AboutPageView, PostDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name="post_detail"),
]
