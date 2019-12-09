#!/usr/bin/python

from validate_email import validate_email
import re

from conf.config import USERNAME_REGEX, EMAIL_USERNAME_REGEX

username_p = re.compile(USERNAME_REGEX)
email_username_p = re.compile(EMAIL_USERNAME_REGEX)

def t_username(username_str):
    if username_p.match(username_str):
        return username_str
    else:
        raise ValueError('{} is not a valid username'.format(username_str))

def t_email_username(email_username_str):
    if email_username_p.match(email_username_str):
        return email_username_str
    else:
        raise ValueError('{} is not a valid username or email'.format(email_username_str))

def t_email(email_str):
    """Return email_str if valid, raise an exception in other case."""
    if validate_email(email_str):
        return email_str
    else:
        raise ValueError('{} is not a valid email'.format(email_str))

def t_password(password_str):
    if len(password_str) >= 5:
        return password_str
    else:
        raise ValueError('{} is not a valid passord'.format(password_str))

