import environ
from pathlib import Path

# --- Path Configuration ---
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Path to the frontend directory (useful for Vite config reference)
FRONTEND_DIR = BASE_DIR.parent / 'frontend'

# --- Environment Variables Configuration ---
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    DJANGO_VITE_DEV_MODE=(bool, False), # Default to False (production mode)
    # Add defaults for other variables you expect in .env
)

# Read .env file located at the project root (../.env relative to this settings.py)
# Or keep it in BASE_DIR if you prefer: environ.Env.read_env(BASE_DIR / '.env')
# For Docker, env vars are often passed directly, but reading .env is good for local dev.
environ.Env.read_env(BASE_DIR / '.env') # Reads .env file in the 'backend' directory

# --- Core Django Settings ---
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG') # Load DEBUG from .env

# Define allowed hosts based on environment variable
# Example .env: ALLOWED_HOSTS=localhost,127.0.0.1,backend
# The 'backend' hostname is crucial for Docker Compose service communication
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['localhost', '127.0.0.1'])

# --- Application Definition ---
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'corsheaders',
    'django_vite',
    'rest_framework', # Make sure DRF is installed and added

    # Your apps
    'users.apps.UsersConfig',
    'api.apps.ApiConfig', # Use AppConfig for clarity if defined
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Should be placed high, before CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_vite_template.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Use pathlib for consistency
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'django_vite_template.wsgi.application'

# --- Database Configuration ---
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    # Reads DATABASE_URL env var
    # Example .env: DATABASE_URL=sqlite:///db.sqlite3
    # Example .env: DATABASE_URL=psql://user:pass@db_host:port/db_name
    'default': env.db(default=f'sqlite:///{BASE_DIR / "db.sqlite3"}') # Sensible default
}

# --- Password Validation ---
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# --- Internationalization ---
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Static Files Configuration (CSS, JavaScript, Images) ---
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = '/static/'

# Directory where Vite builds assets (relative to Django BASE_DIR)
# Use pathlib here
DJANGO_VITE_ASSETS_PATH = BASE_DIR / 'frontend_dist'

# Where collectstatic will gather static files for production.
# Use pathlib here
STATIC_ROOT = BASE_DIR / 'staticfiles_prod'

# Add the Vite build directory to STATICFILES_DIRS
STATICFILES_DIRS = [
    DJANGO_VITE_ASSETS_PATH,
]

# --- Django Vite Configuration ---
# https://github.com/MrBin99/django-vite#configuration

# Vite server HMR URL (used by template tags)
# Needs to point to the Vite container in Docker development
# Example .env: DJANGO_VITE_DEV_SERVER_URL=http://frontend:5173
DJANGO_VITE_DEV_SERVER_URL = env('DJANGO_VITE_DEV_SERVER_URL', default='http://localhost:5173')

# Read DEV_MODE from env, default to DEBUG value if not set explicitly
# Example .env: DJANGO_VITE_DEV_MODE=True
DJANGO_VITE_DEV_MODE = env.bool('DJANGO_VITE_DEV_MODE', default=DEBUG)


# --- CORS Configuration ---
# https://github.com/adamchainz/django-cors-headers
# Define allowed origins based on environment variable
# Example .env: CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173,http://localhost:8000
# Add your production frontend domain here too when deploying
CORS_ALLOWED_ORIGINS = env.list('CORS_ALLOWED_ORIGINS', default=[
    'http://localhost:5173', # Default Vite dev origin
    'http://127.0.0.1:5173',
    'http://localhost:8000', # Django itself, in case frontend calls API from same origin
    DJANGO_VITE_DEV_SERVER_URL, # Add the configured Vite URL just in case
])

# If you need to allow credentials (cookies, authorization headers)
# CORS_ALLOW_CREDENTIALS = True

# Alternatively, for wider development access (use with caution):
# if DEBUG:
#     CORS_ALLOW_ALL_ORIGINS = True

# --- Authentication Configuration ---
AUTH_USER_MODEL = 'users.CustomUser'

# --- Default primary key field type ---
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# --- Optional: Logging Configuration ---
# LOGGING = { ... } # Add logging configuration if needed

# --- Optional: Celery Configuration (if using background tasks) ---
# CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='redis://localhost:6379/0')
# CELERY_RESULT_BACKEND = env('CELERY_RESULT_BACKEND', default='redis://localhost:6379/0')
