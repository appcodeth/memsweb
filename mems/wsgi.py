import os
import sys

sys.path.append("/var/www/website/envs/mems")

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mems.settings')
application = get_wsgi_application()
