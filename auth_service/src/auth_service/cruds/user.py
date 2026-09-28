from auth_service.model.user import User


def insert_user(user: User):
    # TODO: ユーザーのレコード追加
    user_id = 20
    return user_id


def update_user(user: User):
    return user


def find_user_by_id(user_id: int):
    # TODO: ユーザーIDでユーザーを取得
    return User


def find_user_by_mail_address(mail_address: str):
    # TODO: メールアドレスでユーザーを取得
    return User
