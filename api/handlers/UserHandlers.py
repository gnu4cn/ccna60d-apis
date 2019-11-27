#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from datetime import datetime

from flask import g
from flask_restful import Resource, reqparse
from sqlalchemy import or_

import api.error.errors as error
from api.conf.auth import auth, TOKEN_EXPIRATION
from api.database.database import db
from api.models.user_model import User
from api.roles import role_required
from api.schemas.schemas import user_schema, users_schema
from helpers.helpers import confirm_activation

# https://flask-restful.readthedocs.io/en/0.3.5/intermediate-usage.html#full-parameter-parsing-example
from helpers.reqparser_helpers import email

regParser = reqparse.RequestParser()
regParser.add_argument('username', type=str, help='用户名', location='json',
                       store_missing=True, default='visitor')
regParser.add_argument('password', type=str, help='密码', required=True,
                       location='json')
regParser.add_argument('email', type=email, help='邮件地址格式不符合要求',
                       required=True, location='json')

class Register(Resource):
    @staticmethod
    def post():

        try:
            args = regParser.parse_args()
            # Get username, password and email.
            username, password, email = args['username'], args['password'], \
                args['email']
        except Exception as why:

            # Log input strip or etc. errors.
            logging.info("Username, password or email is wrong. " + str(why))

            # Return invalid input error.
            return error.INVALID_INPUT_422

        # Check if any field is none.
        if username is None or password is None or email is None:
            return error.INVALID_INPUT_422

        # Get user if it is existed.
        user = User.query.filter_by(email=email).first()

        # Check if user is existed.
        if user is not None:
            return error.ALREADY_EXIST

        # Create a new user.
        user = User(username=username, email=email)
        user.hash_password(password)

        # Add user to session.
        db.session.add(user)

        # Commit session.
        db.session.commit()

        return {
            'status': 'registration completed.',
            'activation_sent': user.send_activation_mail()
        }


loginParser = reqparse.RequestParser()
loginParser.add_argument('password', type=str, help='密码', required=True,
                       location='json')
loginParser.add_argument('username_or_email', type=str, help='账户名或邮箱地址', \
                       required=True, location='json')

class Login(Resource):
    @staticmethod
    def post():

        try:
            args = loginParser.parse_args()
            # Get user email and password.
            username_or_email, password = args['username_or_email'], \
                args['password']

            # print(username_or_email, password)

        except Exception as why:

            # Log input strip or etc. errors.
            logging.info("Email or password is wrong. " + str(why))

            # Return invalid input error.
            return error.INVALID_INPUT_422

        # Check if user information is none.
        if username_or_email is None or password is None:
            return error.INVALID_INPUT_422

        # Get user if it is existed.
        # Only activated can login.
        user = User.query.filter(or_(User.email==username_or_email,
                                     User.username==username_or_email)
        ).first()

        # Check if user is not existed.
        if user is None:
            return error.DOES_NOT_EXIST

        if user.verify_password(password) is False:
            return error.WRONG_PASSWORD_422

        # Return access token and refresh token.
        return {
            'access_token': user.generate_auth_token(),
            'token_expiration': TOKEN_EXPIRATION
        }


resetParser = reqparse.RequestParser()
resetParser.add_argument('old_password', type=str, help='原密码', required=True,
                       location='json')
resetParser.add_argument('new_password', type=str, help='新密码', required=True,
                       location='json')


class ResetPassword(Resource):
    @auth.login_required
    def post(self):

        args = resetParser.parse_args()
        # Get old and new passwords.
        old_pass, new_pass = args['old_password'], args['new_password']

        # Get user. g.user generates email address cause we put email address to g.user in models.py.
        user = User.query.filter_by(email=g.user).first()

        # Check if user password does not match with old password.
        if user.verify_password(old_pass) is False:

            # Return does not match status.
            return {'status': 'old password does not match.'}

        # Update password.
        user.hash_password(new_pass)

        # Commit session.
        db.session.commit()

        # Return success status.
        return {'status': 'password changed.'}


class UsersList(Resource):
    @auth.login_required
    @role_required.permission(3)
    def get(self):
        try:

            users = User.query.all()

            # Get json data
            data = users_schema.dump(users)

            # Return json data from db.
            return data

        except Exception as why:

            print(why)

            # Log the error.
            logging.error(why)

            # Return error.
            return error.INVALID_INPUT_422


# auth.login_required: Auth is necessary for this handler.
# role_required.permission: Role required user=0, admin=1 and super admin=2.

class DataAdminRequired(Resource):
    @auth.login_required
    @role_required.permission(2)
    def get(self):

        return {"status": "Test admin data OK."}


class AddUser(Resource):
    @auth.login_required
    @role_required.permission(3)
    def get(self):

        return {"status": "OK"}


class UserProfile(Resource):
    @auth.login_required
    def get(self, id):
        try:
            # Get id
            user = User.query.filter_by(id = id).first()

            # Get json data
            data = user_schema.dump(user)

            # Return json data from db.
            return data

        except Exception as why:

            print(why)

            # Log the error.
            logging.error(why)

            # Return error.
            return error.INVALID_INPUT_422

class UserActivation(Resource):
    def get(self, token):
        result = confirm_activation(token)

        if result is False:
            return {'status': 'Activation failed'}
        else:
            user = User.query.filter_by(email=result).first()

            user.user_role = 1

            db.session.commit()

            return {'status': 'Activation complete.'}


class UserSendActivation(Resource):
    @auth.login_required
    def get(self):
        user = User.query.filter_by(email=g.email).first()

        if user.user_role > 0:
            return {
                'status': 'User already activated.',
                'email': g.email
            }
        else:
            return {
                'activation_sent': user.send_activation_mail()
            }
