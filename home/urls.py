from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

app_name='home'

urlpatterns=[
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('', home, name='home'),
]
