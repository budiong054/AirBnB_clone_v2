#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime
import os


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
