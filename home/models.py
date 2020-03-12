from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import io
from django.core.files.storage import default_storage
import json
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
	data=models.TextField(blank=True)
	rowdata=models.TextField(blank=True)
	complete=models.BooleanField(default=False)

	def __str__(self):
		return self.file.name

@receiver(post_save, sender=AreaKey)
def areakeyfn(sender, instance, **kwargs):
	filename=instance.file
	path=settings.BASE_DIR + '/media/' + str(filename)
	f=open(path, 'r')
	content=f.read()
	instance.data=content
	d = instance.data.split('\n')
	AreaKey.objects.filter(id=instance.id).update(data=d)
	del d[0]
	d.remove('')
	a=[]
	b=[]
	for i in d:
		x=i.split(',')
		a={'cust_name':x[0]}
		a.update({'order_num':x[1]})
		a.update({'date':x[2]})
		a.update({'post':x[3]})
		b+=[a]
	c=json.dumps(b)	
	AreaKey.objects.filter(id=instance.id).update(rowdata=c)
	f.close()
