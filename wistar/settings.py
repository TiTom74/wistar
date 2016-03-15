"""
Django settings for wistar project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MEDIA_ROOT = '/opt/images'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8lsqwq$3a(spg-i)1mtoc*8zv8_qmp#bmcd(z_y3181&ye2^)c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
                               "django.core.context_processors.debug",
                               "django.core.context_processors.i18n",
                               "django.core.context_processors.media",
                               "django.core.context_processors.static",
                               "django.core.context_processors.tz",
                               "django.contrib.messages.context_processors.messages",
                               "common.lib.context_processor.add_load"
                               )


ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'topologies',
    'images',
    'scripts',
    'common',
    'ajax',
    'webConsole',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'wistar.urls'

WSGI_APPLICATION = 'wistar.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Registered VM Image types
# this list will register the javascript VM configuration settings in
# common/static/js/vm_types

VM_IMAGE_TYPES = [
    {
        "name": "blank",
        "description": "Blank",
        "js": "draw2d.shape.node.generic",
        "relationship_status": "single",
        "cloud_init": "nope",
        "dummy_interfaces": [],
    },
    {
        "name": "linux",
        "description": "Ubuntu Linux",
        "js": "draw2d.shape.node.linux",
        "relationship_status": "single",
        "cloud_init": "yep",
        "dummy_interfaces": [],

    },
    {
        "name": "junos_vmx",
        "description": "Junos vMX Phase 1",
        "js": "draw2d.shape.node.vmx",
        "relationship_status": "single",
        "cloud_init": "nope",
        "dummy_interfaces": [],
    },
    {
        "name": "junos_vre",
        "description": "Junos vMX RE",
        "js": "draw2d.shape.node.vre",
        "relationship_status": "parent",
        "cloud_init": "nope",
        "dummy_interfaces": [],
    },
    {
        "name": "junos_vpfe",
        "description": "Junos vMX vPFE",
        "js": "draw2d.shape.node.vpfe",
        "relationship_status": "child",
        "cloud_init": "nope",
        "dummy_interfaces": [],
    },
    {
        "name": "junos_vqfx_re",
        "description": "Junos vQFX RE",
        "js": "draw2d.shape.node.vqfxRe",
        "relationship_status": "parent",
        "cloud_init": "nope",
        "dummy_interfaces": [],
    },
    {
        "name": "junos_vqfx_cosim",
        "description": "Junos vQFX Cosim",
        "js": "draw2d.shape.node.vqfxCosim",
        "relationship_status": "child",
        "cloud_init": "nope",
        "dummy_interfaces": [],
    },
    {
        "name": "generic",
        "description": "Other",
        "js": "draw2d.shape.node.generic",
        "relationship_status": "single",
        "cloud_init": "nope",
        "dummy_interfaces": [],
    },
    {
        "name": "junos_firefly",
        "description": "Junos vSRX",
        "js": "draw2d.shape.node.vsrx",
        "relationship_status": "single",
        "cloud_init": "nope",
        "dummy_interfaces": [],
    },
    {
        "name": "junos_vmx_hdd",
        "description": "Junos vMX HDD",
        "js": "draw2d.shape.node.generic",
        "relationship_status": "child",
        "cloud_init": "nope",
        "dummy_interfaces": [],
    }
]
