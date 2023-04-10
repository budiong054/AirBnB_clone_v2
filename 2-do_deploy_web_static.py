#!/usr/bin/python3
"""Distributes an archive to your web servers"""
from fabric.api import put, run, env
from os import path


env.hosts = ['18.233.67.42', '54.237.66.155']


def do_deploy(archive_path):
    """This scripts distributes an archive to your webservers
    """
    if not path.exists(archive_path):
        return False
    archive_file = archive_path.split('/')[-1]
    archive = archive_file.split('.')[0]

    try:
        put(f"{archive_path}", f"/tmp/{archive_file}")
        run(f"mkdir -p /data/web_static/releases/{archive}")
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
            archive_file, archive))
        run(f"rm /tmp/{archive_file}")
        run(f"cp -r /data/web_static/releases/{archive}/web_static/* "
            f"/data/web_static/releases/{archive}")
        run(f"rm -rf /data/web_static/releases/{archive}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{archive}/ "
            "/data/web_static/current")
    except Exception:
        return False
    else:
        print("New version deployed!")
        return True
