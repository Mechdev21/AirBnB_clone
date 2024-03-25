#!/usr/bin/python3
"""A file storage claass that helps with serialization
and deserialization"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """that serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns a dictionary of all objects"""
        return self.__objects

    def new(self, obj):
        """adds a new objects to the dictionary"""
        if obj not in self.__objects:
            key = ("{}.{}".format(obj.__class__.__name__, obj.id))
            self.__objects[key] = obj

    def save(self):
        """serializes an object into a json file"""
        dict_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w', encoding= 'utf-8') as f:
            json.dump(dict_dict, f)

    def reload(self):
        """Deserialize a JSON file and convert it into instances"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    instance_dict = json.load(f)

                for data in instance_dict.values():
                    class_key = data.get('__class__')
                    if class_key:
                        class_name = globals().get(class_key)
                        if class_name:
                            obj = class_name(**data)
                            self.new(obj)
            except Exception:
                pass

