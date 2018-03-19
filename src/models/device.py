# -*- coding: utf-8 -*-

import datetime
from src.extensions import db
from sqlalchemy import Column, Integer, DateTime
from src.models.base import BaseModel

class Device(BaseModel):
    """
    Devices
    """

    __tablename__ = "devices"

    id = db.Column(db.Integer, primary_key=True)                              # pk
    hub_id = db.Column(db.Integer, db.ForeignKey("hubs.id"), nullable=False)  # fk: hub_id
    name = db.Column(db.String(100), nullable=False)                          # device name
    device_type = db.Column(db.Integer, nullable=False)                       # device type 0: simulator, 1: real device
    platform = db.Column(db.String(100), nullable=False)                      # platform: iOS/Android
    model = db.Column(db.String(100), nullable=False)                         # device model
    platform_version = db.Column(db.String(100), nullable=False)              # platform version
    api_level = db.Column(db.String(100), nullable=False)                     # api level (only for Android)
    status = db.Column(db.Integer, nullable=False)                            # device status 0: available, 1: unavailable
    created_time = Column(DateTime, default=datetime.datetime.utcnow)
    updated_time = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, hub_id, name, device_type, platform, model, platform_version, api_level, *args, **kwargs):
        self.hub_id = hub_id
        self.name = name
        self.device_type = device_type
        self.platform = platform
        self.model = model
        self.platform_version = platform_version
        self.api_level = api_level
        self.status = 0
        self.created_time = datetime.datetime.now()
        self.updated_time = datetime.datetime.now()
        if kwargs and kwargs['id']:
            self.id = kwargs['id']

    @staticmethod
    def all_devices():
        """
        Get all devices.
        :return:
        """
        return Device.query.order_by(Device.id.desc()).all()
