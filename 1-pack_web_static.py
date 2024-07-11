#!/usr/bin/python3
"""Use fabric function do_pack() to generage a tgz archive"""
from fabric.api import local
import time


def do_pack():
    '''generates a .tgz archive from contents of the web_static'''
    # First create versions directpry if doesn't exist
    local("mkdir -p versions")
    name = 'versions/web_static_' + time.strftime('%Y%m%d%H%M%S') + '.tgz'
    result = local(f"tar -cvzf {name} web_static")
    if result.succeeded:
        return name
    else:
        return None
