#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.app import create_app
from src.config.config import Config
# from src.config.config_test import TestConfig
# from src.config.config_production import ProductionConfig
import logging
import os

logger = logging.getLogger(__name__)

# if os.environ.get("debug_mode", "False") == "True":
#     logger.info("测试环境模式")
#     config = TestConfig
# else:
#     config = ProductionConfig

config = Config

application = create_app(config)

logger.info("started")
