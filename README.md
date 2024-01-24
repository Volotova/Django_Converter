Задание:
-------

Cоздать "голый" джанго проект, который по переходу на страницу /get-current-usd/ бужет отображать в json формате актуальный курс доллара к рублю (запрос по апи, найти самостоятельно) и показывать 10 последних запросов 


### Установка и запуск
-------
Установливаем Django, создаем новый проект, заходим в папку, создаем приложение

```bash
pip install django
django-admin startproject Photo_Point
cd Photo_Point
python manage.py starapp photo_app
pip install bs4
```

Добавляем приложение в settings.py

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'photo_app',
]
```

Создаем view.py. В коде все расписано для чего что создано.

Регистрируем urls.py в приложении и в корневой папке.

1) Корневая папка
```bash
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('photo_app.urls')),
]
```

2) Приложение
```bash
from django.urls import path

from .views import show_json

urlpatterns = [
    path('get-current-usd/', show_json, name='get_current_usd'),
]
```


Добавим функционан в apps.py, который позволяет единожды при запуске программы отработать некоторые функции
```bash
from django.apps import AppConfig

from .views import *


class PhotoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'photo_app'
    verbose_name = 'Тестовое задание'

    def ready(self):
        save_xml()
        parsing_xml()
        json_file()
```


Запускаем приложение и переходим по пути get-current-usd/ 
При первом запуске появится 2 файла: file.xml и output.json в папке проекта.

```bash
python manage.py runserver
```

