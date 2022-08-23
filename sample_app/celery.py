from __future__ import absolute_import, unicode_literals
import os
# from django.conf import settings


from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample_app.settings')

app = Celery(   'sample_app',
                broker='redis://localhost:6379/0',
                backend='redis://localhost:6379/0'
                ) # config is the name of the app having setting files

# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()