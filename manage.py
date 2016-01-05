from flask_script import Manager, Shell, Server
from flask import session
from __init__ import app


manager = Manager(app)
manager.add_command("runserver", Server())
manager.add_command("shell", Shell())


@manager.command
def createdb():
    from models import db, User, Tags, CsTags, ElecTags, MusicTags, GamingTags
    db.drop_all()
    db.create_all()

    cstags = [CsTags("Flask"), CsTags("Web Development"), CsTags("Algorithms"), CsTags("Artificial Intelligence"),
              CsTags("Machine Learning"), CsTags("Java")]
    electags = [ElecTags("PCB"), ElecTags("VLSI"), ElecTags("Circuit Design")]
    gamingtags = [GamingTags("Dota 2"), GamingTags("Counter-Strike"), GamingTags("Leage of Legeneds")]
    musictags = [MusicTags("Heavy Metal"), MusicTags("Grunge"), MusicTags("Trash Metal")]
    db.session.add_all(cstags)
    db.session.add_all(electags)
    db.session.add_all(gamingtags)
    db.session.add_all(musictags)
    db.session.commit()

createdb()
manager.run()