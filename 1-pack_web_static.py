#!/usr/bin/env python3
"""Use fabric function do_pack() to generage a tgz archive"""
from fabric.api import local
import time


def do_pack():
    '''generates a .tgz archive from contents of the web_static'''
    # First create versions directpry if doesn't exist
    local("mkdir -p versions")
    name = 'versions/web_static_' + time.strftime('%Y%m%d%H%M%S') + '.tgz'
    try:
        tgz_file = local(f"tar -cvzf {name} web_static")
        return tgz_file
    except Exception:
        return None
