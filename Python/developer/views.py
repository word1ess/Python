from django.shortcuts import render, redirect
from django.http import HttpRequest

from .models import Post
from hh_ru.python_vacancies import get_python_vacancies


def html_context(name):
    content = \
        {'content': Post.objects.filter(title=name).first(),
         'title': name}
    return content


def index(requset):
    context = html_context('Главная')
    return render(requset, 'developer/index.html', context)


def demand(requset):
    context = html_context('Востребованность')
    return render(requset, 'developer/index.html', context)


def geography(requset):
    context = html_context('География')
    return render(requset, 'developer/index.html', context)


def recentVacancies(requset):
    vacancies = get_python_vacancies()
    context = {
        'vacancies': vacancies
    }
    return render(requset, 'developer/recent-vacancies.html', context)


def skills(requset):
    context = html_context('Навыки')
    return render(requset, 'developer/index.html', context)
