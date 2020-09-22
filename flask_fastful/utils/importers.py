# encoding: utf-8
from glob import glob
import importlib
import logging
log = logging.getLogger(__name__)

def GlobImport(pattern: str):
    imports = [ py[:-3].replace('/','.') for py in glob(pattern)]
    log.debug("imports: %s", imports)
    for m in imports:
        importlib.import_module(m)
