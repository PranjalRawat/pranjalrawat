from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com']



STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'
