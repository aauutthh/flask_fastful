# encoding: utf-8
from glob import glob
import importlib

def GlobImport(pattern: str):
    imports = [ py[:-3].replace('/','.') for py in glob(pattern)]
    for m in imports:
        importlib.import_module(m)
