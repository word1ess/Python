from django.shortcuts import render, redirect
from django.http import HttpRequest
# Create your views here.

def index(requset):
    return render(requset, 'devoloper/index.html')

def demand(requset):
    return render(requset, 'devoloper/demand.html')

def geography(requset):
    return render(requset, 'devoloper/geography.html')

def recentVacancies(requset):
    return render(requset, 'devoloper/recent-vacancies.html')

def skills(requset):
    return render(requset, 'devoloper/skills.html')

def signUp(requset):
    return render(requset, 'devoloper/sign-up.html')

def signIn(requset):
    return render(requset, 'devoloper/sign-in.html')



