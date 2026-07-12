import os
from pathlib import Path
from dotenv import load_dotenv

# BASE_DIR loyihaning ildiz papkasini ko'rsatadi
BASE_DIR = Path(__file__).resolve().parent.parent

# .env faylini aniq manzili bilan yuklaymiz
env_path = BASE_DIR / '.env'
load_dotenv(dotenv_path=env_path)

# Agar .env dan o'qiy olmasa, vaqtincha local default kalitni ishlatadigan qilamiz
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-local-development-key-12345')

DEBUG = False

ALLOWED_HOSTS = ['salmoncs.com', 'www.salmoncs.com', '167.172.251.184', 'localhost', '127.0.0.1']

ROOT_URLCONF = 'config.urls'


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'portfolio_db'),
        'USER': os.getenv('DB_USER', 'salmon_admin'),
        'PASSWORD': os.getenv('DB_PASSWORD'),  # Bu yerda os.getenv bo'lishi shart!
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # E410 uchun
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # E408 uchun
    'django.contrib.messages.middleware.MessageMiddleware', # E409 uchun
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]



WSGI_APPLICATION = 'config.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'], # Agar loyiha boshida templates/ papkasi bo'lsa
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


STATIC_URL = 'static/'

# DigitalOcean deploy jarayonida static fayllarni to'plash uchun kerak (Production uchun)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Loyihamiz ichidagi static fayllar joylashgan asosiy papka
STATICFILES_DIRS = [
    BASE_DIR / 'core' / 'static',
]



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
