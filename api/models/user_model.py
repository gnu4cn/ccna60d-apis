#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from passlib.apps import custom_app_context as pwd_context

from flask import g

from api.conf.auth import auth, jwt
from api.database.database import db


class User(db.Model):

    # Generates default class name for table. For changing use
    __tablename__ = 'sys_users'

    # User id.
    id = db.Column(db.Integer, primary_key=True)

    # User name.
    username = db.Column(db.String(length=80))

    # User password.
    password_hash = db.Column(db.String(length=128))

    # User email address.
    email = db.Column(db.String(length=80))

    # Creation time for user.
    created = db.Column(db.DateTime, default=datetime.utcnow)

    # Unless otherwise stated default role is user.
    user_role = db.Column(db.Integer, default='0')

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    # Generates auth token.
    def generate_auth_token(self):

        return str(jwt.dumps({'email': self.email, 'admin': self.user_role}), encoding='utf-8')

    # Generates a new access token from refresh token.
    @staticmethod
    @auth.verify_token
    def verify_auth_token(token):

        # Create a global none user.
        g.user = None

        try:
            # Load token.
            data = jwt.loads(token)

        except:
            # If any error return false.
            return False

        # Check if email and admin permission variables are in jwt.
        if 'email' and 'admin' in data:

            # Set email from jwt.
            g.user = data['email']

            # Set admin permission from jwt.
            g.admin = data['admin']

            # Return true.
            return True

        # If does not verified, return false.
        return False

    def __repr__(self):

        # This is only for representation how you want to see user information after query.
        return "<User(id='%s', name='%s', password='%s', email='%s', created='%s')>" % (
            self.id, self.username, self.password, self.email, self.created)
