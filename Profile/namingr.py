import hashlib
import uuid


def get_profile_picture_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f'00003.000.000.000/u/a/{filename}'
    # 00003.000.000.000/users/avatars/

def get_profile_cover_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f'00003.000.000.000/u/c/{filename}'
    # 00003.000.000.000/users/covers/


def get_profile_trademark_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f'00003.000.000.000/u/t/{filename}'
    # 00003.000.000.000/users/trademark/