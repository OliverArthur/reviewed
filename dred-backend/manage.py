#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api import create_app, db

app = create_app(os.getenv('DRED_ENV') or 'dev')

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
