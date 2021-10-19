from django import forms
from django.forms import ModelForm, widgets
from .models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('Name', 'Email', 'Subject', 'Message')


# To remove the labels 

        labels = {
            'Name': '',
            'Email': '',
            'Subject': '',
            'Message': '',
        }

        widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'Email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
            'Subject' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject'}),
            'Message' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Message'}),
        }