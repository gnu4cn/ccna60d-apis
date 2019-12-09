#! /usr/bin/python

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_token = request.args.get("auth_token", None)
        if auth_token is None:
            disconnect(sid=request.sid)
        else:
            status = UserQueries.check_session(user_id=user_id,
                                               store="test")
            if not status:
                disconnect(request.sid)

            return f(*args, **kwargs)

        return decorated_function
