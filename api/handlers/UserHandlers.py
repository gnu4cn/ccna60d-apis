#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
from datetime import datetime

from flask import g, request
from flask_restful import Resource

import api.error.errors as error
from api.conf.auth import auth, refresh_jwt
from api.database.database import db
from api.models.models import Blacklist, User
from api.roles import role_required
from api.schemas.schemas import user_schema, users_schema


class Register(Resource):
    @staticmethod
    def post():

        try:
            # Get username, password and email.
            username, password, email = request.json.get('username').strip(), \
                                        request.json.get('password').strip(), \
                                        request.json.get('email').strip()
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

        # Return success if registration is completed.
        return {'status': 'registration completed.'}


class Login(Resource):
    @staticmethod
    def post():

        try:
            # Get user email and password.
            email, password = request.json.get('email').strip(), \
                                request.json.get('password').strip()

            # print(email, password)

        except Exception as why:

            # Log input strip or etc. errors.
            logging.info("Email or password is wrong. " + str(why))

            # Return invalid input error.
            return error.INVALID_INPUT_422

        # Check if user information is none.
        if email is None or password is None:
            return error.INVALID_INPUT_422

        # Get user if it is existed.
        user = User.query.filter_by(email=email).first()

        # Check if user is not existed.
        if user is None:
            return error.DOES_NOT_EXIST

        if user.verify_password(password) is False:
            return error.WRONG_PASSWORD_422

        # Return access token and refresh token.
        return {
            'access_token': user.generate_auth_token(),
            'refresh_token': user.generate_refresh_token()
        }


class Logout(Resource):
    @staticmethod
    @auth.login_required
    def post():

        # Get refresh token.
        refresh_token = request.json.get('refresh_token')

        # Get if the refresh token is in blacklist
        ref = Blacklist.query.filter_by(refresh_token=refresh_token).first()

        # Check refresh token is existed.
        if ref is not None:
            return {'status': 'already invalidated', 'refresh_token': refresh_token}

        # Create a blacklist refresh token.
        blacklist_refresh_token = Blacklist(refresh_token=refresh_token)

        # Add refresh token to session.
        db.session.add(blacklist_refresh_token)

        # Commit session.
        db.session.commit()

        # Return status of refresh token.
        return {'status': 'invalidated', 'refresh_token': refresh_token}


class RefreshToken(Resource):
    @staticmethod
    def post():

        # Get refresh token.
        refresh_token = request.json.get('refresh_token')

        # Get if the refresh token is in blacklist.
        ref = Blacklist.query.filter_by(refresh_token=refresh_token).first()

        # Check refresh token is existed.
        if ref is not None:

            # Return invalidated token.
            return {'status': 'invalidated'}

        try:
            # Generate new token.
            data = refresh_jwt.loads(refresh_token)

        except Exception as why:
            # Log the error.
            logging.error(why)

            # If it does not generated return false.
            return {"status": False}

        # Create user not to add db. For generating token.
        user = User(email=data['email'])

        # New token generate.
        token = user.generate_auth_token()

        # Return new access token.
        return {'access_token': token}


class ResetPassword(Resource):
    @auth.login_required
    def post(self):

        # Get old and new passwords.
        old_pass, new_pass = request.json.get('old_pass'), request.json.get('new_pass')

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
    @role_required.permission(2)
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
    @role_required.permission(1)
    def get(self):

        return {"status": "Test admin data OK."}


class AddUser(Resource):
    @auth.login_required
    @role_required.permission(2)
    def get(self):

        return {"status": "OK"}


class UserProfile(Resource):

    @auth.login_required
    def get(self, id):
        try:
            # Get id
            user = User.query\
                .filter(User.id == id)\
                .one()

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
