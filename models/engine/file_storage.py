#!/usr/bin/python3
"""A file storage claass that helps with serialization
and deserialization"""

import json
from models.base_model import BaseModel


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
        """desrialise a json file and converts it into an instance"""
        try:
            with open(self.__file_path, 'r') as f:
                instance_dict = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print("File not found {}".format(e))
            return
        for data in instance_dict.values():
            class_key = data.get('__class__')
            if class_key:
                class_name = globals()[class_key]
                if class_name:
                    self.new(class_name(**data))
