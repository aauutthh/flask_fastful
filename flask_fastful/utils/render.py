# encoding: utf-8
from flask_fastful.utils.path import mkdir
import logging
import os
from jinja2 import Template
log = logging.getLogger(__name__)

def rend_file_with_relpath(tpl: str, dstdir: str, ctx:dict):
    with open(tpl, 'r') as f:
        t = Template(f.read())
    dstdir = os.path.join(dstdir, os.path.dirname(tpl))
    dstfn = os.path.basename(tpl[:-4]) # trip -tpl
    dstfn = os.path.join(dstdir, dstfn)
    if dstdir and not os.path.exists(dstdir):
        mkdir(dstdir)
    with open(dstfn, "w") as f:
        f.write(t.render(ctx))
        log.info("generate file [%s] done", dstfn)

