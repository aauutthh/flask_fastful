# encoding: utf-8
import yaml
from logging.config import dictConfig

class Fastful():
    @staticmethod
    def init_log():
        with open("conf/log.config.yaml", "r") as f:
            logconfig = yaml.safe_load(f)
            dictConfig(logconfig)

    @staticmethod
    def init():
        Fastful.init_log()

    @staticmethod
    def init_app(app):
        with open("conf/flask.config.yaml", "r") as f:
            flaskconfig = yaml.safe_load(f)
            app.config.update(flaskconfig)


from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base

def ModelBaseBuilder(prefix=""):
    _Base = declarative_base()

    class Base(_Base):
        __abstract__ = True
        _the_prefix = prefix
        __display_exclude__ = []

        def __init__(self, *args):
            cols = list(self.__table__.columns)
            l = min(len(cols)-1, len(args))
            for i, col in enumerate(cols[1:l+1]):
                setattr(self, col.name, args[i])


        @declared_attr
        def __tablename__(cls):
            return cls._the_prefix + cls.__name__.lower()

        def _filter(self, k, v, filterNone=False):
            return k.startswith("_sa_") or \
                k in self.__display_exclude__ or\
               ( filterNone and v is None)

        def _asDict(self, filterNone=False):
            return { k:v
                for k,v in self.__dict__.items()
                if not self._filter(k,v, filterNone)
                }

    return Base


import flask
from celery import Celery

class FlaskCelery(Celery):
    """
    app = Flask()
    capp = FlaskCelery()
    capp.init_app(app)
    """

    def __init__(self, *args, **kwargs):

        super(FlaskCelery, self).__init__(*args, **kwargs)
        self.patch_task()

        if 'app' in kwargs:
            self.init_app(kwargs['app'])

    def patch_task(self):
        TaskBase = self.Task
        _celery = self

        class ContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                if flask.has_app_context():
                    return TaskBase.__call__(self, *args, **kwargs)
                else:
                    with _celery.app.app_context():
                        return TaskBase.__call__(self, *args, **kwargs)

        self.Task = ContextTask

    def init_app(self, app):
        self.app = app
        if not "CELERY_CONFIG" in app.config:
            raise Exception("CELERY_CONFIG not find in flask config")
        self.config_from_object(app.config.get('CELERY_CONFIG'))

