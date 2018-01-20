# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from datetime import date, datetime
import itertools as it

import json
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from app.models import Event,UserName,Email,PhoneNo,AdmissionNo,Branch,TeamName,Gender,Idea,Registration
from app.form import EventForm,EventFormExtra,UserNameForm,EmailForm,PhoneNoForm,AdmissionNoForm,BranchForm,TeamNameForm,GenderForm,IdeasForm
import app.Constant as Constant
import xlwt
from django.contrib import messages as info
from datetime import datetime




def grouper(n, iterable):
    """
    >>> list(grouper(3, 'ABCDEFG'))
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G']]
    """
    iterable = iter(iterable)
    return iter(lambda: list(it.islice(iterable, n)), [])


def Events(request):
	"""Display all the available events"""
	events =  Event.objects.all().order_by('-Dateime')
	if events:
		event_list = []
		for event in events:
			event_dict ={}
			event_dict['event_id'] = event.id
			event_dict['event_name'] = event.Eventname
			event_dict['location'] = event.Location

			event_dict['Datetime'] = event.Dateime
			print(event_dict['Datetime'])
			event_dict['Description'] = event.Description
			
			event_dict['download'] = event.document
				
			
			print(event_dict)
			
			event_list.append(event_dict)

		event_list = list(grouper(3, event_list))
		
		return render(request,"Events.html",{'event_list':event_list})
	else:
		return render(request,"Events.html")


@login_required
def AddEvent(request):
	"""Add Any event"""
	if request.method == 'POST':
		eventform = EventForm(request.POST,request.FILES)
		eventformextra = EventFormExtra(request.POST)
		

		if (eventform.is_valid() and eventformextra.is_valid()):
			event_form = eventform.save(commit=False)
			print(eventform.cleaned_data.get('Description'))
			event_form.RequiredFields = eventformextra.cleaned_data.get('RequiredField')
			print(event_form.RequiredFields)
			Dateime= datetime.combine(eventformextra.cleaned_data['Eventdate'], eventformextra.cleaned_data['EventTime'])

			event_form.Dateime = Dateime
			message = "Successfully Created " +eventform.cleaned_data['Eventname']+ "Event"
			
			event_form.save()
			
			info.add_message(request, info.INFO, message)
			return HttpResponseRedirect(Events)

	else:
		eventform = EventForm()
		eventformextra = EventFormExtra()
		return render(request,'Add_event.html',{'eventform':eventform,'eventformextra':eventformextra})


def Download(request,event_id):
	event = Event.objects.get(id=event_id)
	path = event.document.path
	file = open(path,"rb")
	response = HttpResponse(file,content_type='application/pdf')
	filename = '-'.join(event.Eventname.split(' '))
	filename = filename + "-Rules.pdf"
	#decide file name
	response['Content-Disposition'] = 'attachment; filename=' +filename


	print (path)

	return response


# @login_required
# def DeleteEvent(request):
# 	pass


# @login_required
# def EditEvent(request,event_id):
# 	event = get_object_or_404(Event, id = event_id)

# 	if request.method == "POST":
# 		eventform = EventForm(request.POST,request.FILES,instance=event)
# 		eventformextra = EventFormExtra(request.POST)
		

# 		if (eventform.is_valid() and eventformextra.is_valid()):
# 			event_form = eventform.save(commit=False)
# 			print(eventform.cleaned_data.get('Description'))
# 			event_form.RequiredFields = eventformextra.cleaned_data.get('RequiredField')
# 			print(event_form.RequiredFields)
# 			Dateime= datetime.combine(eventformextra.cleaned_data['Eventdate'], eventformextra.cleaned_data['EventTime'])

# 			event_form.Dateime = Dateime
# 			message = "Successfully Edited " +eventform.cleaned_data['Eventname']+ "Event"
			
# 			event_form.save()
			
# 			info.add_message(request, info.INFO, message)
# 			return HttpResponseRedirect("event/view_events/")
# 	else:
# 		eventform = EventForm(instance=event)
# 		eventformextra = EventFormExtra()

# 		message = "Add Required Fields, and date time"
# 		info.add_message(request, info.INFO, message)
# 		return render(request,'Add_event.html',{'eventform':eventform,'eventformextra':eventformextra})

 


