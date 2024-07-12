#!/usr/bin/python3
"""Use fabric function do_pack() to generage a tgz archive"""
from fabric.api import *
import os

# My ip addresses of web server 1 and web server 2
env.hosts = ['100.26.246.92', '54.237.124.240']


def do_deploy(archive_path):
    '''distributes an archive to my web servers'''
    if not os.path.exists(archive_path):
        return False

    # archive_path = versions/web_static_20170315003959.tgz

    # filename_tgz = web_static_20170315003959.tgz
    filename_tgz = archive_path.split('/')[-1]

    # archive = /tmp/web_static_20170315003959.tgz
    archive = f'/tmp/{filename_tgz}'

    # filename = web_static_20170315003959
    filename = filename_tgz.split(".")[0]
    without_tgz = f'/data/web_static/releases/{filename}'
    try:
        put(archive_path, '/tmp/')
        run(f'mkdir -p {without_tgz}/')
        run(f'tar -xzf {archive} -C {without_tgz}/')
        run(f'rm {archive}')
        run(f'mv {without_tgz}/web_static/* {without_tgz}')
        run(f'rm -rf {without_tgz}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s {without_tgz}/ /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception:
        return False
