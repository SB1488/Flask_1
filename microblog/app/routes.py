# -*- coding: utf-8 -*-
from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
 user = {'username': 'name '}
 posts = [
 {
 'author': {'username': 'John'},
 'body': 'I want to die!!'
 },
 {
 'author': {'username': 'Susan'},
 'body': 'We had school shooting today!'
 },
 {
 'author': {'username': 'Иван'},
 'body':'Бродягам привет, остальным соболезную.'
 }
 ]
 return render_template('index.html', title='Home', user=user, posts=posts)

