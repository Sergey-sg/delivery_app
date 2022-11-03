# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/
import os

from django.conf import settings

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_L10N = True
USE_TZ = True
gettext = lambda s: s
LANGUAGES = (
    ('en', gettext('English')),
    ('uk', gettext('Українська')),
)
LOCALE_PATHS = (
    os.path.join(settings.BASE_DIR, 'locale'),
)

MODELTRANSLATION_FALLBACK_LANGUAGES = ('en', 'uk')
