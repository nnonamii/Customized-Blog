"""
Django settings for blog_project project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os, json
from django.core.exceptions import ImproperlyConfigured


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
secret_file = os.path.join(BASE_DIR, "secrets.json")

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# TinyMCE 텍스트 에디터 설정
# STATIC_URL = "/static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

# TINYMCE_JS_URL = os.path.join(STATIC_URL, "tinymce/tinymce.min.js")
# TINYMCE_DEFAULT_CONFIG = {
#     "cleanup_on_startup": True,
#     "custom_undo_redo_levels": 20,
#     "selector": "textarea",
#     "theme": "silver",
#     "plugins": """
#             textcolor save link image media preview codesample contextmenu
#             table code lists fullscreen  insertdatetime  nonbreaking
#             contextmenu directionality searchreplace wordcount visualblocks
#             visualchars code fullscreen autolink lists  charmap print  hr
#             anchor pagebreak
#             """,
#     "toolbar1": """
#             fullscreen preview bold italic underline | fontselect,
#             fontsizeselect  | forecolor backcolor | alignleft alignright |
#             aligncenter alignjustify | indent outdent | bullist numlist table |
#             | link image media | codesample |
#             """,
#     "toolbar2": """
#             visualblocks visualchars |
#             charmap hr pagebreak nonbreaking anchor |  code |
#             """,
#     "contextmenu": "formats | link image",
#     "menubar": True,
#     "statusbar": True,
#     "theme_advanced_resizing": True,
#     "images_upload_url": "upload_image",
#     "width": "100%",
#     "height": 600,
# }


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "blog_app",
    "rest_framework",
    "tinymce",
    "social_django",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
]

# 구글 소셜 로그인 설정
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = get_secret("SOCIAL_AUTH_GOOGLE_OAUTH2_KEY")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = get_secret("SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET")
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = "http://127.0.0.1:8000/board"

AUTHENTICATION_BACKENDS = [
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
    "social_core.backends.naver.NaverOAuth2",
]

SOCIAL_AUTH_AUTHENTICATION_BACKENDS = [
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.naver.NaverOAuth2",
]

# 네이버 소셜 로그인 설정
SOCIAL_AUTH_NAVER_KEY = get_secret("SOCIAL_AUTH_NAVER_KEY")
SOCIAL_AUTH_NAVER_SECRET = get_secret("SOCIAL_AUTH_NAVER_SECRET")

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "blog_project.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "blog_project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
with open("password.txt") as f:
    password_postresql = f.read()

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "blog_project",
        "USER": "postgres",
        "PASSWORD": password_postresql,
        "HOST": "blog-project-db.cminy4xslvpf.ap-northeast-2.rds.amazonaws.com",
        "PORT": "5432",
    }
}

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

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
