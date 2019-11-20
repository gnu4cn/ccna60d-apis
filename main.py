#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import logging

from flask import Flask

from api.conf.config import SQLALCHEMY_DATABASE_URI
from api.conf.routes import generate_routes
from api.database.database import db
from api.schemas.schemas import ma
from api.db_initializer.db_initializer import (create_admin_user,
                                               create_super_admin,
                                               create_test_user)
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT,
                    datefmt=DATE_FORMAT)

def create_app():

    # Create a flask app.
    app = Flask(__name__)

    # Set debug true for catching the errors.
    app.config['DEBUG'] = True

    # Set database url.
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # Database initialize with app.
    db.init_app(app)

    # Marshmallow initialize with app.
    # 避免循环导入
    ma.init_app(app)

    # Check if there is no database.
    if not os.path.exists(SQLALCHEMY_DATABASE_URI):

        # New db app if no database.
        db.app = app

        # Create all database tables.
        db.create_all()

        create_super_admin()

        create_admin_user()

    # Return app.
    return app


if __name__ == '__main__':

    # Create app.
    app = create_app()

    # Generate routes.
    generate_routes(app)

    # Run app.
    app.run(port=5000, debug=True, host='localhost', use_reloader=True)
