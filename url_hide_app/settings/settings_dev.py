import os
from .settings_base import INSTALLED_APPS


if os.environ.get('DJANGO_DEBUG') == 'True':
    INSTALLED_APPS += [
        'django_extensions',
    ]
