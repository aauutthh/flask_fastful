# encoding: utf-8
from .api import api
from flask_restful import Resource, current_app
import logging
log = logging.getLogger(__name__)

@api.resource("/demo")
class Demo(Resource):
    def get(self):
        log.info("%s", dir(current_app))
        current_app.logger.info("%s", current_app.config)
        return {"demo": "hi! %s"%(current_app.config.get("name"))}

