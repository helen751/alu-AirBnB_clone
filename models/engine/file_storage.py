#!/usr/bin/python3
"""FileStorage engine"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """Serializes instances to a JSON file and deserializes them"""

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
        """Sets obj in __objects"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        dict_to_save = {}
        for key, obj in FileStorage.__objects.items():
            dict_to_save[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(
                {k: v.to_dict() for k, v in FileStorage.__objects.items()},
                f
            )

    def reload(self):
        """Deserializes JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
        }
        try:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value["__class__"]
                    cls = classes.get(class_name)
                    if cls:
                        # FileStorage.__objects[key] = cls(**value)
                        self.new(cls(**value))
        except FileNotFoundError:
            pass
