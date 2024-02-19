# manipulação de estáticos debug false
import mimetypes
from pathlib import Path, os

mimetypes.add_type("text/css", ".css", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-tkahy*n1l1_6&kt94yfcb0tl6b6r)x(x-uag5rb_3=1mwj5$u("

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "localhost", "srv479192.hstgr.cloud"]

CSRF_TRUSTED_ORIGINS = ['http://localhost:1337','https://*.127.0.0.1', 'http://srv479192.hstgr.cloud']

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "login"

EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = BASE_DIR / "emails"

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER =
# EMAIL_HOST_PASSWORD =

# Application definition

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "dashboard",
    "usuario",
    "documentos",
    "tarefas",
    "cursos",
    "cartao_visitas",
    "aniversariantes",
    "social",
    "calendario",
    "informativos",
    "mapa",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "intranet_innovatore.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

""" DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
} """
# AMBIENTE DE PRODUÇÃO
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "intranet_innovatore",
        "USER": "flavio",
        "PASSWORD": "314628",
        "HOST": "database",
        "PORT": "6000",
    }
}


# AMBIENTE DE DESENVOLVIMENTO
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "intranet_innovatore",
#         "USER": "flavio",
#         "PASSWORD": "314628",
#         "HOST": "localhost",
#         "PORT": "5432",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "intranet_innovatore/static")
# STATIC_ROOT = BASE_DIR / "static"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# AMBIENTE DE PRODUÇÃO
MEDIA_ROOT = os.path.join(BASE_DIR, "intranet_innovatore/media")

# AMBIENTE DE DESENVOLVIMENTO
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")


MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Redirect to home URL after login (Default redirects to /accounts/profile/)

# Tamanho máximo slavo em RAM em bytes
# codigo =   FILE_UPLOAD_MAX_MEMORY_SIZE = 100000000

# Logof limite de tempo:
SESSION_COOKIE_AGE = 1200

# Reinicia a contagem com request:
SESSION_SAVE_EVERY_REQUEST = True


WSGI_APPLICATION = "intranet_innovatore.wsgi.application"


# CHANNELS
ASGI_APPLICATION = "intranet_innovatore.asgi.application"

# AMBIENTE DE PRODUÇÃO
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("redis", 6380)],
        },
    },
}

# AMBIENTE DE DESENVOLVIMENTO
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "channels_redis.core.RedisChannelLayer",
#         "CONFIG": {
#             "hosts": [("localhost", 6379)],
#         },
#     },
# }


SESSION_SAVE_EVERY_REQUEST = True


# Tamanho de upload permitido

DATA_UPLOAD_MAX_MEMORY_SIZE = 10000000
