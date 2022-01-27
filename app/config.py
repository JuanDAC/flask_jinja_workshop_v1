from uuid import uuid4


class Config:
    SECRET_KEY = uuid4().hex
