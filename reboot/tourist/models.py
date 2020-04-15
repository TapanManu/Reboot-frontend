from django.db import models
from django.contrib.auth.models import User


class Tourist(models.Model):
	tuser=models.ForeignKey(User,on_delete=models.CASCADE)
	email=models.EmailField(max_length=254)
	t_contact=models.CharField(max_length=10,null=True,blank=True)
	languages=models.CharField(max_length=30)
	locations=models.CharField(max_length=40,null=True,blank=True)
	interest_rate=models.IntegerField(blank=True,null=True)
	cultures=models.BooleanField(default=False,blank=True,null=True)
	def __str__(self):
		return self.tuser.username		


# Create your models here.
