#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as JWT

# JWT creation.
jwt = JWT('_RSBUOivZ6PyV72wG9g-4XURAL2vf-zqlA_V-kBvXJOuKZRP4Pq2ESM_YXftpuXj4xJ4GYK9yhCPxRMHH3gKk2rqUBtoYBhDYUaiIndjgoCazHVfkUMniOlN4If1lpvm6bhHq-NtMGcdtY7fBNDiolcpreC5CeFjkxYM5bBZzc8', expires_in=3600)

# Auth object creation.
auth = HTTPTokenAuth('Bearer')
