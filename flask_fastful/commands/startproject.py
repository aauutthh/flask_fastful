# encoding: utf-8
from .cli import cli
import click
import logging
log = logging.getLogger(__name__)

@cli.add_command
@click.command("startproject")
def startproject():
    log.info("hello")

