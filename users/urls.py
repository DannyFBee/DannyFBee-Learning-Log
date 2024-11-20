"""Defines URL patterns for users."""

from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'users'
urlpatterns = [
	# Include default auth urls. 
	path('users/', include('django.contrib.auth.urls')),
	# Registration page.
	path('register/', views.register, name='register'),
	# Logout page attempt.
	path('logout/', views.logout_view, name='logout'),
	# path('logout/', LogoutView.as_view(), name='logout'),	
]
