import datetime
import requests
import json

from datetime import date
from bs4 import BeautifulSoup
from django.http import JsonResponse


def api_url():
    current_time = str(date.today())  # Получение текущей даты в формате %Y-%m-%d
    clear_current_time = datetime.datetime.strptime(current_time, "%Y-%m-%d").strftime('%d/%m/%Y')  # Преобразование в формат %d/%m/%Y для дальнейшего использования в шаблоне
    api_url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={clear_current_time}'  # Получение страницы с дерером XML
    return api_url

def save_xml():  # Сохраним стринцу с дерером XML в файл
    response = requests.get(api_url())

    with open('file.xml', 'wb') as file:
        file.write(response.content)

    return file

def parsing_xml():
    fd = open('file.xml', 'r')  # Передадим файл в переменную
    xml_file = fd.read()

    soup = BeautifulSoup(xml_file, 'xml')  # Распарсим XML файл записанный в строку
    value = soup.find('Valute', {'ID': 'R01235'}).find('Value').text  # Через ID найдем нужную валюту

    return value

def json_file():  # Создадим json файл и передадим в него ранее полученный эквивалент валюты
    dictionary = {}
    dictionary[f'The current exchange rate of the dollar to the ruble {datetime.datetime.now()}'] = parsing_xml()

    data = dictionary

    json_file_path = 'output.json'

    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=2)

def new_data():  # Перезаписываем файл с обновленными данными
    with open('output.json', 'r') as file:
        data = json.load(file)

    current_datetime = datetime.datetime.now().replace(microsecond=0)
    new_data = {f'The current exchange rate of the dollar to the ruble {current_datetime}': parsing_xml()}
    data.update(new_data)

    if len(data) > 10:
        first_key = list(data.keys())[0]
        del data[first_key]

    with open('output.json', 'w') as file:
        json.dump(data, file)

def show_json(request):
    new_data()

    json_file_path = 'output.json'

    with open(json_file_path, 'r') as file:
        json_data = json.load(file)

    return JsonResponse(json_data)

