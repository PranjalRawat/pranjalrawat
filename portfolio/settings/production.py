from pathlib import Path
from portfolio.settings.base import INSTALLED_APPS, MIDDLEWARE

BASE_DIR = Path(__file__).resolve().parent.parent

INSTALLED_APPS+= [
    'whitenoise.runserver_nostatic',
]
MIDDLEWARE+=[
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

DEBUG = False
ALLOWED_HOSTS = ['pranjalrawat.herokuapp.com']



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'
