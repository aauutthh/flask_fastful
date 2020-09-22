# encoding: utf-8
from .cli import cli
import flask_fastful
from flask_fastful.utils.path import mkdir
from flask_fastful.utils.render import rend_file_with_relpath
import click
import logging
import os
from glob import glob
log = logging.getLogger(__name__)


@cli.add_command
@click.command("startproject")
@click.argument("projectname")
@click.argument("dstdir", default=None, required=False)
def startproject(projectname, dstdir):
    log.info("----- start -----")
    srcdir = flask_fastful.__path__[0]
    tpldir = os.path.join(srcdir, "templates", "project_templates")
    if not dstdir:
        if not os.path.exists(projectname):
            mkdir(projectname)
        dstdir = projectname
    dstdir = os.path.abspath(dstdir)
    if os.listdir(dstdir):
        raise Exception("%s dir not empty, choose another projectname"%(dstdir))
    os.chdir(tpldir)
    ctx = {
        "project_name": projectname,
    }

    for f in glob("*.*-tpl"):
        rend_file_with_relpath(f, dstdir, ctx)

    for f in glob("**/*.*-tpl"):
        rend_file_with_relpath(f, dstdir, ctx)

    log.info("----- all done -----")
