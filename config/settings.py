from pathlib import Path
import dj_database_url
import os
import cloudinary

# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

# =========================================================
# SECURITY
# =========================================================

SECRET_KEY = os.environ.get("SECRET_KEY", "django-insecure-development-key-change-in-production")

DEBUG = True  # Development mode

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

# =========================================================
# APPLICATIONS
# =========================================================

INSTALLED_APPS = [
    # Jazzmin
    "jazzmin",

    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third-party apps
    "rest_framework",
    "corsheaders",
    "django_filters",
    "drf_spectacular",
    "cloudinary",
    "cloudinary_storage",
    "ckeditor",
    "ckeditor_uploader",

    # Local apps
    "core",
]

# =========================================================
# MIDDLEWARE
# =========================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "corsheaders.middleware.CorsMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# =========================================================
# URLS & WSGI
# =========================================================

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"

# =========================================================
# TEMPLATES
# =========================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "core" / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ],
        },
    },
]

# =========================================================
# DATABASE
# =========================================================
# =========================================================
# DATABASE
# =========================================================

# Development: Use SQLite
# Production: Use DATABASE_URL environment variable
DATABASE_URL = os.environ.get("DATABASE_URL")

if DATABASE_URL and not DEBUG:
    # Production: Use PostgreSQL via DATABASE_URL
    DATABASES = {
        "default": dj_database_url.config(
            default=DATABASE_URL,
            conn_max_age=600,
            ssl_require=True
        )
    }
else:
    # Development: Use SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# =========================================================
# PASSWORD VALIDATION
# =========================================================

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

# =========================================================
# INTERNATIONALIZATION
# =========================================================

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# =========================================================
# STATIC FILES
# =========================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)

# =========================================================
# MEDIA FILES / CLOUDINARY
# =========================================================

cloudinary.config(
    cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
    api_key=os.environ.get("CLOUDINARY_API_KEY"),
    api_secret=os.environ.get("CLOUDINARY_API_SECRET"),
    secure=True,
)

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# =========================================================
# DJANGO DEFAULTS
# =========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# =========================================================
# DJANGO REST FRAMEWORK
# =========================================================

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",

    "DEFAULT_PAGINATION_CLASS":
        "rest_framework.pagination.PageNumberPagination",

    "PAGE_SIZE": 9,

    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ],
}

# =========================================================
# DRF SPECTACULAR
# =========================================================

SPECTACULAR_SETTINGS = {
    "TITLE": "Braymell API",
    "DESCRIPTION": "Braymell backend API",
    "VERSION": "1.0.0",
}

# =========================================================
# CORS
# =========================================================

CORS_ALLOW_CREDENTIALS = True

# Development: Allow all origins
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost",
    "http://127.0.0.1",
]

# For development, you can also allow all with:
# CORS_ALLOW_ALL_ORIGINS = True

# =========================================================
# CKEDITOR
# =========================================================

CKEDITOR_UPLOAD_PATH = "uploads/"

# =========================================================
# SECURITY HEADERS (PRODUCTION)
# =========================================================

if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True

    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    SECURE_SSL_REDIRECT = True

    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# =========================================================
# JAZZMIN
# =========================================================

JAZZMIN_SETTINGS = {
    "site_title": "Braymell Admin",
    "site_header": "Braymell Dashboard",
    "site_brand": "Braymell",

    "welcome_sign": "Welcome to Braymell Admin Dashboard",

    "copyright":
        "Braymell TradeMasters LTD",

    "site_logo": "images/logo.jpeg",
    "login_logo": "images/logo.jpeg",
    "site_icon": "images/logo.jpeg",

    "search_model": "core.Project",

    "user_avatar": None,

    "topmenu_links": [
        {
            "name": "Home",
            "url": "admin:index",
            "permissions": ["auth.add_user"],
        },
        {
            "name": "API Docs",
            "url": "/api/docs/",
            "new_window": True,
        },
    ],

    "usersidebar_links": [
        {
            "name": "View Site",
            "url": "/",
            "new_window": True,
        },
    ],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.Group": "fas fa-user-shield",
        "auth.user": "fas fa-user",

        "core.project": "fas fa-briefcase",
        "core.projectimage": "fas fa-images",
        "core.testimonial": "fas fa-comment-dots",
        "core.clientlogo": "fas fa-handshake",
        "core.brand": "fas fa-tags",
        "core.client": "fas fa-building-user",
    },

    "default_icon_parents": "fas fa-chevron-right",
    "default_icon_children": "fas fa-arrow-right",

    "related_modal_active": True,

    "changeform_format": "single",

    "changeform_format_overrides": {
        "core.project": "collapsible",
        "auth.user": "horizontal_tabs",
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small": False,
    "footer_small": False,
    "body_small": False,

    "brand_small": False,
    "brand_bold": True,

    "sidebar_nav_small": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,

    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,

    "theme": "default",
    "dark_mode_theme": "darkly",

    "button_corners": "rounded-1",
    "action_button_style": "squared-0",

    "actions_sticky_top": True,
}