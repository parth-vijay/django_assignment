from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

app_name='home'

urlpatterns=[
	path('profile/', user_profile, name='user_profile'),
	path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
	path('logout/', logout_request, name='logout'),
	path('product/', product, name='product'),
	path('areakey/', areakey, name='areakey'),
	path('data/', table_data, name='table_data'),
	path('export/', csv_export, name='csv_export'),
	path('order/', place_order, name='place_order'),
	path('map/', map_view, name='map_view'),
	path('', home, name='home'),
]
