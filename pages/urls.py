from django.contrib import admin
from django.urls import path, include

from pages.views import HomePageView, AboutPageView, PostDetailView, PostCreateView, PostEditView, PostDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('post-detail/<int:pk>', PostDetailView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name="post_new"),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name="post_edit"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
]
