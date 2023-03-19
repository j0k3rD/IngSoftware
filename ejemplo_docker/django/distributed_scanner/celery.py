import os
from celery import Celery
from django.conf import settings

# Establecer la variable de entorno DJANGO_SETTINGS_MODULE para que Celery pueda encontrar el archivo settings.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'distributed_scanner.settings')

# Instanciar la aplicación de Celery
app = Celery('distributed_scanner')
# Configurar Celery utilizando las opciones definidas en settings.py
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    BROKER_URL='redis://redis:6379/0',
    CELERY_RESULT_BACKEND='redis://redis:6379/0',
)