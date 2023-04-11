#!/usr/bin/python3
"""
Distributes an archive to your web servers
"""

from datetime import datetime
from fabric.api import put, run, env, local
import os


env.hosts = ['18.233.67.42', '54.237.66.155']


def do_pack():
    """pack all the content of the web_static folder to a tgz file
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    d_time = datetime.now()
    archive_path = "versions/web_static_{}{:02d}{:02d}{}{}{}.tgz".format(
        d_time.year,
        d_time.month,
        d_time.day,
        d_time.hour,
        d_time.minute,
        d_time.second
    )
    try:
        print("Packing web_static to {}".format(archive_path))
        local("tar -cvzf {} web_static".format(archive_path))
        size = os.stat(archive_path).st_size
        print("web_static packed: {} -> {} Bytes".format(archive_path, size))
    except Exception:
        archive_path = None
    return archive_path


def do_deploy(archive_path):
    """
        This scripts distributes an archive to your webservers
    """
    if not os.path.exists(archive_path):
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
        pass
    else:
        print("New version deployed!")
        return True
