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

SECRET_KEY = os.environ.get("SECRET_KEY")

DEBUG = os.environ.get("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS",
    "localhost,127.0.0.1"
).split(",")

CSRF_TRUSTED_ORIGINS = os.environ.get(
    "CSRF_TRUSTED_ORIGINS",
    "http://localhost:3000,http://127.0.0.1:3000"
).split(",")

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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'brays_db',
        'USER': 'brays_db_user',
        'PASSWORD': 'NEsje949F9UeVNdQ3ETYvRUpgS7G33fJ',
        'HOST': 'postgresql://brays_db_user:NEsje949F9UeVNdQ3ETYvRUpgS7G33fJ@dpg-d82ok8vaqgkc739c591g-a.frankfurt-postgres.render.com/brays_db',
        'PORT': '5432'
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

CORS_ALLOWED_ORIGINS = os.environ.get(
    "CORS_ALLOWED_ORIGINS",
    "http://localhost:3000,http://127.0.0.1:3000"
).split(",")

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