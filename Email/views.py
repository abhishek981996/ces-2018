# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from app.models import Event,UserName,Email,PhoneNo,AdmissionNo,Branch,TeamName,Gender,Idea,Registration
from Email.form import SendEmailForm
import app.Constant as Constant
from django.contrib import messages as info
from django.core.mail import EmailMessage




@login_required
def SendMail(request):
	log = 0
	if request.method == 'POST':
		SendEmailform = SendEmailForm(request.POST)
		if SendEmailform.is_valid():
			subject = SendEmailform.cleaned_data['subject']
			body = SendEmailform.cleaned_data['body']
			value1 = SendEmailform.cleaned_data['Select_Event']
			event = Event.objects.get(id=value1)
			registraions = Registration.objects.filter(event=event)
			Email(registraions,subject,body)

			messages = "Email send succesfully"
			return render(request,'form.html',{'SendEmailform':SendEmailform,"messages":messages})
		
		message = "Error during validation of form, please fill correct email data"
		return render(request,'form.html',{'SendEmailform':SendEmailform,"message":message})
	else:
		SendEmailform = SendEmailForm()
		return render(request,'form.html',{'SendEmailform':SendEmailform})




def Email(registraions,subject,body):
	for user in registraions:
		email1 = str(user.email.emailid)
		email = EmailMessage(subject,body,to=[email1])
		value = email.send()

