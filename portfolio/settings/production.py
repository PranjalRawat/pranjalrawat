from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = True
ALLOWED_HOSTS = ['pranjalrawat.herokuapp.com']



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'
