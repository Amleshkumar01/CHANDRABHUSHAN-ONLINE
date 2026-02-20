"""
ASGI config for chandrabhushan_online project.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chandrabhushan_online.settings')

application = get_asgi_application()
