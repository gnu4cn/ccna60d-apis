#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# For the database
POSTGRES_USER='peng'
POSTGRES_PW=os.getenv('POSTGRES_PW')
POSTGRES_URL='127.0.0.1:5432'
POSTGRES_DB='ccna60d'

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user=POSTGRES_USER,
    pw=POSTGRES_PW,
    url=POSTGRES_URL,
    db=POSTGRES_DB)

# Create a database in project and get it's path.
SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFACATIONS = False

# For email sending.
MAIL_SERVER = 'smtp.163.com'
MAIL_PORT = 994
MAIL_USE_SSL = True
MAIL_USERNAME = 'gnu4cn@163.com'
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
DEFAULT_MAIL_SENDER='gnu4cn@163.com'
