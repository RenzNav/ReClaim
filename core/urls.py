from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse, name='browse'),
    path('create-listing/', views.create_listing, name='create_listing'),
    path('requests/', views.requests, name='requests'),
]