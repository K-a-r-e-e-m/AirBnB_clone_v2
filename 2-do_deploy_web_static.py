#!/usr/bin/python3
"""Use fabric function do_pack() to generage a tgz archive"""
from fabric.api import *
import os

# My ip addresses of web server 1 and web server 2
env.hosts = ['100.26.246.92', '54.237.124.240']


def do_deploy(archive_path):
   """
   Deploy archive to web server
   """
   try:
       filename = archive_path.split("/")[-1]
       no_ext = filename.split(".")[0]
       path_no_ext = "/data/web_static/releases/{}/".format(no_ext)
       symlink = "/data/web_static/current"
       put(archive_path, "/tmp/")
       run("mkdir -p {}".format(path_no_ext))
       run("tar -xzf /tmp/{} -C {}".format(filename, path_no_ext))
       run("rm /tmp/{}".format(filename))
       run("mv {}web_static/* {}".format(path_no_ext, path_no_ext))
       run("rm -rf {}web_static".format(path_no_ext))
       run("rm -rf {}".format(symlink))
       run("ln -s {} {}".format(path_no_ext, symlink))
       return True
   except Exception:
       return False

