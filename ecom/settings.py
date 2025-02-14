from pathlib import Path
import os
import environ
import dj_database_url

# Διαβάζουμε τις μεταβλητές περιβάλλοντος από το .env
env = environ.Env()
environ.Env.read_env()

# Ορίζουμε τη διαδρομή του project
BASE_DIR = Path(__file__).resolve().parent.parent

# Λειτουργικό περιβάλλον (development ή production)
ENVIRONMENT = env("ENVIRONMENT", default="production")

# Secret Key (μην την αφήνεις exposed σε production!)
SECRET_KEY = env("SECRET_KEY", default="your-secret-key")

# Debug mode (πρέπει να είναι False σε production)
DEBUG = env.bool("DEBUG", default=False)

# Επιτρεπτοί hosts
ALLOWED_HOSTS = [
    "commercial-django-production.up.railway.app",
    "localhost",
    "127.0.0.1",
]

CSRF_TRUSTED_ORIGINS = ["https://commercial-django-production.up.railway.app"]

# Εγκατεστημένες εφαρμογές
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "store",
    "cart",
    "payment",
    "whitenoise.runserver_nostatic",
    "paypal.standard.ipn",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "ecom.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "cart.context_processors.cart",
            ],
        },
    },
]

WSGI_APPLICATION = "ecom.wsgi.application"

# ---------------------------------
# DATABASE CONFIGURATION
# ---------------------------------
DATABASE_URL = env("DATABASE_URL", default="")

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": ("railway"),
            "USER": ("postgres"),
            "PASSWORD": ("NGrPDMsxhNBRRNqQbZbGTNHbCxodbkns"),
            "HOST":("autorack.proxy.rlwy.net"),
            "PORT":("47504"),
        }
    }

# ---------------------------------
# PASSWORD VALIDATION
# ---------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ---------------------------------
# STATIC & MEDIA FILES
# ---------------------------------
STATIC_URL = "static/"
STATICFILES_DIRS = ["static/"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ---------------------------------
# PAYPAL CONFIGURATION
# ---------------------------------
PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL = env("PAYPAL_RECEIVER_EMAIL", default="business@codemytest.com")

# Default primary key type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

