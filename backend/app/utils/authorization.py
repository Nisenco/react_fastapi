from typing import Optional
from datetime import timedelta
from datetime import datetime
from jose import jwt
from app.config.config import settings


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Generate access token from user data"""
    to_encode = data.copy()
    # to_encode.update({"exp":  int(time.mktime((datetime.utcnow() + expires_delta).timetuple()))})
    to_encode.update({"exp": datetime.utcnow() + expires_delta})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm="HS256")
    return encoded_jwt
