"""
WSGI config for intranet_innovatore project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from django.conf import settings

from whitenoise import WhiteNoise

application = get_wsgi_application()
application = WhiteNoise(application, root= settings.STATIC_ROOT)
#application.add_files("/path/to/more/static/files", prefix="more-files/")


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "intranet_innovatore.settings")

