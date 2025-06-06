import os
import dj_database_url
from dotenv import load_dotenv
load_dotenv()
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$k0m&rnyf9wua_=@37aaouf3m9w5s)zu)*joz89glas47!_!&i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'url_server', 'de1f-200-87-152-233.ngrok-free.app', '192.168.0.13']
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')


# Configuración unificada de archivos media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Rutas específicas dentro de media
BACKUP_ROOT = os.path.join(MEDIA_ROOT, 'backups')
STAFF_PHOTOS_ROOT = os.path.join(MEDIA_ROOT, 'staff_photos')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',

    'rest_framework',  # Django REST Framework
    'corsheaders',     # CORS Headers
    'users',           # Nuestra app de usuarios

    'auditlog', #para la bitácora
    'audit',
    'services',
    'locations',
    'django_extensions',
    'events',
    'companies',
    'subscriptions',
    'backup',
    'packages',
    'sales',
    'schedules',
    'staff',        # Nueva app
    'tasks',        # Nueva app
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Añadir al inicio
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'subscriptions.middleware.SubscriptionRequiredMiddleware',
]

ROOT_URLCONF = 'planit_one_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'audit/templates'),
        ],
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

WSGI_APPLICATION = 'planit_one_backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

#Servidor Railway
DATABASES ={
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

# DATABASES = {
#    'default': {
#       'ENGINE': 'django.db.backends.postgresql',
#       'NAME': os.getenv('DB_NAME'),
#       'USER': os.getenv('DB_USER'),
#       'PASSWORD': os.getenv('DB_PASSWORD'),
#       'HOST': os.getenv('DB_HOST'),
#       'PORT': os.getenv('DB_PORT'),
#   }
# }


# Configuración de CORS para permitir solicitudes desde el frontend
CORS_ALLOW_ALL_ORIGINS = True  # En producción, limitar a dominios específicos

# Configuración de REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',  # JWT para autenticación
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.User'

# SimpleJWT Configuration
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,
}

# Al final del archivo para la bitácora
AUDITLOG_INCLUDE_ADMIN_MODEL_ACTIONS = True

STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

STATICFILES_STORAGE="whitenoise.storage.CompressedManifestStaticFilesStorage"

# CSRF_TRUSTED_ORIGINS=['http://*','https://softwareeventosbackend-production.up.railway.app']
CSRF_TRUSTED_ORIGINS = os.environ.get(
    'CSRF_TRUSTED_ORIGINS',
    'http://localhost:3000,http://127.0.0.1:8000'
).split(',')

# Configuración de Stripe
STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY', '')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY', '')
STRIPE_WEBHOOK_SECRET = os.environ.get('STRIPE_WEBHOOK_SECRET', '')
