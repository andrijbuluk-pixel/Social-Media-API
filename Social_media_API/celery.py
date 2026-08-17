import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Social_media_API.settings')

app = Celery('Social_media_API')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()