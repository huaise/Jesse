from flask import render_template, url_for
from . import main

@main.route('/', methods = ['GET'])
def index():
	return render_template('main/index.html')

@main.route('/home', methods = ['GET'])	
def home():

	
	return render_template('main/home.html')