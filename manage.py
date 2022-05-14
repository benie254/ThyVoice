from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand


# create app instance
app = create_app('production')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)