import os
from app import new_app,db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = new_app()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
