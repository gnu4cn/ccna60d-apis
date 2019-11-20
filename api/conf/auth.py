#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as JWT

# JWT creation.
jwt = JWT('_RSBUOivZ6PyV72wG9g-4XURAL2vf-zqlA_V-kBvXJOuKZRP4Pq2ESM_YXftpuXj4xJ4GYK9yhCPxRMHH3gKk2rqUBtoYBhDYUaiIndjgoCazHVfkUMniOlN4If1lpvm6bhHq-NtMGcdtY7fBNDiolcpreC5CeFjkxYM5bBZzc8', expires_in=3600)

# Refresh token creation.
refresh_jwt = JWT('7wDTV_GuJXJJpQ-66M2RxrmjPKBdU5bnQ7xpzt9jxuENqGNgaoqTTNngRPKdZHSPCP0tedkCvZMAndah1wJ9Dhs2MGXIFkzhjUg-02DF0CjhJ5DRuNR3DTB0faGC3fRG-xKBUGg2nB0ZvAUkQVxUekk_BeNslGRonAws1ZzPa0E', expires_in=7200)

# Auth object creation.
auth = HTTPTokenAuth('Bearer')
