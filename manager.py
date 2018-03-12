#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.app import create_app
from src.config.config import Config

app = create_app(Config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.PORT, debug=True)
