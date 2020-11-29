from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    #render allows us to pass back a template for httpresponse
    return render(request, 'generator/home.html')

def password(request):

    #puts list of chars into a list
    characters = list('abcdefghijklmnopqrstuvwxyz')

    #check for Uppercase
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    #check for special chars
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    #check if user wants number:
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    #get length they want (12 is the defualt)
    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html',{'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
