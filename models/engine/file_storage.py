#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes instances to JSON file and deserializes back"""

    __file_path = "file.json"
    __objects = {}

    classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                f
            )

    def reload(self):
        """Deserializes JSON to objects"""
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value["__class__"]
                    self.__objects[key] = self.classes[class_name](**value)
        except FileNotFoundError:
            pass
