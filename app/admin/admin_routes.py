from flask import render_template
from . import admin



@admin.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('admin/index.html')
