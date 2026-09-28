from pydantic import BaseModel, Field


class AuthorizePostIn(BaseModel):
    mail_address: str = Field(..., title="メールアドレス", min_length=3, max_length=264)
    password: str = Field(..., title="パスワード", min_length=8, max_length=20)
    scope: str


class AuthorizePostOut(BaseModel):
    status: str


class TokenExchangePostIn(BaseModel):
    new_scope: str


class TokenExchangePostOut(BaseModel):
    status: str
