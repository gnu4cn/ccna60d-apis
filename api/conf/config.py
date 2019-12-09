#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# For the database
POSTGRES_USER='peng'
# os.getenv() 所能获取到的环境变量，与系统环境变量有所不同，是设置在
# conf.d/uwsgi.conf配置文件中的
POSTGRES_PW=os.getenv('POSTGRES_PW')
POSTGRES_URL='127.0.0.1:5432'
POSTGRES_DB='ccna60d_apis'

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=POSTGRES_USER,
    pw=POSTGRES_PW,
    url=POSTGRES_URL,
    db=POSTGRES_DB)

# Create a database in project and get it's path.
SQLALCHEMY_TRACK_MODIFACATIONS = False

# For email sending.
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 994
MAIL_USE_SSL = True
MAIL_USERNAME = 'gnu4cn@163.com'
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
DEFAULT_MAIL_SENDER='gnu4cn@163.com'

# 正则表达式：必须以大小写字母开头，只能包含大小写字母、数字、下划线和短横线
USERNAME_REGEX = '^[a-zA-Z0-9_]{1}[a-zA-Z0-9_-]{4,24}$'

# 非常好的验证邮件地址的正则表达式
EMAIL_REGEX = '^[a-zA-Z0-9_.+-]{5,25}\@[a-zA-Z0-9-]{2,16}\.[a-zA-Z]{2,4}$'
EMAIL_USERNAME_REGEX = '^([a-zA-Z0-9_.+-]{5,25}|[a-zA-Z0-9_]{1})([a-zA-Z0-9_-]{4,24}|\@[a-zA-Z0-9-]{2,16}\.[a-zA-Z]{2,4})$'

