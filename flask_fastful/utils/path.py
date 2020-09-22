# encoding: utf-8
import os

def mkdir(p: str, *args):
    base = os.path.dirname(p)
    if base and not os.path.exists(base):
        mkdir(base, *args)
    if p and not os.path.exists(p):
        os.mkdir(p, *args)


