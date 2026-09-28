from auth_service.model.user import User
from fastapi import Request, Response
from pydantic import BaseModel

TOKEN_KEY = "book_app_auth_id"
REQUIRED_ROLE_KEY = "x-required-role"


class AuthClient(BaseModel):
    mail_address: str
    name: str
    role_id: int


def verify_auth_param(mail_address: str, password: str):
    # TODO: メールアドレスとパスワード両方の存在チェック
    user = User
    return user


def verify_role(request: Request):
    # TODO: REQUIRED_ROLE_KEYから必要なロールの値を取得

    # TODO: JWTトークンからロールを取り出してチェック
    return AuthClient(mail_address="", name="", role_id=1)


def _create_token(user: User):
    # TODO: JWTトークンの作成
    token = ""
    return token


def attach_token(response: Response, user: User):
    # トークンの作成
    token = _create_token(user)
    response.set_cookie(TOKEN_KEY, token)
