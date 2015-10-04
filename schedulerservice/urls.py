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
from django.conf.urls import patterns, url
from schedulerservice.views import *

urlpatterns = patterns('',
    url(r'^scheduler$', 'schedulerservice.views.index', name='home'),
    url(r'^$', 'schedulerservice.views.index', name='home'),
    url(r'^account$', 'schedulerservice.views.account', name='home'),
    url(r'^login/(?P<fake_user>.+)$','schedulerservice.views.login_google',name='login_google'),
    url(r'^oauth2callback','schedulerservice.views.credential_google', name='credential_google')
)
