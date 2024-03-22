#!/usr/bin/python3

'''
Creating a basemodel
not expecting this to be fun at all
'''

import uuid
from datetime import datetime
import models


class BaseModel:

    '''
    Creating a public attribute of Basemodel

    Attributes:
        id: assign with an uuid when an instance is created
        created_at: assign with the current datetime when an
        instance is created
        updated_at: assign with the current datetime when an
        instance is created and updated
    Args:
        *args: Gets's a number of undisclosed arguments
        **kwargs: passes variable-length argument
        dictionary to a function
    '''

    def __init__(self, *args, **kwargs):
        """Create BaseModel from dictionary"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    '''Public instance attributes'''
    def __str__(self):

        '''Output [<class name>] (<self.id>) <self.__dict__>'''
        return ("[{}] ({}) {}". format(
            self.__class__.__name__, self.id, self.__dict__))

    """creating the public instances"""
    def save(self):

        """updates the public instance attribute updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    """creating a to_dict(self)"""
    def to_dict(self):

        """
        Returns a dictionary conatining all keys/values
        of dict instance
        """

        instance_dict = {}
        instance_dict.update(self.__dict__)
        instance_dict["created_at"] = instance_dict[
            "created_at"].isoformat()
        instance_dict["updated_at"] = instance_dict[
            "updated_at"].isoformat()
        instance_dict["__class__"] = self.__class__.__name__
        return instance_dict
