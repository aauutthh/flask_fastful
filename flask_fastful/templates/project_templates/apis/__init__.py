# encoding: utf-8
__all__ = ["api"]
from .api import api
from flask_fastful.utils.importers import GlobImport
GlobImport("api*.py")
