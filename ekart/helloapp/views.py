from django.shortcuts import render
from django.http import HttpResponse

def homepage(request): #her we can use pass keyword to disable this function instead #
    return render(request,'home.html')

def welcome(request):
    #return render(request,'welcome.html')
    name=request.POST['uname'] #uname from html name
    password=request.POST['psw']
    sub=name+' '+password;
    return render(request,'welcome.html',{'final':sub}) #where final:sub is the key and values

def password(request):

    return render(request,'password.html')