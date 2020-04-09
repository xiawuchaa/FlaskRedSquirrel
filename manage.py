import os
from flask import render_template
from flask_migrate import MigrateCommand
from flask_script import Manager
from Apps import create_app

env = os.environ.get('FLASK_ENV')
app = create_app(env)
manage = Manager(app)
manage.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manage.run()
    # app.run()
