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
    api.add_resource(Register, '/api/auth/register')

    # Login page.
    api.add_resource(Login, '/api/auth/login')

    # Password reset page. Not forgot.
    api.add_resource(ResetPassword, '/api/auth/password_reset')

    # Get users page with admin permissions.
    api.add_resource(UsersList, '/api/users', endpoint="users")

    # Example admin handler for admin permission.
    api.add_resource(DataAdminRequired, '/api/data_admin')

    # Example user handler for user permission.
    api.add_resource(UserProfile, '/api/user/<id>', endpoint='user')

    # Example user handler for user permission.
    api.add_resource(AddUser, '/api/user_add')

    api.add_resource(UserActivation, '/activation/<token>', endpoint='activation')

    api.add_resource(UserSendActivation, '/api/auth/send_activation_mail')
