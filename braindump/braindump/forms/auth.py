# -*- coding: utf-8 -*-
"""
    braindump.forms.auth
    ~~~~~~~~~~~~~~~~~~~~

    Forms used to register and log into braindump


    :copyright: (c) 2016 by Lev Lazinskiy.
    :license: MIT, see LICENSE for more details.
"""
from braindump.models.user import User
from flask_wtf import FlaskForm
from wtforms import (BooleanField, PasswordField, StringField, SubmitField,
                     ValidationError)
from wtforms.validators import Email, EqualTo, Length, Regexp, Required


class RegistrationForm(FlaskForm):
    """
    Form used to register for a new braindump account
    """
    email = StringField(
        'Email',
        validators=[
            Required(), Length(1, 254), Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Register')


class LoginForm(RegistrationForm):
    """
    Form used to login to braindump
    """
    remember_me = BooleanField('Remember me on this computer for 30 days.')
    submit = SubmitField('Log in')
