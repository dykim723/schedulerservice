"""schedulerservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, url, include
from django.contrib import admin
from schedulerservice.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^scheduler$', 'schedulerservice.views.index', name='home'),
    url(r'^index', 'schedulerservice.views.index', name='home'),
    url(r'^weather', 'schedulerservice.views.weather', name='weather'),
    url(r'^account$', 'schedulerservice.views.account', name='home'),
    url(r'^login$','schedulerservice.views.login',name='login'),
    url(r'^login/google$','schedulerservice.views.login_google',name='login_google'),
    url(r'^oauth2callback','schedulerservice.views.credential_google', name='credential_google'),
    url(r'^admin/', include(admin.site.urls)),    
    # if the URL pattern match /admin/ then open up admin panel 
    url(r'', include('shortenerSite.urls', namespace='shortenerSite')),
    # if anything rather then /admin/ then it will look for shortenerSite/urls

)