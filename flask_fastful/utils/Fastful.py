# encoding: utf-8
import yaml
from logging.config import dictConfig

def init_log():
    with open("conf/log.config.yaml", "r") as f:
        logconfig = yaml.safe_load(f)
        dictConfig(logconfig)

def init():
    init_log()

def init_app(app):
    with open("conf/flask.config.yaml", "r") as f:
        flaskconfig = yaml.safe_load(f)
        app.config.update(flaskconfig)
