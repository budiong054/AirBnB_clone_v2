#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo
"""
from fabric.api import local
from datetime import datetime
from os import mkdir


date = datetime.now()
tgz_file = f"web_static_{date.year}{date.month}{date.day}{date.hour}"\
    f"{date.minute}{date.second}.tgz"


def do_pack():
    """pack all the content of the web_static folder to a tgz file
    """
    try:
        mkdir("versions")
    except FileExistsError:
        pass
    
    # Packing web_static to versions/{tgz_file}
    pack = local(f"tar -cvzf versions/{tgz_file} web_static")

    if pack.succeeded:
        return f"versions/{tgz_file}"
    return None
