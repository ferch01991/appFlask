#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wtforms import Form
from wtforms import StringField, TextField, HiddenField, PasswordField
from wtforms.fields.html5 import EmailField

from wtforms import validators

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacio.')

class CommentForm(Form):
    username = StringField('Nombre de usuario',
                        [
                            validators.Required(message='El usuario no es valido.'),
                            validators.length(min=4, max=25, message='Ingrese un usuario valido')
                        ])
    email = EmailField('Correo Electronico',
                [
                    validators.Required(message='El email es requerido.'),
                    validators.Email(message='Ingrese un email valido')
                ])
    comment = TextField('Comentario')
    honeypot = HiddenField('', [length_honeypot])
class LoginForm(Form):
    username = StringField('Nombre de usuario',
                        [
                            validators.Required(message='El usuario es requerido.'),
                            validators.length(min=4, max=25, message='Ingrese un usuario valido')
                        ])
    password = PasswordField('Password', [validators.Required(message='El password es requerido')])
