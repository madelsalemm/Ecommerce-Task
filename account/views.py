#from multiprocessing import context
from django.shortcuts import render , redirect 
#from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate 
# Create your views here.

def signup(request):
    if request.method =="POST" :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            
            user = authenticate(username = username , password = password)
            login(request , user)
            return redirect('/')
            
    else:
        form = UserCreationForm()
    
    context = {'form' : form}         #{form of templete: above form}
    return render(request , 'registration/signup.html' , context)