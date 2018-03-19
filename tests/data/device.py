# -*- coding: utf-8 -*-

import sys
sys.path.append('.')
from src.models.device import Device
from src.app import create_app
from src.config.config import Config
from flask.globals import _app_ctx_stack

test_device1 = Device(1, "Nexus 5X API 24", 0, "Android", "Nexus 5X", "7.0", "24", id=1)
test_device2 = Device(2, "Nexus 5X API 25", 0, "Android", "Nexus 5X", "7.1.1", "25", id=2)
test_device3 = Device(3, "Nexus 5X API 26", 0, "Android", "Nexus 5X", "8.0", "26", id=3)
test_device4 = Device(4, "Nexus 5X API P", 0, "Android", "Nexus 5X", "P", "P", id=4)

if not _app_ctx_stack.top:
    app = create_app(Config)
    ctx = app.app_context()
    ctx.push()

    test_device1.save()
    test_device2.save()
    test_device3.save()
    test_device4.save()

    _app_ctx_stack.pop()
