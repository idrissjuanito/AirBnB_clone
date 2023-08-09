#!/usr/bin/python3
""" A holds storage object for storing objects """
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
