from django.urls import path

from .views import show_json

urlpatterns = [
    path('get-current-usd/', show_json, name='get_current_usd'),
]