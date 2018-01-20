# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your models here.
from django.db import models
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
import app.Constant as Constant
import os
from django.core.exceptions import ValidationError

YEAR = (
	('1', 'First'),
	('2', 'Second'),
	('3', 'Third'),
	('4', 'Fourth'),
	('5', 'Fifth'),
)
BRANCHES = (
	('CO', 'Computer Engineering'),
	('ME', 'Mechanical Engineering'),
	('CE', 'Civil Engineering'),
	('EE', 'Electrical Engineering'),
	('CH', 'Chemical Engineering'),
	('EC', 'Electronics Engineering'),
	('PHY', 'Physics'),
	('CHEM', 'Chemistry'),
	('MATH', 'Mathematics')
)

DEGREES = (
	('BTECH', 'BTech'),
	('MSC', 'MSc'),
)

GENDER_CHOICES = (
	('M', 'Male'),
	('F', 'Female'),
	('O', 'Other'),
)

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




class Event(models.Model):
	id = models.AutoField(primary_key=True)
	Eventname = models.CharField(max_length=30)
	Location = models.CharField(max_length=255)
	Dateime = models.DateTimeField()
	Description = models.TextField(max_length=5000)
	RequiredFields = MultiSelectField(max_length = 50 ,choices = OPTIONS)
	created_date = models.DateTimeField(auto_now_add=True)
	document = models.FileField(upload_to='Media/',blank=True)
    

	def __str__(self):
		return "{}, {}, {}".format(
			self.Eventname, self.Location, self.id)





class UserName(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=255)
#     Event = models.ForeignKey(Event,
#     on_delete=models.CASCADE,
#     verbose_name="Registration details",
#     blank=True,
# )


	def __str__(self):
		return "{}, {}".format(self.first_name,self.last_name)


class Email(models.Model):
	emailid = models.EmailField(max_length=50)
	def __str__(self):
		return "{}".format(self.emailid)



class AdmissionNo(models.Model):
	admission_no = models.CharField(max_length=10)
	def __str__(self):
		return "{}".format(self.admission_no)

 

class PhoneNo(models.Model):
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
	
	def __str__(self):
		return "{}".format(self.phone_number)



class Branch(models.Model):
	branch_name = models.CharField(max_length=4, choices=BRANCHES)
	degree = models.CharField(max_length=5, choices=DEGREES, default='BTECH')
	year = models.CharField(choices=YEAR,max_length=10)

	class Meta:
		ordering = ['degree']

	def __str__(self):
		return "{}, {},{}".format(self.get_degree_display(), self.get_branch_name_display(),self.get_year_display())



class TeamName(models.Model):
	team_name = models.CharField(max_length=50)

	def __str__(self):
		return "{}".format(self.team_name)

class Idea(models.Model):
	ideas = models.TextField()

	def __str__(self):
		return "{}".format(self.ideas)


class Gender(models.Model):
	genders = models.CharField(max_length=10,choices=GENDER_CHOICES)
	def __str__(self):
		return "{}".format(self.genders)



class Registration(models.Model):
	event = models.ForeignKey("Event",on_delete=models.CASCADE)
	username = models.ForeignKey('UserName', related_name='username', blank=True, null=True)
	email = models.ForeignKey('Email', related_name='Email', blank=True, null=True)
	phoneno = models.ForeignKey('PhoneNo', related_name='phoneno', blank=True, null=True)
	admissionno = models.ForeignKey('AdmissionNo',blank=True, null=True)
	branch = models.ForeignKey("Branch",related_name='branch',blank=True,null=True)
	teamname = models.ForeignKey('TeamName', related_name='teamname', blank=True, null=True)
	idea = models.ForeignKey("Idea",related_name='Idea',blank=True,null=True)
	gender = models.ForeignKey("Gender",related_name='gender',blank=True,null=True)
	created_date = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return "{},{},{},{}".format(self.event,self.username,self.email,self.admissionno)



	
	
	
	


