#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static
    folder of your AirBnB Clone repo
"""
#from fabric.api import run
from datetime import datetime


date = datetime.now()
file_name = f'{datetime.now()}'
print(file_name)

def do_pack():
	"""pack all the content of the web_static folder"""
	print(file_name)
	return file_name
