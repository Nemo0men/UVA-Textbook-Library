from .settings import *

# Override storage backend for testing
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}

# Use a test-specific secret key
SECRET_KEY = 'test-key-123'

# Disable AWS settings for testing
AWS_ACCESS_KEY_ID = None
AWS_SECRET_ACCESS_KEY = None
AWS_STORAGE_BUCKET_NAME = None
AWS_S3_CUSTOM_DOMAIN = None

# Use local file storage for media files during tests
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 