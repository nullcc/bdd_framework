# -*- coding: utf-8 -*-

import sys
sys.path.append('.')
from src.models.hub import Hub
from src.app import create_app
from src.config.config import Config
from flask.globals import _app_ctx_stack

test_hub1 = Hub("测试hub1", "http://10.32.60.67", 4723, "/wd/hub", id=1)
test_hub2 = Hub("测试hub3", "http://10.32.60.67", 4724, "/wd/hub", id=2)
test_hub3 = Hub("测试hub3", "http://10.32.60.67", 4725, "/wd/hub", id=3)
test_hub4 = Hub("测试hub4", "http://10.32.60.67", 4726, "/wd/hub", id=4)

if not _app_ctx_stack.top:
    app = create_app(Config)
    ctx = app.app_context()
    ctx.push()

    test_hub1.save()
    test_hub2.save()
    test_hub3.save()
    test_hub4.save()

    _app_ctx_stack.pop()
