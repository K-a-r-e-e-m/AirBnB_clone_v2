#!/usr/bin/python3
"""Use fabric function do_pack() to generate a tgz archive"""
from fabric.api import env, put, run
import os

# My IP addresses of web server 1 and web server 2
env.hosts = ['100.26.246.92', '54.237.124.240']


def do_deploy(archive_path):
    '''distributes an archive to my web servers'''
    if not os.path.exists(archive_path):
        return False
    
    try:
        # archive_path = versions/web_static_20170315003959.tgz
        
        # filename_tgz = web_static_20170315003959.tgz
        filename_tgz = archive_path.split('/')[-1]
        
        # archive = /tmp/web_static_20170315003959.tgz
        archive = f'/tmp/{filename_tgz}'
        
        # filename = web_static_20170315003959
        filename = filename_tgz.split(".")[0]
        without_tgz = f'/data/web_static/releases/{filename}'
        
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')
        
        # Create the release directory
        run(f'mkdir -p {without_tgz}/')
        
        # Uncompress the archive
        run(f'tar -xzf {archive} -C {without_tgz}/')
        
        # Delete the archive from the web server
        run(f'rm {archive}')
        
        # Move contents out of the web_static directory
        run(f'mv {without_tgz}/web_static/* {without_tgz}/')
        run(f'rm -rf {without_tgz}/web_static')
        
        # Delete the symbolic link /data/web_static/current from the web server
        run(f'rm -rf /data/web_static/current')
        
        # Create a new symbolic link /data/web_static/current on the web server
        run(f'ln -s {without_tgz}/ /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception as e:
        print(f"Error during deployment: {e}")
        return False
