"""
WSGI config for chandrabhushan_online project.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chandrabhushan_online.settings')

application = get_wsgi_application()
