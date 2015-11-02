import os
import logging
import httplib2
import io
import hashlib, zlib
import short_url

from django.shortcuts import render

from apiclient.discovery import build
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseRedirect
from oauth2client import xsrfutil
from oauth2client.client import flow_from_clientsecrets
from oauth2client.django_orm import Storage

my_secret = "michnorts"

CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), '../static/', 'client_secret_01.json')

FLOW = flow_from_clientsecrets( CLIENT_SECRETS,
	scope='https://www.googleapis.com/auth/calendar',
	redirect_uri='http://localhost:8000/oauth2callback/')

def index(request):
	context = {}
	return 	render(request, 'index.html', context)

def weather(request):
	context = {}
	return 	render(request, 'weather.html', context)

def account(request):
	context = {}
	return render(request, 'account.html', context)

def login(request):
	context={}
	return render(request, 'login.html',context)

def login_google(request):
	authorize_url = FLOW.step1_get_authorize_url()
	return HttpResponseRedirect(authorize_url)

def credential_google(request):
	credential = FLOW.step2_exchange(request.GET['code'])#JH 20150924

	output = io.StringIO()
	http = httplib2.Http()
	http = credential.authorize(http)

	service = build('calendar', 'v3', http=http)
	request = service.events().list(calendarId='primary')

	while request != None:
		response = request.execute()
		for event in response.get('items', []):
			output.write(repr(event.get('summary', 'NO SUMMARY')) + '\n')
		request = service.events().list_next(request, response)
	return HttpResponse(output.getvalue())