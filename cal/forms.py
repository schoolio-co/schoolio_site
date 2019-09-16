from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from django.conf import settings
from django.forms import ModelChoiceField
from django.forms import formset_factory
from django.db import transaction
from datetime import datetime
from schoolio.models import Event

class EventForm(forms.ModelForm):
    start_time = forms.DateTimeField(initial=datetime.now().strftime("%Y-%m-%d %H:%M"), required=False)
    end_time = forms.DateTimeField(initial=datetime.now().strftime("%Y-%m-%d %H:%M"), required=False)
    
    class Meta:
        model = Event
        fields = '__all__'