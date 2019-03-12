"""
WSGI config for I_Volenteer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'I_Volenteer.settings')

application = get_wsgi_application()

# from django.contrib.auth.models import AbstractUser

# class Oraganisation(AbstractUser):
#     oraganisation_name = models.CharField(max_length=16,default='NITK Rescue Team',)
