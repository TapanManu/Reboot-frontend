from django.urls import path
from .import views
from django.contrib import auth

app_name='guides'
urlpatterns=[
path('',views.index,name='index'),
path('guides/signup',views.guides_signup,name='guides_signup'),
path('tourist/signup',views.tourist_signup,name='tourist_signup'),
path('signin',views.signin,name='signin'),
path('signout',views.signout,name='signout'),
]
