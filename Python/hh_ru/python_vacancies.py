from bs4 import BeautifulSoup
import requests

from datetime import datetime


def get_python_vacancies():
    vacancies = requests.get("https://api.hh.ru/vacancies?text=python&order_by=publication_time&search_field=name")
    vacancies = vacancies.json()['items']

    result = []
    for vacancy in vacancies[:10]:
        vacancy = requests.get("https://api.hh.ru/vacancies/" + vacancy['id']).json()
        description = BeautifulSoup(vacancy['description'], features="html.parser").get_text()
        date = datetime.strptime(vacancy['published_at'], "%Y-%m-%dT%H:%M:%S+0300")
        date = date.strftime("%d.%m.%Y, %H:%M")
        salary = vacancy['salary']

        if salary is None:
            salary = ""
        else:
            if salary['to'] is not None:
                salary = salary['to']
            else:
                salary = salary['from']
            salary = str(salary) + " " + vacancy['salary']['currency']

        skills = []
        for skill in vacancy['key_skills']:
            skills.append(skill['name'])
        skills = ', '.join(skills)

        fields = {
            "name": vacancy['name'],
            "description": description,
            "salary": salary,
            "skills": skills,
            "employer": vacancy['employer']['name'],
            "city": vacancy['area']['name'],
            "date": date,
            "url": vacancy['alternate_url']
        }
        result.append(fields)
    return result
