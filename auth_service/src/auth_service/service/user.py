from auth_service.cruds.user import find_user_by_id, find_user_by_mail_address


def is_exist_mail_address(mail_address):
    user = find_user_by_mail_address(mail_address)
    return bool(user)


def is_exist_user(user_id):
    user = find_user_by_id(user_id)
    return bool(user)
