from datetime import datetime
from typing import Optional
from jose import jwt
from pydantic.schema import timedelta

from settings import SECRET_KEY, ALGORITHM


def decode_access_token(
        token: str,
):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, SECRET_KEY, algorithm=ALGORITHM
    )
    return encoded_jwt
