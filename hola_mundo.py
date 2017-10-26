#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask import g
from flask_wtf.csrf import CSRFProtect

from config import DevelopmentConfig

from models import db
from models import User

from flask import flash
from flask import url_for
from flask import redirect

import forms
import json

app = Flask(__name__)
# configuraciones de config
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    title = 'Page no found'
    return render_template('404.html', title=title)

# antes que una peticion se procece, para validar usuarios o redirigir, condiciones que se deben ejecutar antes de responder al cliente
@app.before_request
def before_request():
    pass


@app.route('/ajax-login', methods=['POST'])
def ajax_login():
    print (request.form)
    username=request.form['username']
    response={'status': 200, 'username': username, 'id': 1}
    return json.dumps(response)

@app.route('/create', methods=['GET' ,'POST'])
def create():
    title = 'Nuevo'
    create_form = forms.CreateForm(request.form)
    #print request.method
    if request.method == 'POST' and create_form.validate():
        user = User(username = create_form.username.data,
                    password = create_form.password.data,
                    email = create_form.email.data)
        print user
        db.session.add(user)
        db.session.commit()
        success_message = 'Usuario registrado en la base de datos'
        flash(success_message)

    return render_template('create.html', form = create_form, title=title)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    title = 'Autenticacion'
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        success_message = 'Bienvenido {}'.format(username)
        session['username'] = login_form.username.data
        flash(success_message)
    return render_template('login.html', form = login_form, title=title)

@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username')
    # aqui se ubica la funcion
    return redirect(url_for('login'))

@app.route('/cookie', methods = ['GET', 'POST'])
def cookie():
    title = 'Manejo de Cookies'
    response = make_response(render_template('cookie.html', title=title))
    response.set_cookie('custome_cookie', 'Fernando')
    return response

# Decorador que diga a que ruta debe ir, route recibe un string
@app.route('/', methods = ['GET', 'POST'])
# funcion que retorna un hola mundo, un template
def index():
    # sino encuentra 'custome_cookie' entonces responde Undifined
    custome_cookie = request.cookies.get('custome_cookie', 'Undifined')
    print (custome_cookie)
    title = 'Intro Flask'
    comment_form = forms.CommentForm(request.form)
    if 'username' in session:
        username = session['username']
        print (username)
    if request.method == 'POST' and comment_form.validate():
        print (comment_form.username.data)
        print (comment_form.email.data)
        print (comment_form.comment.data)
    return render_template('index.html', title=title, form = comment_form)


if __name__ == '__main__':
    # Inicie las apliciones con las configiraciones 
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
        
    app.run(port=8000)