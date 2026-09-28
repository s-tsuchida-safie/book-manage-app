from pydantic import BaseModel, Field


class AdminPostIn(BaseModel):
    name: str = Field(..., title="ユーザー名", min_length=1, max_length=255)
    mail_address: str = Field(..., title="メールアドレス", min_length=3, max_length=255)
    password: str = Field(..., title="パスワード", min_length=8, max_length=20)


class AdminPostOut(BaseModel):
    user_id: int
