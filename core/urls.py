from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('browse/', views.browse, name='browse'),
    path('create-listing/', views.create_listing, name='create_listing'),
    path('requests/', views.requests, name='requests'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('my-listings/', views.my_listings, name='my_listings'),
    path('my-listings/<int:listing_id>/edit/', views.edit_listing, name='edit_listing'),
    path('my-listings/<int:listing_id>/delete/', views.delete_listing, name='delete_listing'),
]