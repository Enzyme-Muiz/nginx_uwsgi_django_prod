"""
WSGI config for django_docker_nginx project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
print("5")
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_docker_nginx.settings.prod'

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_docker_nginx.settings.dev')
print("5")
application = get_wsgi_application()
