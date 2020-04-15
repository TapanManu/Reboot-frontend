from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import GuserForm,GuidesForm,UserForm
from tourist.forms import TuserForm,InterestsForm
from .models import Guides
from tourist.models import Tourist
from django.contrib import auth 
from django.contrib.auth.models import User

def index(request):
	return render(request,'index.html',{})


def guides_signup(request):
	registered=False
	if request.method=='POST':
		guser_form=GuserForm(data=request.POST)
		g_form=GuidesForm(data=request.POST)
		if guser_form.is_valid() and g_form.is_valid() :
			user=guser_form.save()
			user.set_password(user.password)
			user.save()
			g_form=g_form.save(commit=False)
			registered=True
			auth.login(request,user)
			u=User.objects.get(username=request.user)
			g_form.guser=u
			g_form.save()
			context={
			'user':user
			}
			return render(request,'guides/home.html',context)

		else:
			print("false")

	else:
		guser_form=GuserForm()
		g_form=GuidesForm()
	return render(request,'guides/signup.html',{'user_form':guser_form,'g_form':g_form,'registered':registered})

def tourist_signup(request):
	registered=False
	if request.method=='POST':
		tuser_form=TuserForm(data=request.POST)
		i_form=InterestsForm(data=request.POST)
		if tuser_form.is_valid() and i_form.is_valid():
			user=tuser_form.save(commit=False)
			user.set_password(user.password)
			user.save()
			i_form=i_form.save(commit=False)
			registered=True
			auth.login(request,user)
			u=User.objects.get(username=request.user)
			i_form.tuser=u
			i_form.save()
			context={
			'user':user
			}
			return render(request,'tourist/home.html',context)

		else:
			print('false')
			#must create invalid signup page!
	else:
		tuser_form=TuserForm()
		i_form=InterestsForm()
	return render(request,'tourist/signup.html',{'user_form':tuser_form,'i_form':i_form,'registered':registered})	

def signin(request):
	error=False
	glist=[]
	tlist=[]
	user_form=UserForm(data=request.POST)
	staff = User.objects.filter(is_staff=True)
	print(tlist)
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=auth.authenticate(username=username,password=password)
		print(user.email)
		if user is not None and user.is_active:
			if user.email in u.email:
				auth.login(request,user)
				context={
				'user':user
					}
				return render(request,'guides/home.html',context)
			elif user.email in tlist:
				auth.login(request,user)
				context={
				'user':user
				}	
				return render(request,'tourist/home.html',context)
			#elif request.user in staff:
			#	auth.login(request,user)
			#	context={
			#	'user':user
			#	}	
			#	return render(request,'admin/home.html',context)
			else:
				error=True		

		else:
			error=True
			return render(request,'signin.html',{'user_form':user_form,'error':error})
	return render(request,'signin.html',{'user_form':user_form,'error':error})			
	
def signout(request):
	auth.logout(request)
	return render(request,'signout.html',{})


#	function onclick(event) {
 # gtag('event', 'click', {
  #  'event_action': 'button-footer-download'
  #});
#}