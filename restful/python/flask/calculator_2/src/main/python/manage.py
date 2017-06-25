from flask.ext.script import Manager, Server

from calculator import create_app


app = create_app()

manager = Manager(app)
manager.add_command('server', Server())

if __name__ == '__main__':
    manager.run()
