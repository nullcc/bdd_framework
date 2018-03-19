# -*- coding: utf-8 -*-

# 清除数据库数据

import sys
sys.path.append('.')
from src.app import create_app
from src.database import db_session
from src.config.config import Config

from src.models.hub import Hub
from src.models.device import Device

app = create_app(Config)
ctx = app.app_context()
ctx.push()

Device.query.delete()
Hub.query.delete()

db_session.commit()

print '数据清理完毕!'
