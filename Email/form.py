from django import forms
from django.utils.translation import ugettext_lazy as _

from app.models import Event




def choicefields():
    events = Event.objects.all()
    event_dict = {}
    for event in events:
        event_dict[event.id] = event.Eventname

    event_list = []
    for key, value in event_dict.iteritems():

        temp = [key,value]
        event_list.append(temp)

    return event_list


event_list = choicefields()
class SendEmailForm(forms.Form):
    subject = forms.CharField(max_length=100,required=True)
    body =forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}),required=True)
    Select_Event = forms.ChoiceField(
        required=True,choices = event_list)
    class meta:

 
        labels = {
        	'subject':_("Subject for mail"),
        	'body':_("Body"),
        	"Select_Event":_("Select Event")
        }

 


