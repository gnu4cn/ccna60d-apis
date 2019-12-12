#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging

from flask import Flask
from flask_socketio import SocketIO

from conf.config import (
    SECRET_KEY,
    SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFACATIONS,
    MAIL_SERVER,
    MAIL_PORT,
    MAIL_PASSWORD,
    MAIL_USERNAME,
    MAIL_USE_SSL,
    DEFAULT_MAIL_SENDER
)

from database.database import db
from schemas.schemas import ma
from mail_sender.mail import mail
from socket_io.sockets import generate_sockets

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
socketio = SocketIO(app,
                    cors_allowed_origins="http://localhost:8100"
                    )

# Set debug true for catching the errors.
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = SECRET_KEY

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


@app.route('/')
def index():
	return 'Yey', 201

generate_sockets(socketio)

if __name__ == '__main__':

    print("Run into CLI.")

    socketio.run(app, port=5001, debug=True, host='localhost', use_reloader=True)
