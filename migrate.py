#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from src.extensions import db
from src.app import create_app
from src.config.config import Config
from src.models import *

app = create_app(Config)
db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
