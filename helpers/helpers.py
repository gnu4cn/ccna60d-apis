import json
from api.conf.auth import ust

class CustomJsonDumpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return str(obj, encoding='utf-8')
        return json.JSONEncoder.default(self, obj)

# 激活确认
def confirm_activation(token, expiration=15*60):
    try:
        email = ust.loads(
            token,
            salt = SECURITY_PASSWORD_SALT,
            max_age = expiration
        )
    except:
        return False

    return email
