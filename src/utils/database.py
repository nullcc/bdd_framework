# -*- coding: utf-8 -*-

import pytz
from src.extensions import db
from src.database import db_session
from src.utils.signals import model_saved
from flask import current_app as app


class CRUDMixin(object):
    def __repr__(self):
        return "<{}>".format(self.__class__.__name__)

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        return instance.save()

    def save(self):
        """
        保存对象到数据库
        :return:
        """
        try:
            db_session.add(self)
            db_session.commit()
        except:
            db_session.rollback()
            raise
        finally:
            db_session.close()

        model_saved.send(app._get_current_object())
        return self

    def delete(self):
        """
        从数据库中删除对象
        :return:
        """
        try:
            db_session.delete(self)
            db_session.commit()
        except:
            db_session.rollback()
            raise
        finally:
            db_session.close()
        return self


class UTCDateTime(db.TypeDecorator):
    impl = db.DateTime

    def process_bind_param(self, value, dialect):
        """Way into the database."""
        if value is not None:
            # store naive datetime for sqlite and mysql
            if dialect.name in ("sqlite", "mysql"):
                return value.replace(tzinfo=None)

            return value.astimezone(pytz.UTC)

    def process_result_value(self, value, dialect):
        """Way out of the database."""
        # convert naive datetime to non naive datetime
        if dialect.name in ("sqlite", "mysql") and value is not None:
            return value.replace(tzinfo=pytz.UTC)

        # other dialects are already non-naive
        return value
