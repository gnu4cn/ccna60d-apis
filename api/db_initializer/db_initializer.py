#!/usr/bin/python
# -*- coding: utf-8 -*-

from api.database.database import db
from api.models.user_model import User


def create_super_admin():

    # Check if admin is existed in db.
    user = User.query.filter_by(user_role=3).first()

    # If user is none.
    if user is None:
        sa_username = input("请输入超级管理员用户名，以回车结束：")
        sa_email = input('请输入超级管理员邮箱地址，以回车结束：')
        sa_password = input('请输入超级管理员密码，以回车结束：')

        # Create admin user if it does not existed.
        user = User(username=sa_username,
                    email=sa_email, user_role=3, activated=True)

        user.hash_password(sa_password)

        # Add user to session.
        db.session.add(user)

        # Commit session.
        db.session.commit()

        # Print admin user status.
        print("Super admin was set.")

    else:

        # Print admin user status.
        print("Super admin already set.")


def create_admin_user():

    # Check if admin is existed in db.
    user = User.query.filter_by(email='admin_email@example.com').first()

    # If user is none.
    if user is None:

        # Create admin user if it does not existed.
        user = User(username='admin_username',
                    email='admin_email@example.com', user_role=2)

        user.hash_password('admin_password')

        # Add user to session.
        db.session.add(user)

        # Commit session.
        db.session.commit()

        # Print admin user status.
        print("Admin was set.")

    else:
        # Print admin user status.
        print("Admin already set.")


def create_test_user(username=None, password="test_password", email=None, user_role=None):

    # Check if admin is existed in db.
    user = User.query.filter_by(email='test_email@example.com').first()

    # If user is none.
    if user is None:

        # Create admin user if it does not existed.
        # user = User(username=username, password=password, email=email, user_role=user_role)
        user = User(username='test_username', email='test_email@example.com',
                    user_role=0)

        user.hash_password(password)

        # Add user to session.
        db.session.add(user)

        # Commit session.
        db.session.commit()

        # Print admin user status.
        print("Test user was set.")

    else:

        # Print admin user status.
        print("User already set.")
