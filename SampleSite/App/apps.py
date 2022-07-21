from multiprocessing.context import ForkServerContext
from django.apps import AppConfig


class aplication(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App'