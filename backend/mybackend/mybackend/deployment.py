import os
from .settings import*
from .settings import BASE_DIR


ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTSNAME']]
CSRF_TRUSTED_ORIGINS = ["https://"+os.environ['WEBSITE_HOSTNAME']]

DEBUG = False
SECRET_KEY = os.environ['MY_SECRET_KEY']

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Add this line
    'django.middleware.common.CommonMiddleware',  # Add this line
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#CORS_ALLOWED_ORIGINS = ["https://"+os.environ['WEBSITE_HOSTNAME'],]

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles":{
        "BACKEND":"whitenoise.storage.CompressedManifestStaticFilesStorage",
    }
}

CONNECTION = os.environ['CONNECTION']
CONNECTION_STR = {pair.split('=')[0]:pair.split('=')[1] for pair in CONNECTION.split(' ')}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': CONNECTION_STR['Database'],
        'HOST': CONNECTION_STR['Data Source'],
        'USER': CONNECTION_STR['User Id'],
        'PASSWORD': CONNECTION_STR['Password'],
    }
}

STACIC_ROOT = BASE_DIR / 'staticfiles'