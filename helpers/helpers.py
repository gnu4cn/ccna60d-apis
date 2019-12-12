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

# socket-io login_required
def login_required_socket_io(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            token = request.args.get("token", None)

            data = jwt.loads(token)

        except ValueError:
            disconnect(request.sid)

        except Exception as why:
            logging.error(why)
            disconnect(request.sid)

        return f(*args, **kwargs)

    return decorated_function
