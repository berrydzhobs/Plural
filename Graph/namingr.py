import hashlib
import uuid


def get_topic_picture_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f'00002.000.000.000/t/{filename}'
    # 00002.000.000.000/topic/