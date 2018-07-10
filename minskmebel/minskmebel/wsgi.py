"""
WSGI config for minskmebel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import sys, os
cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/minskmebel') 

os.environ['DJANGO_SETTINGS_MODULE'] = "minskmebel.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
