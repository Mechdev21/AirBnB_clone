#!/usr/bin/python3

'''
Creating a basemodel
not expecting this to be fun at all
'''

from uuid import uuid4
from datetime import datetime

class BaseModel:

    '''
    Creating a public attribute of Basemodel

    Attributes:
        id: assign with an uuid when an instance is created
        created_at: assign with the current datetime when an instance is created
        updated_at: assign with the current datetime when an instance is created and updated

    '''
    def __init__(self)

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    '''Public instance attributes'''
    def __str__(self):

        '''Output [<class name>] (<self.id>) <self.__dict__>'''
        return ("[{}] ({}) {}". format(self.__class__.__name__, self.id, self.__dict__.))


    """creating the public instances"""
    def save(self):

        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()

    """creating a to_dict(self)"""
    def to_dict(self):

        instance_dict = {}
        intance_dict = update(self.__dict__)
        instance_dict["created_at"] = instance_dict["created_at"].isoformat()
        instance_dict["updated_at"] = instance_dict["updated_at"].isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        return instance_dict
