from stat_collector.settings.common import *
import os

DEBUG = False

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

ALLOWED_HOSTS = ['localhost','127.0.0.1']

# DATABASES = {
#     'default':{
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd9k5f7ogqt4f1h',
#         'HOST': 'ec2-18-210-191-5.compute-1.amazonaws.com',
#         'PORT': 5432,
#         'USER':'qyezzutaarpnjz',
#         'PASSWORD':'dbdb32bb0107296f77f87835f301531700b5994655913831401515ffa81b2335',
#     }
# }


# postgres://qyezzutaarpnjz:dbdb32bb0107296f77f87835f301531700b5994655913831401515ffa81b2335@ec2-18-210-191-5.compute-1.amazonaws.com:5432/d9k5f7ogqt4f1h