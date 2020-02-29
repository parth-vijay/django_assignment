from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

gender = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))

class User(AbstractUser):
	parent = models.ForeignKey("self", verbose_name="Parent", on_delete=models.PROTECT, blank=True, null=True)
	email = models.EmailField(blank=False)
	mobile = models.CharField(max_length=15)
	gender = models.CharField(max_length=6, choices=gender, default='Male')
	dob = models.DateField(null=True, blank=True)
	image = models.ImageField(upload_to='user/', blank=True, null=True)
	about = models.TextField(blank=True)
	city = models.CharField(max_length=50, blank=True, null=True)
	country = models.CharField(max_length=50, blank=True, null=True)
	address = models.TextField(blank=True)
	postcode = models.CharField(max_length=10, blank=True, null=True)

	class Meta:
		verbose_name_plural = "Users"

	def __str__(self):
		return str(self.username)

