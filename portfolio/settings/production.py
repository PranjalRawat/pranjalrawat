from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


DEBUG = False
ALLOWED_HOSTS = ['pranjalrawat.herokuapp.com']



STATIC_ROOT = BASE_DIR / 'staticfiles'

