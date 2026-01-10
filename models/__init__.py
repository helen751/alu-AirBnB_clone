#!/usr/bin/python3
"""The __init__ method for models directory"""

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()


dict_classes = {"BaseModel": BaseModel}