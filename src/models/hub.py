# -*- coding: utf-8 -*-

import datetime
from src.extensions import db
from sqlalchemy import Column, Integer, DateTime
from src.models.base import BaseModel


class Hub(BaseModel):
    """
    Appium hub
    """

    __tablename__ = "hubs"

    id = db.Column(db.Integer, primary_key=True)      # pk
    name = db.Column(db.String(100), nullable=False)  # hub name
    url = db.Column(db.String(100), nullable=False)   # hub url
    port = db.Column(db.Integer, nullable=False)      # hub port
    path = db.Column(db.String(100), nullable=False)  # hub path
    status = db.Column(db.Integer, nullable=False)    # hub status 0: available, 1: unavailable
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
    updated_time = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, url, port, path, *args, **kwargs):
        self.name = name
        self.url = url
        self.port = port
        self.path = path
        self.status = 1
        self.created_time = datetime.datetime.now()
        self.updated_time = datetime.datetime.now()
        if kwargs and kwargs['id']:
            self.id = kwargs['id']

    @staticmethod
    def all_hubs():
        """
        Get all hubs.
        :return:
        """
        return Hub.query.order_by(Hub.id.desc()).all()
