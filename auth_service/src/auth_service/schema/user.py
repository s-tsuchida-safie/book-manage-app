from pydantic import BaseModel, Field


class UserPostIn(BaseModel):
    name: str = Field(..., title="ユーザー名", min_length=1, max_length=255)
    mail_address: str = Field(..., title="メールアドレス", min_length=3, max_length=255)
    password: str = Field(..., title="パスワード", min_length=8, max_length=20)


class UserPostOut(BaseModel):
    user_id: int


class UserPatchIn(BaseModel):
    name: str | None = Field(..., title="ユーザー名", min_length=1, max_length=255)
    mail_address: str | None = Field(
        ..., title="メールアドレス", min_length=3, max_length=255
    )
    password: str | None = Field(..., title="パスワード", min_length=8, max_length=20)


class UserPatchOut(BaseModel):
    status: str


class UserDeleteOut(BaseModel):
    status: str
