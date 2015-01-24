from settings import *


DEBUG = True
INTERNAL_IPS = ("127.0.0.1",)
DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}
ROOT_URLCONF = "urls"

ALLOWED_HOSTS = [
    '*.redhat.com',  # Allow domain and subdomains
    '.blozzer.com.', # Also allow FQDN and subdomains
]



DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'mezzanine',
         'USER': 'adminXsnWZBu',
         'PASSWORD': 'jn3L8Dk_Piq6',
         'HOST': os.environ.get('OPENSHIFT_MYSQL_DB_HOST'),
         'PORT': os.environ.get('OPENSHIFT_MYSQL_DB_ PORT'),
     }
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'mezzanine',
    #     'USER': 'root',
    #     'PASSWORD': 'A3ternatenebrae',
    #     'HOST': "localhost",
    #     'PORT': "3306",
    # }
}

SECRET_KEY = 'development-key'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, '../../data/media/')


from mezzanine.utils.conf import set_dynamic_settings
set_dynamic_settings(globals())

