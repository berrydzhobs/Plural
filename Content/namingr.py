import hashlib
import uuid

def get_app_icon_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f'app/icons/{filename}'

def get_app_thumbnail_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f'app/thumbnails/{filename}'

def get_appcarousel_media_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f'app/carousels/{filename}'
    