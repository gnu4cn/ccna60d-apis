#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging

from flask import Flask
from flask_cors import CORS

from conf.config import (SQLALCHEMY_DATABASE_URI,
                         SQLALCHEMY_TRACK_MODIFACATIONS,
                         MAIL_SERVER,
                         MAIL_PORT,
                         MAIL_PASSWORD,
                         MAIL_USERNAME,
                         MAIL_USE_SSL,
                         DEFAULT_MAIL_SENDER
                         )
from api.routes import generate_routes
from database.database import db
from schemas.schemas import ma
from db_initializer.db_initializer import create_super_admin
from mail_sender.mail import mail

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(filename='my.log',
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT)

# Create a flask app.
# 这里涉及到 Flask 模板机制，render_template将在根目录下的 templates 文件夹中
# 查找模板文件
app = Flask(__name__, template_folder="templates")
cors = CORS(app, resources={r"/api/*": {"origins": "http://localhost:8100"}})

# Set debug true for catching the errors.
app.config['DEBUG'] = True

# Set database url.
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFACATIONS

# Set email parameters
app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_SSL'] = MAIL_USE_SSL
app.config['DEFAULT_MAIL_SENDER'] = DEFAULT_MAIL_SENDER

# Database initialize with app.
db.init_app(app)

# Marshmallow initialize with app.
# 避免循环导入
ma.init_app(app)
mail.init_app(app)

# New db app if no database.
db.app = app

db.create_all()

generate_routes(app)

if __name__ == '__main__':

    print("Run into CLI.")

    create_super_admin()
    # Debug app
    app.run(port=5000, debug=True, host='localhost', use_reloader=True)
