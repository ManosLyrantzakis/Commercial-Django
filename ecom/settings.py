from pathlib import Path
import os
from environ import Env
import dj_database_url

env = Env()
Env.read_env()
ENVIRONMENT = env('ENVIRONMENT', default='production')

#from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load our environmental variables
# load_dotenv()





# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-x4m$gfeda-r+)u05g*bzm%8#_vz&8-wl^3epo45gqi#_eqwvtq'


#ENCRYPT_KEY = env('ENCRYPT_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

    
ALLOWED_HOSTS = ['commercial-django-production.up.railway.app','localhost','127.0.0.1',]

CSRF_TRUSTED_ORIGINS = ["https://commercial-django-production.up.railway.app"]

    



#ALLOWED_HOSTS = ['https://djangotest.com', 'djangotest.com', 'django-ecommerce-production-81b6.up.railway.app', 'https://django-ecommerce-production-81b6.up.railway.app']
#CSRF_TRUSTED_ORIGINS = ['https://djangotest.com', 'https://django-ecommerce-production-81b6.up.railway.app']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'cart',
    'payment',
    'whitenoise.runserver_nostatic',
    'paypal.standard.ipn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'ecom.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',

            ],
        },
    },
]

WSGI_APPLICATION = 'ecom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': os.getenv('django.db.backends.postgresql'),
        'NAME': os.getenv('railway'),
        'USER': os.getenv('postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD_W'),
        'HOST': os.getenv('postgresql://postgres:xbiWlFZsFntrfmuIigqLhDoiAgfputbQ@junction.proxy.rlwy.net:33767/railway'),
        'PORT': os.getenv('5432'),
    }
}

POSTGRES_LOCALLY = True
if ENVIRONMENT =='production' or POSTGRES_LOCALLY == True:
    DATABASES['default'] = dj_database_url.parse(env('DATABASE_URL'))

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = ['static/']

# White noise static stuff
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Add paypal settings
# Set sandbox to true
PAYPAL_TEST = True

PAYPAL_RECEIVER_EMAIL = 'business@codemytest.com' # Business Sandbox account