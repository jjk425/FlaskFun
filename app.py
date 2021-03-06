from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
from sqlalchemy.orm import sessionmaker
from tabledef import *
engine = create_engine('sqlite:///tutorial.db', echo=True)

app = Flask(__name__)

@app.route("/")
def home():
	if not session.get("logged_in"):
		return render_template('login.html')
	else:
		return render_template('home.html')#'''<p>Who did it?<form method='get' action='/logout'><button type="submit">Log out</button></form> </p>'''

@app.route('/login', methods=['POST'])
def do_admin_login():

	POST_USERNAME = str(request.form['username'])
	POST_PASSWORD = str(request.form['password'])

	Session = sessionmaker(bind=engine)
	s = Session()
	query = s.query(User).filter(User.username.in_([POST_USERNAME]), User.password.in_([POST_PASSWORD]) )
	result = query.first()

	if result:
		session['logged_in'] = True
		session['username'] = POST_USERNAME
	else:
		flash('Wrong password!')
	return home()

@app.route('/logout')
def logout():
	session['logged_in'] = False
	return home()

@app.route('/didit')
def didit():
	if not session.get("logged_in"):
		return "How are you seeing this?!"
	user = session['username']
	notes = str(request.form['notes'])
	event = Event(user, notes)
	s.add(event)
	return home()


if __name__ == "__main__":
	app.secret_key = os.urandom(12)
	app.run(host='0.0.0.0', port=4000)

