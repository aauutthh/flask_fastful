# encoding: utf-8
#!/bin/env python
import logging
log = logging.getLogger(__name__)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    from flask_fastful.commands import cli
    cli()


