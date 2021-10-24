from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm
from django.contrib import messages

#from django.contrib.auth.forms import UserCreationForm #first to import for creating a new form


# Create your views here.

def home(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ('Your Message Has Been Sent Successfully!'))
        return redirect('/')

    else:
        context = {}
        return render(request, 'Resume/home.html', context)
