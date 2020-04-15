from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class Community(models.Model):
#class Skills(models.Model):
#	known_languages=models.CharField(max_length=30)
#	community=models.ManyToManyField(Community,null=True,blank=True)


class Guides(models.Model):
	guser=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
	email=models.EmailField(max_length=254)
	g_contact=models.CharField(max_length=10)
	date_of_join=models.DateTimeField(null=True,blank=True)
	tiers=models.IntegerField(null=True,blank=True)
	#date_of_completion=models.DateTimeField(null=True,blank=True)
	is_available=models.BooleanField(default=False,null=True,blank=True)
	base_rate=models.CharField(max_length=6,default='3000',null=True,blank=True)
	verified=models.BooleanField(default=False,null=True,blank=True)
	operating_level=models.CharField(max_length=10,default='state')
	location=models.CharField(max_length=40,null=True,blank=True)
	known_languages=models.CharField(max_length=30)
	reviews=models.TextField(max_length=350,null=True,blank=True)
	ratings=models.IntegerField(null=True,default=True)
	cuisines=models.TextField(default='kerala cuisines',max_length=40,null=True,blank=True)
	arts=models.TextField(default='kerala arts',max_length=40,null=True,blank=True)
	hotspots=models.TextField(default='kerala hotspots',max_length=40,null=True,blank=True)
	culture=models.TextField(default='kerala culture',max_length=30,null=True,blank=True)


	#idcard=upload aadhar card/valid identity card
	#users=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)	


	

#now i have added some null constraints to all fields for time being,need to develop for the better


