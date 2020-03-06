from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# Register your models here.
class CustomUserAdmin(UserAdmin):
	ordering = ('-id',)
	list_display_links = ('username', 'mobile')
	list_display = ['username', 'email', 'mobile', 'gender', 'first_name', 'last_name']
	search_fields = ['username','email', 'mobile', 'gender', 'first_name', 'last_name']
	autocomplete_fields =['parent']
	add_fieldsets = (
		(None, {
			'classes': ('wide', 'extrapretty'),
			'fields': ('first_name', 'last_name', 'email', 'mobile', 'username', 'password1', 'password2' ),
		}),
	)
	fieldsets = [
		(None, {'fields': ('email', 'username', 'mobile', 'first_name', 'last_name', 'password',)}),
		('Personal info', {'fields': ('image', 'parent', 'gender', 'dob', 'about', 'address', 'country', 'city', 'postcode' )}),
		('Permissions', {'fields': ('is_active','is_staff','is_superuser', 'groups','user_permissions')}),
		('Important dates', {'fields': ('last_login','date_joined')})]

	

admin.site.register(User, CustomUserAdmin)
admin.site.register(AreaKey)
