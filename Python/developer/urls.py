from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('demand/', demand, name="demand"),
    path('geography/', geography, name="geography"),
    path('recent-vacancies/', recentVacancies, name="recent-vacancies"),
    path('skills/', skills, name="skills"),
]
