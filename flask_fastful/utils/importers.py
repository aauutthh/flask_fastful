# encoding: utf-8
import os
from glob import glob
import importlib
import logging
log = logging.getLogger(__name__)

def GlobImport(pattern: str):
    imports = [ py[:-3].replace(os.sep,'.') for py in glob(pattern)]
    log.debug("imports: %s", imports)
    for m in imports:
        importlib.import_module(m)
