from flask_script import Manager, Shell, Server
from __init__ import app


manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell())


@manager.command
def createdb():
    from models import db
    db.create_all()

manager.run()