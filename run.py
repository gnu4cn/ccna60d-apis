#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging

from flask import Flask

from api.conf.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFACATIONS
from api.conf.routes import generate_routes
from api.database.database import db
from api.schemas.schemas import ma
from api.db_initializer.db_initializer import create_super_admin

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(filename='my.log',
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT)

# Create a flask app.
app = Flask(__name__)

# Set debug true for catching the errors.
app.config['DEBUG'] = True

# Set database url.
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFACATIONS

# Database initialize with app.
db.init_app(app)

# Marshmallow initialize with app.
# 避免循环导入
ma.init_app(app)


# New db app if no database.
db.app = app

db.create_all()

generate_routes(app)

if __name__ == '__main__':

    print("Run into CLI.")

    create_super_admin()
    # Debug app
    app.run(port=5000, debug=True, host='localhost', use_reloader=True)
