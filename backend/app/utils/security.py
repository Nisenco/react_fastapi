from app.config import settings
import hashlib


def make_password(password):
    SECRET_KEY = settings.salt
    password = SECRET_KEY + password
    # 2.开始加密
    sha256_obj = hashlib.sha256()
    sha256_obj.update(password.encode())
    ret = sha256_obj.hexdigest()
    return ret
