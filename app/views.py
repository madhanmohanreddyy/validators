from django.http.response import HttpResponse
from app.forms import StudentForm
from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def madhu(request):
    form=StudentForm()
    if request.method=='POST':
        form_data=StudentForm(request.POST)
        if form_data.is_valid():

          return HttpResponse('data submitted successfully')
        
    return render(request,'validators.html',context={'form':form})


def madhan(request,data):
  return HttpResponse('hello {}'.format(data))