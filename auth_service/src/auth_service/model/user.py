from enum import Enum

from pydantic import BaseModel


class Role(Enum):
    USER = 1
    ADMIN = 2


class User(BaseModel):
    user_id: int
    name: str
    mail_address: str
    password_hashed: str
    role_id: Role

    def __init__(self, user_id, name, mail_address, password, role_id: Role):
        self.user_id = user_id
        self.name = name
        self.mail_address = mail_address
        self.password_hashed = self._to_hash(password)
        self.role_id = role_id

    def _to_hash(value):
        # TODO: ハッシュ化
        return value
