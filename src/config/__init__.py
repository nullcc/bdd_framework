# -*- coding: utf-8 -*-

import os
import pytz
from src.config.config import Config
# from src.config.config_test import TestConfig
# from src.config.config_production import ProductionConfig

# if os.environ.get("debug_mode", None) == "True":
#     config = TestConfig
# elif os.environ.get("production_mode", None) == "True":
#     config = ProductionConfig
# else:
#     config = DevConfig

config = Config

tz = pytz.timezone(config.TIME_ZONE)
