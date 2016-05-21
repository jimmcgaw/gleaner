"""
WSGI config for gleaner project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir('~/.virtualenvs/gleaner/local/lib/python2.7/site-packages')
parent_dir = os.path.abspath(os.path.join(yourpath, os.pardir))
sys.path.append(parent_dir)

# Activate your virtual env
activate_env=os.path.expanduser("~/.virtualenvs/gleaner/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gleaner.settings")

application = get_wsgi_application()
