from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Message
from .forms import MessageForm
from django.http import HttpResponseRedirect
# Create your views here.

def home(request):
    submitted = False
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MessageForm
        if 'submitted' in request.GET:
           submitted = True 
    return render(request, 'Resume/home.html', {'form':form, 'submitted':submitted})



