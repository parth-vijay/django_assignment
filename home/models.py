from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import io
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

class AreaKey(models.Model):
	user=models.ForeignKey(User, on_delete=models.PROTECT)
	file=models.FileField(null=True)
	data=models.CharField(max_length=200, blank=True)
	rowdata=models.CharField(max_length=300, blank=True)
	complete=models.BooleanField(default=False)

	def __str__(self):
		return self.file.name

# @receiver(post_save, sender=AreaKey)
# def areakeyfn(sender, instance, **kwargs):
# 	filename=instance.file
# 	path=settings.BASE_DIR + '/media/' + str(filename)
# 	print(type(path))
# 	# print(str(filename))
# 	# fpath=path.encode('utf-8').strip()
# 	# print(fpath)
# 	f=io.open(path, 'r', encoding='utf-8')
# 	content=f.read()
# 	print(content)
