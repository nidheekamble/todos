from api import app, db
import time
import hashlib
from sqlalchemy import or_, and_
from sqlalchemy.orm import Session
from flask_login import login_user, current_user, logout_user, login_required, UserMixin
from flask import Flask, session, render_template, url_for, flash, redirect, request, send_from_directory
from api.forms import UserForm
from api.models import User
#Sample AJAX REQUEST

@app.route('/api/hello', methods=['POST'])
def hello():
	time.sleep(1)
	return 'Hello'

'''
isme try to add a 
/api/login [POST]
/api/signup [POST]
Add sqlalchemy and sessions to it
'''
'''
@app.route('/api/login', methods=['POST'])
def login():
	form = LoginForm(request.form)

	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		pw = (form.password.data)
		s = 0
		for char in pw:
			a = ord(char) #ASCII
			s = s+a #sum of ASCIIs acts as the salt
		now_hash = (str)((hashlib.sha512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())

		if (user and (user.password==now_hash)):
			login_user(user)
			print("hash correct")
			return 'Log in successful'

		else:
			print('Nahin hua')
			

	return 'Log in not successful'
'''

@app.route('/api/login', methods=['GET', 'POST'])
def login():
	name = request.form['name']
	password = request.form['password']
	user = User.query.filter_by(name=name).first()

	s = 0
	for char in password:
		a = ord(char) #ASCII
		s = s+a #sum of ASCIIs acts as the salt
	now_hash = (str)((hashlib.sha512((str(s).encode('utf-8'))+((password).encode('utf-8')))).hexdigest())

	if (user and (user.password==now_hash)):
		return ('signed in', 200, {'Content-Type': 'application/json'})
	return('not signed in')

'''
@app.route('/api/signup', methods=['POST'])
def signup():
	form = UserForm()
	if form.validate_on_submit():
		
		pw = (form.password.data)
		s = 0
		for char in pw:
			a = ord(char) #ASCII
			s = s+a #sum of ASCIIs acts as the salt
		hashed_password = (str)((hashlib.sha512((str(s).encode('utf-8'))+((form.password.data).encode('utf-8')))).hexdigest())
	
		user = User(name=form.name.data, password = hashed_password, about=form.about.data)
		db.session.add(user)
		db.session.commit()
		return redirect(url_for('login'))

	print('form not validated')
	print(form.errors)
	return 'Not validated'
'''

@app.route('/api/signup', methods=['GET', 'POST'])
def signup():
	form = UserForm()
	pw = form.password.data

	s = 0
	for char in pw:
		a = ord(char) #ASCII
		s = s+a #sum of ASCIIs acts as the salt
	hashed_password = (str)((hashlib.sha512((str(s).encode('utf-8'))+((pw).encode('utf-8')))).hexdigest())

	user = User(name=form.name.data, password = hashed_password, about=form.about.data)
	db.session.add(user)
	db.session.commit()
	print (user)
	if user:
		return ('', 200)
	return ('', 400)