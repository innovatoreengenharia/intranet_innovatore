"""
WSGI config for intranet_innovatore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "intranet_innovatore.settings")

application = get_wsgi_application()
#application.add_files("/path/to/more/static/files", prefix="more-files/")



