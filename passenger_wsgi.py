import os, sys
sys.path.insert(0, '/var/www/u1860870/data/www/tavolga-journal.ru/tavolga')
sys.path.insert(1, '/var/www/u1860870/data/djangoenv/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'tavolga.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()