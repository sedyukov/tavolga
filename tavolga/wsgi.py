"""
WSGI config for tavolga project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tavolga.settings')
#
# application = get_wsgi_application()

import os
import sys

try:
    sys.path.remove('ali/opt/miniconda3/bin/python3/dist-packages')
except:
    pass
sys.path.append('/home/c/cm99441/django/public_html/tavolga')
sys.path.append('/home/c/cm99441/django/venv/lib/python3.9/site-packages/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tavolga.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
