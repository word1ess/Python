from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('index/', index, name="index"),
    path('demand/', demand, name="demand"),
    path('geography/', geography, name="geography"),
    path('recent-vacancies/', recentVacancies, name="recent-vacancies"),
    path('skills/', skills, name="skills"),
    path('sign-up/', signUp, name="sign-up"),
    path('sign-in/', signIn, name="sign-in"),
]