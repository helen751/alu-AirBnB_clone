#!/usr/bin/python3
"""This is the BaseModel for all of the classes"""

import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
      """Method of constructor for the class"""
      if kwargs:
         for key, value in kwargs.items():
            if key == "__class__":
               continue
            if key == "created_at" or key == "updated_at":
               value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            setatrr(self, key, value)
      else:
          self.id = str(uuid.uuid4())
          self.created_at = datetime.now()
          self.updated_at = datetime.now()
          models.storage.new(self)

    def __str__(self):
        """String representation"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
       """Updates the updated_at attribute with the current"""
       self.updated_at = datetime.now()
       models.storage.save()

    def to_dict(self):
       """Dictionary containing keys or values of __dict__ 
       of the instance"""
       obj_dict = self.__dict__.copy
       obj_dict['__class__'] = self.__class__.__name__
       obj_dict['created_at'] = self.created_at.isoformat()
       obj_dict['updated_at'] = self.updated_at.isoformat()
       return obj_dict
