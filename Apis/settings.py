"""
Django settings for Apis project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from datetime import timedelta
from rest_framework.settings import api_settings
import dj_database_url
from corsheaders.defaults import default_headers


# *******************************
import environ
env=environ.Env()
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True if env("DEBUG")=="True" else False

ALLOWED_HOSTS = ['192.168.43.73','127.0.0.1']

if not DEBUG:
    RENDER_EXTERNAL_HOSTNAME = env('RENDER_EXTERNAL_HOSTNAME')
    if RENDER_EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'cloudinary',

    # package
    'rest_framework',
    "corsheaders",
    # 'rest_framework.authtoken',
    'knox',
   'drf_yasg',
      'tinymce',
#    'rest_framework_simplejwt',
    

    #local App
    'account',
    'posts',
    'comments',
    'userprofile',
    'contacts',
    'likes'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('knox.auth.TokenAuthentication',
                                    #    'rest_framework_simplejwt.authentication.JWTAuthentication',
                                    ),
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '4/minute',
    #     'user': '4/minute',
    # },
    
}
# CACHES = {
#     'default': {
#         # 'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         # "BACKEND":'django.core.cache.backends.filebased.FileBasedCache',
#         #  "BACKEND":'django.core.cache.backends.dummy.DummyCache',
#         # "BACKEND":'django.core.cache.backends.locmem.LocMemCache',
#          "BACKEND":'django.core.cache.backends.db.DatabaseCache',
#         # 'LOCATION':'127.0.0.1:1109'
#         # "LOCATION":'C://'
#         "LOCATION":'my_cache_table'
        
#     }
# }
# 'django.contrib.auth.backends.ModelBackend'
AUTHENTICATION_BACKENDS = [
    # 'account.authentication.EmailBackend'
    'django.contrib.auth.backends.ModelBackend'
]

MIDDLEWARE = [
    # 'csp.middleware.CSPMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
     "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'Apis.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'Apis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
            'default': dj_database_url.parse(env('DATABASE_URL'))
        }




# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL='account.CustomUser'



if DEBUG:
    MEDIA_URL="/media/"
    MEDIA_ROOT=os.path.join(BASE_DIR,'media/')
else:
    MEDIA_URL="/media/"
    DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://192.168.43.73:8000"
]
CORS_ALLOW_ALL_ORIGINS=False

CORS_ALLOW_HEADERS=(
    *default_headers,
)
CSRF_TRUSTED_ORIGINS=[
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "http://192.168.43.73:8000"

]

if not DEBUG:
    RENDER_EXTERNAL_HOSTNAME = env('RENDER_EXTERNAL_HOSTNAME')
    if RENDER_EXTERNAL_HOSTNAME:
        CORS_ALLOWED_ORIGINS.append(RENDER_EXTERNAL_HOSTNAME)
        CSRF_TRUSTED_ORIGINS.append(RENDER_EXTERNAL_HOSTNAME)

SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
      }
   }
}

REST_KNOX = {
  'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
  'AUTH_TOKEN_CHARACTER_LENGTH': 64,
  'TOKEN_TTL': timedelta(hours=10),
  'USER_SERIALIZER': 'account.serializers.CustomUserSerializer',
  'TOKEN_LIMIT_PER_USER': None,
  'AUTO_REFRESH': False,
  'EXPIRY_DATETIME_FORMAT': api_settings.DATETIME_FORMAT,
  'AUTH_HEADER_PREFIX': 'Bearer'
}



# SIMPLE_JWT = {
#     "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
#     "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
#     "ROTATE_REFRESH_TOKENS": False,
#     "BLACKLIST_AFTER_ROTATION": False,
#     "UPDATE_LAST_LOGIN": False,

#     "ALGORITHM": "HS256",
#     "SIGNING_KEY": settings.SECRET_KEY,
#     "VERIFYING_KEY": "",
#     "AUDIENCE": None,
#     "ISSUER": None,
#     "JSON_ENCODER": None,
#     "JWK_URL": None,
#     "LEEWAY": 0,

#     "AUTH_HEADER_TYPES": ("Bearer",),
#     "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
#     "USER_ID_FIELD": "id",
#     "USER_ID_CLAIM": "user_id",
#     "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

#     "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
#     "TOKEN_TYPE_CLAIM": "token_type",
#     "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

#     "JTI_CLAIM": "jti",

#     "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
#     "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
#     "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

#     "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
#     "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
#     "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
#     "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
#     "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
#     "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
# }


STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

CLOUDINARY_STORAGE = {
    'CLOUD_NAME':env('CLOUDINARY_CLOUD_NAME'),
    'API_KEY':env('CLOUDINARY_API_KEY'),
    'API_SECRET':env('CLOUDINARY_API_SECRET')
}


# SECURE_BROWSER_XSS_FILTER=True
# SECURE_CONTENT_TYPE_NOSNIFF=True
# CSRF_COOKIE_SECURE=True
# SESSION_COOKIE_SECURE=True
# SECURE_HSTS_SECONDS = 1576800
# X_FRAME_OPTIONS='DENY'

# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True


# SECURE_SSL_REDIRECT = True

# CSP_DEFAULT_SRC=("'self'",'none')
# CSP_STYLE_SRC=("'self'",)
# CSP_SCRIPT_SRC=("'self'",)
# CSP_IMG_SRC=("'self'",)
# CSP_FONT_SRC=("'self'",)
# CSP_MEDIA_SRC=("'self'",)
# CSP_BASE_URI=("'self'",)

TINYMCE_DEFAULT_CONFIG = {
    "height": "500px",
    "width": "100%",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
    "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
    "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
    "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
    "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
    "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
    "language": "en_En",
  
    "file_picker_types": 'image',
    "file_picker_callback":""" function (cb, value, meta) {
    var input = document.createElement('input');
    input.setAttribute('type', 'file');
    input.setAttribute('accept', 'image/*');

    /*
      Note: In modern browsers input[type="file"] is functional without
      even adding it to the DOM, but that might not be the case in some older
      or quirky browsers like IE, so you might want to add it to the DOM
      just in case, and visually hide it. And do not forget do remove it
      once you do not need it anymore.
    */

    input.onchange = function () {
      var file = this.files[0];

      var reader = new FileReader();
      reader.onload = function () {
        /*
          Note: Now we need to register the blob in TinyMCEs image blob
          registry. In the next release this part hopefully won't be
          necessary, as we are looking to handle it internally.
        */
        var id = 'blobid' + (new Date()).getTime();
        var blobCache =  tinymce.activeEditor.editorUpload.blobCache;
        var base64 = reader.result.split(',')[1];
        var blobInfo = blobCache.create(id, file, base64);
        blobCache.add(blobInfo);

        /* call the callback and populate the Title field with the file name */
        cb(blobInfo.blobUri(), { title: file.name });
      };
      reader.readAsDataURL(file);
    };

    input.click();
  }""",
  "content_style": 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
}

