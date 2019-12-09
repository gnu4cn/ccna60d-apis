#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as JWT
from itsdangerous import URLSafeTimedSerializer as UST

SECRET_KEY = 'lwFGe4Fc5_papO7h97pFrx-XKfMH3_4-9v6lbzQ3Ddf7JhIqVGJxOsPPXB97XIQxdig1cJSJQtEYqSOYLvwgAg'
SECURITY_PASSWORD_SALT = 'q_Pw0HvoLstvicmBbEKeX-p47ljAUPEicuRoMJC4Oc5MZTbAxE0Rq0LeGxUmwV-KEjIaFAHq6fcZ-X3q80djeg'

# 邮件激活有效期
ACTIVATION_EXPIRATION = 30 * 60

# 认证令牌有效期
TOKEN_EXPIRATION = 7 * 24 * 60 * 60

# JWT creation.
jwt = JWT(SECRET_KEY, expires_in=TOKEN_EXPIRATION)
ust = UST(SECRET_KEY)

# Auth object creation.
auth = HTTPTokenAuth('Bearer')
