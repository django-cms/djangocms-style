import importlib.util
import os

SECRET_KEY = "djangocms-style-test"

ALLOWED_HOSTS = ["localhost"]

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sites",
    "django.contrib.sessions",
    "django.contrib.admin",
    "django.contrib.messages",
    "cms",
    "menus",
    "treebeard",
    "djangocms_style",
]

if importlib.util.find_spec("djangocms_versioning") is not None:  # V4 test?
    INSTALLED_APPS += [
        "djangocms_versioning",
    ]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(os.path.dirname(__file__), "templates"),
        ],
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

SITE_ID = 1

CMS_TEMPLATES = (("page.html", "Normal page"),)

CMS_LANGUAGES = {
    1: [
        {
            "code": "en",
            "name": "English",
        }
    ]
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "mydatabase",
    }
}

LANGUAGE_CODE = "en"

ROOT_URLCONF = "tests.urls"

CMS_CONFIRM_VERSION4 = True
