import os
from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['localhost', 'danidee.pythonanywhere.com']

# email config
DEFAULT_FROM_EMAIL = 'osaetindaniel@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'osaetindaniel@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAILPASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
