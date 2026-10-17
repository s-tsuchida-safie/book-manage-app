from auth_service.model.user import User
from fastapi import Request, Response
from pydantic import BaseModel

TOKEN_KEY = "book_app_auth_id"
REQUIRED_ROLE_KEY = "x-required-role"

def _get_required_role(request: Request):
    current_route = request.scope.get("route")

    if current_route and hasattr(current_route, "openapi_extra"):
        extra_data = current_route.openapi_extra
        return extra_data.get(REQUIRED_ROLE_KEY)

    return None


class AuthClient(BaseModel):
    mail_address: str
    name: str
    role_id: int


def verify_auth_param(mail_address: str, password: str):
    # TODO: メールアドレスとパスワード両方の存在チェック
    user = User
    return user


def verify_role(request: Request):
    required_role = _get_required_role(request)

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

def resolve_token(request: Request):
    token = request.cookies.get(TOKEN_KEY)
