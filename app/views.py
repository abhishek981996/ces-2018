from datetime import date, datetime
import itertools as it

import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from app.models import Event,UserName,Email,PhoneNo,AdmissionNo,Branch,TeamName,Gender,Idea,Registration
from app.form import EventForm,EventFormExtra,UserNameForm,EmailForm,PhoneNoForm,AdmissionNoForm,BranchForm,TeamNameForm,GenderForm,IdeasForm
import app.Constant as Constant
import xlwt
from django.contrib import messages as info
from datetime import datetime


OPTIONS = (
	(1,Constant.UserName),
	(2,Constant.Emailid),
	(3,Constant.AdmissionNo),
	(4,Constant.PhoneNo),
	(5,Constant.Branch),
	(6,Constant.TeamName),
	(7,Constant.Idea),
	(8,Constant.Gender)

	)

# Create your views here.
@csrf_exempt
def Login(request):
	if request.method == "POST":
		username = request.POST['UserName']
		password = request.POST['Password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect(AddEvent)
		message = "Login failed,error login"
		return render(request,"login.html",{'error':message})
	elif request.user.is_authenticated:
		return redirect(AddEvent)
	else:
		return render(request,"login.html")
		
def Logout(request):
	logout(request)
	return redirect(Login)


def Index(request):
	"""The index page of Ces"""
	return render(request,"index.html")





def Registrations(request,event_id):
	"""Register for any event"""
	if request.method == "POST":

		try:
			event = Event.objects.get(id=event_id)
			required_fields = event.RequiredFields
			event_name = event.Eventname

		except:
			return HttpResponse("404 page not found")

		error_list = []
		required_field= []
		for fields in required_fields:
			required_field.append(int(fields))	


		if 1 in required_field:
			print ("username form")
			usernameform = UserNameForm(prefix='username_form',data = request.POST)
			username_form = usernameform.is_valid()
			if username_form != True:
				error_dict = usernameform.errors.as_data()
				for key, value in error_dict.items():
					for item in value:
						error_list.extend(item)
		else:
			usernameform = ''
			username_form = True


		if 2 in required_field:
			print ("email form")
			emailForm = EmailForm(prefix='email_form',data = request.POST)
			email_Form = emailForm.is_valid()
			if email_Form != True:
				error_dict = emailForm.errors.as_data()
				for key, value in error_dict.items():
					for item in value:
						error_list.extend(item)		
		else:
			emailForm = ''
			email_Form = True


		if 3 in required_field:
			print ("admission form")
			admissionnoform = AdmissionNoForm(prefix='admissionno_form',data = request.POST)
			admissionno_form = admissionnoform.is_valid()
			if admissionno_form != True:
				error_dict = admissionnoform.errors.as_data()
				for key, value in error_dict.items():
					for item in value:
						error_list.extend(item)
		else:
			admissionnoform = ''
			admissionno_form = True


		
		if 4 in required_field:
			print ("phoeno form")
			phonenoform = PhoneNoForm(prefix='phoneno_form',data = request.POST)
			phoneno_form = phonenoform.is_valid()
			if phoneno_form != True:
				error_dict = phonenoform.errors.as_data()
				for key, value in error_dict.items():
					for item in value:
						error_list.extend(item)
		else:
			phonenoform = ''
			phoneno_form = True


		if 5 in required_field:
			print ("Branch form")
			branchform = BranchForm(prefix='branch_form',data = request.POST)
			branch_form = branchform.is_valid()
			if branch_form != True:
				error_dict = branchform.errors.as_data()
				for key, value in error_dict.items():
					for item in value:
						error_list.extend(item)
		else:
			branchform = ''
			branch_form=True


		if 6 in required_field:
			print ("teamname form")
			teamname = TeamNameForm(prefix='teamname_form',data = request.POST)
			teamname_form = teamname.is_valid()
			if teamname_form != True:
				error_dict = teamname.errors.as_data()
				for key, value in error_dict.items():
					for item in value:
						error_list.extend(item)
		else:
			teamname = ''
			teamname_form = True

		
		if 7 in required_field:
			print ("idea form")
			ideasform = IdeasForm(prefix='Ideas_form',data = request.POST)
			ideas_form = ideasform.is_valid()
			if ideas_form != True:
				error_dict = ideasform.errors.as_data()
				for key, value in error_dict.items():
					for item in value:
						error_list.extend(item)
		else:
			ideasform = ''
			ideas_form=True


		if 8 in required_field:
			print ("gender form")
			genderform = GenderForm(prefix='Gender_form',data = request.POST)
			gender_form = genderform.is_valid()
			if gender_form != True:
				error_dict = genderform.errors.as_data()
				for key, value in error_dict.items():
					for item in value:
						error_list.extend(item)
		else:
			genderform = ''
			gender_form = True
		


		if (username_form and phoneno_form and admissionno_form and branch_form and teamname_form and gender_form and ideas_form and email_Form):
			event = Event.objects.get(id=event_id)
			new_registration = Registration.objects.create(event=event)
			if usernameform:
				username = usernameform.save()
				new_registration.username = username
		
			
			if emailForm:
				email = emailForm.save()
				new_registration.email = email
		

			if ideasform:
				ideas = ideasform.save()
				new_registration.idea = ideas
				print( 'hello idea')
		

			if teamname:
				team_name = teamname.save()
				new_registration.teamname = team_name
		

			if genderform:
				gender = genderform.save()
				new_registration.gender= gender
		

			if admissionnoform:
				admissionno = admissionnoform.save()
				new_registration.admissionno = admissionno
		

			if phonenoform:
				phoneno = phonenoform.save()
				new_registration.phoneno = phoneno
			

			if branchform:
				branch = branchform.save()
				new_registration.branch = branch
			

			# new_registration = Registration.objects.create(event=event , username=username,email = email,phoneno=phoneno,
			# 	admissionno = admissionno,branch = branch,teamname=team_name, idea = idea ,gender=gender)

			new_registration.save()

			message = "Successfully registered for the %s Event"%event.Eventname
			info.add_message(request, info.INFO, message)
			return HttpResponseRedirect("event/view_events/")
		else:
			return render(request,"registration.html",{
			'usernameform':usernameform,
			'emailForm':emailForm,
			'admissionnoform':admissionnoform,
			'phonenoform':phonenoform,
			'branchform':branchform,
			'teamname':teamname,
			'ideasform':ideasform,
			'genderform':genderform,
			'error_list':error_list
			})
		return HttpResponse("fail")
		

	else:
		usernameform = ''
		phonenoform=''
		admissionnoform = ''
		branchform = ''
		teamname = ''
		genderform = ''
		ideasform = ''
		emailForm = ''


		try:
			event = Event.objects.get(id=event_id)
			required_fields = event.RequiredFields
			event_name = event.Eventname
		except:
			return HttpResponse("404 page not found")

		required_field= []
		for fields in required_fields:
			required_field.append(int(fields))	
		
		print(required_field)
		print(type(required_field))
		


		if 1 in required_field:
			print ("username")
			usernameform = UserNameForm(prefix='username_form')

		if 2 in required_field:
			print ("email")
			emailForm = EmailForm(prefix='email_form')

		if 3 in required_field:
			print ("admission")
			admissionnoform = AdmissionNoForm(prefix='admissionno_form')

		if 4 in required_field:
			print ("phoeno")
			phonenoform = PhoneNoForm(prefix='phoneno_form')


		if 5 in required_field:
			print ("Branch")
			branchform = BranchForm(prefix='branch_form')


		if 6 in required_field:
			print ("teamname")
			teamname = TeamNameForm(prefix='teamname_form')

		if 7 in required_field:
			print ("idea")
			ideasform = IdeasForm(prefix='Ideas_form')

		if 8 in required_field:
			print ("gender")
			genderform = GenderForm(prefix='Gender_form')

		

		return render(request,"registration.html",{
			'usernameform':usernameform,
			'emailForm':emailForm,
			'admissionnoform':admissionnoform,
			'phonenoform':phonenoform,
			'branchform':branchform,
			'teamname':teamname,
			'ideasform':ideasform,
			'genderform':genderform,
			'event_name':event_name
			})

def grouper(n, iterable):
    """
    >>> list(grouper(3, 'ABCDEFG'))
    [['A', 'B', 'C'], ['D', 'E', 'F'], ['G']]
    """
    iterable = iter(iterable)
    return iter(lambda: list(it.islice(iterable, n)), [])


@login_required
def ViewRegistraion(request):
	events =  Event.objects.all()
	if events:
		event_list = []
		for event in events:
			registrations = Registration.objects.filter(event=event.id).count()
			event_dict ={}
			event_dict['event_id'] = event.id
			event_dict['event_name'] = event.Eventname
			event_dict['location'] = event.Location
			event_dict['Description'] = event.Description
			event_dict['registraions_count'] = registrations
			event_list.append(event_dict)

	else:
		return render(request,'view_registration.html')


	return render(request,'view_registration.html',{'event_list':event_list})
	

@login_required
def ExcelData(request,event_id):
	# content-type of response
	event = Event.objects.get(id=event_id)
	response = HttpResponse(content_type='application/ms-excel')

	#decide file name
	response['Content-Disposition'] = 'attachment; filename='+event.Eventname

	#creating workbook
	wb = xlwt.Workbook(encoding='utf-8')

	#adding sheet
	ws = wb.add_sheet("sheet1")

	# Sheet header, first row
	row_num = 0

	font_style = xlwt.XFStyle()
	# headers are bold
	font_style.font.bold = True

	#column header names, you can use your own headers here
	columns = [Constant.FirstName, Constant.LastName, Constant.Emailid , Constant.AdmissionNo,
	Constant.PhoneNo,Constant.Branch,Constant.Year,Constant.Degree,Constant.TeamName,Constant.Gender, Constant.Idea]

	#write column headers in sheetBranch
	for col_num in range(len(columns)):
		ws.write(row_num, col_num, columns[col_num], font_style)

	# Sheetdegree body, remaining rows
	font_style = xlwt.XFStyle()

	#get your data, from database or from a text file...
	registration = Registration.objects.filter(event = event)

	for my_row in registration:

		row_num = row_num + 1
		if my_row.username:
			ws.write(row_num, 0, my_row.username.first_name, font_style)
			ws.write(row_num, 1, my_row.username.last_name, font_style)
		
		if my_row.email:
			ws.write(row_num, 2, my_row.email.emailid, font_style)

		if my_row.admissionno:
			ws.write(row_num, 3, my_row.admissionno.admission_no, font_style)
		if my_row.phoneno:
			ws.write(row_num, 4, my_row.phoneno.phone_number, font_style)
		
		if my_row.branch:
			ws.write(row_num, 5, my_row.branch.branch_name, font_style)
			ws.write(row_num, 7, my_row.branch.degree, font_style)
			ws.write(row_num, 6, my_row.branch.year, font_style)
		if my_row.teamname:
			ws.write(row_num, 8, my_row.teamname.team_name , font_style)

		if my_row.gender:
			ws.write(row_num, 9, my_row.gender.genders , font_style)

		if my_row.idea:
			ws.write(row_num, 10, my_row.idea.ideas , font_style)

	wb.save(response)
	return response