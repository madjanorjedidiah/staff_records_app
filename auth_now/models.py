from django.db import models
from django.contrib.auth.models import AbstractUser


class UserIdentity(AbstractUser):
	conatact = models.CharField(max_length=13, null=True, blank=True)


class UserBioInfo(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	department = models.CharField(max_length=100, null=True, blank=True)
	role = models.CharField(max_length=100, null=True, blank=True)
	title = models.CharField(max_length=100, null=True, blank=True)
	gender = models.CharField(max_length=5, null=True, blank=True)
	last_cert_date = models.CharField(max_length=100, null=True, blank=True)
	image = models.FileField(upload_to='users', null=True, blank=True)
	user_fk = models.ForeignKey(UserIdentity, on_delete=models.CASCADE)
