#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_marshmallow import Marshmallow

ma = Marshmallow()

class UserProfileSchema(ma.Schema):

    """
        User schema returns only username, email and creation time. This was used in user handlers.
    """

    # Schema parameters.
    class Meta:

        fields = ("id", "username", "email", "created", "activated", "_links")
        # https://marshmallow.readthedocs.io/en/latest/_modules/marshmallow/schema.html#Schema
        dump_only = ("id")


    _links = ma.Hyperlinks(
        {
            "self": ma.URLFor("user", id="<id>"),
            "collection": ma.URLFor("users")
        }
    )

user_schema = UserProfileSchema()
users_schema = UserProfileSchema(many=True)
