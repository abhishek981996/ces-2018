from django import forms
from app.models import OPTIONS
from django.utils.translation import ugettext_lazy as _

from cessite.settings import TIME_INPUT_FORMATS, DATE_INPUT_FORMATS

from app.models import Event,UserName,Email,PhoneNo,AdmissionNo,Branch,TeamName,Gender,Idea



class EventForm(forms.ModelForm):

    # Description =forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),required=True)
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['Eventname'].required = True
        self.fields['Location'].required = True
        self.fields['document'].required = False

            
    class Meta:
        model = Event
        exclude = ['id','Dateime','RequiredFields']
        labels = {
            'Eventname': _('Name of the Event'),
            'Location': _('Venue'),
            'Description':_('Description about the event'),
            'document':_('Rules only in .pdf format')
        }
        widgets = {
            'Description': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }

class EventFormExtra(forms.Form):
    Eventdate = forms.DateField(input_formats=DATE_INPUT_FORMATS, required=True)
    EventTime = forms.TimeField(input_formats=TIME_INPUT_FORMATS,required=True)
    RequiredField = forms.MultipleChoiceField(choices = OPTIONS)
    def __init__(self, *args, **kwargs):
        super(EventFormExtra, self).__init__(*args, **kwargs)
        self.fields['RequiredField'].required = True
    class Meta:
            labels = {
            'RequiredField': _('Fields to be added'),
            'Eventdate':_('Date of Event'),
            'EventTime':_('Time of Event'),
            }
         
class UserNameForm(forms.ModelForm):
    """docstring for UserNameForm"""
    def __init__(self, *args, **kwargs):
        super(UserNameForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = UserName
        fields = ['first_name','last_name']
        labels = {
        'first_name':_('First Name'),
        'last_name':_('Last Name')
        }


class EmailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.fields['emailid'].required = True

    class Meta:
        """docstring for Meta"""
        model = Email
        fields = ['emailid']
        labels = {
            'emailid':_("Email id"),
        }
            
class PhoneNoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PhoneNoForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = True

    class Meta:
        model = PhoneNo
        fields = ['phone_number']
        labels = {
            'phone_number':_('Phone number')
        }


class AdmissionNoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdmissionNoForm, self).__init__(*args, **kwargs)
        self.fields['admission_no'].required = True

    class Meta:
        model = AdmissionNo
        fields = ['admission_no']
        
        labels = {
            'admission_no':_('Admission No')
        }

class BranchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BranchForm, self).__init__(*args, **kwargs)
        self.fields['branch_name'].required = True
        self.fields['degree'].required = True
        self.fields['year'].required = True

    class Meta:
        model = Branch
        fields =['branch_name','degree','year']
        labels = {
            'branch_name':_('Branch Name'),
            'degree':_('Degree'),
            'year':_('Year')
        }

class TeamNameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeamNameForm, self).__init__(*args, **kwargs)
        self.fields['team_name'].required = True

    class Meta:
        model = TeamName
        fields = ['team_name']
        labels = {
        'team_name':_('Your Team Name')
        }


class GenderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GenderForm, self).__init__(*args, **kwargs)
        self.fields['genders'].required = True

    class Meta:
        model = Gender
        fields = ['genders']
        lables = {
        'genders',_("Gender")
        }

class IdeasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IdeasForm, self).__init__(*args, **kwargs)
        self.fields['ideas'].required = True

    class Meta:
        model = Idea
        fields = ['ideas']
        labels = {
        'ideas':_("Your Ideas")
        }
        widgets = {
            'ideas': forms.Textarea(attrs={'class': 'materialize-textarea'}),
        }