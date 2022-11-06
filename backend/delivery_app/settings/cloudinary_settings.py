from delivery_app.settings.settings import INSTALLED_APPS
from delivery_app.settings.environ_settings import env


INSTALLED_APPS += ['cloudinary_storage', 'cloudinary',]

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': env('CLOUD_NAME'),
    'API_KEY': env('API_KEY'),
    'API_SECRET': env('API_SECRET'),
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
