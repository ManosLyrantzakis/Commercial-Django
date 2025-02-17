from pathlib import Path
import os
import environ
import dj_database_url

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()  # Load .env file in local development

# Define project base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Environment settings
ENVIRONMENT = env("ENVIRONMENT", default="production")

# Secret Key (Never expose in production)
SECRET_KEY = env("SECRET_KEY", default="your-secret-key")

# Debug mode (should be False in production)
DEBUG = env.bool("DEBUG", default=False)

# Allowed hosts
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[
    "commercial-django-production.up.railway.app",
    "localhost",
    "127.0.0.1",
])

CSRF_TRUSTED_ORIGINS = ["https://commercial-django-production.up.railway.app"]

# Installed apps
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

# Debugging: Print the DATABASE_URL being used
DATABASE_URL = env("DATABASE_URL", default="")
print(f"📌 DATABASE_URL from environ: {DATABASE_URL if DATABASE_URL else 'Not Found'}")

# ---------------------------------
# DATABASE CONFIGURATION
# ---------------------------------
if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.config(default=DATABASE_URL, conn_max_age=600)
    }
else:
    print("⚠️ DATABASE_URL is missing! Using fallback settings.")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("DB_NAME", default="railway"),
            "USER": env("DB_USER", default="postgres"),
            "PASSWORD": env("DB_PASSWORD", default="NGrPDMsxhNBRRNqQbZbGTNHbCxodbkns"),
            "HOST": env("DB_HOST", default="autorack.proxy.rlwy.net"),
            "PORT": env("DB_PORT", default="47504"),
        }
    }

# ---------------------------------
# PASSWORD VALIDATION
# ---------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ---------------------------------
# STATIC & MEDIA FILES
# ---------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = BASE_DIR / "staticfiles"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ---------------------------------
# PAYPAL CONFIGURATION
# ---------------------------------
PAYPAL_TEST = env.bool("PAYPAL_TEST", default=True)
PAYPAL_RECEIVER_EMAIL = env("PAYPAL_RECEIVER_EMAIL", default="business@test.com")

# Default primary key type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
