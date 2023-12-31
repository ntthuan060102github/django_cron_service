import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app_core.settings')

app = Celery('app_core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    pass