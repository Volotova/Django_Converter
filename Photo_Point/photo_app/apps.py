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
