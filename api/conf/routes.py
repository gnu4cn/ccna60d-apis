#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_restful import Api

from api.handlers.UserHandlers import (AddUser, DataAdminRequired,
                                       UserProfile, Login,
                                       Register, ResetPassword,
                                       UsersList, UserActivation,
                                       UserSendActivation)


def generate_routes(app):

    # Create api.
    api = Api(app)

    # Add all routes resources.
    # Register page.
    api.add_resource(Register, '/v1/auth/register')

    # Login page.
    api.add_resource(Login, '/v1/auth/login')

    # Password reset page. Not forgot.
    api.add_resource(ResetPassword, '/v1/auth/password_reset')

    # Get users page with admin permissions.
    api.add_resource(UsersList, '/users', endpoint="users")

    # Example admin handler for admin permission.
    api.add_resource(DataAdminRequired, '/data_admin')

    # Example user handler for user permission.
    api.add_resource(UserProfile, '/user/<id>', endpoint='user')

    # Example user handler for user permission.
    api.add_resource(AddUser, '/user_add')

    api.add_resource(UserActivation, '/activation/<token>', endpoint='activation')

    api.add_resource(UserSendActivation, '/send_activation_mail')
