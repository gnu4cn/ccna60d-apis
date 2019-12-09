import json
from conf.auth import (ust,
                       SECURITY_PASSWORD_SALT,
                       ACTIVATION_EXPIRATION)

class CustomJsonDumpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

# 激活确认
def confirm_activation(token, expiration=ACTIVATION_EXPIRATION):
    try:
        email = ust.loads(
            token,
            salt = SECURITY_PASSWORD_SALT,
            max_age = expiration
        )

    except Exception as why:
        return False

    return email
