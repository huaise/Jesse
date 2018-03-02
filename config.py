import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	DEBUG = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'tKsrcPgweEis1zkf'
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

	@staticmethod
	def init_app(app):
		pass

