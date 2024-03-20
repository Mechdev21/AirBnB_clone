#!/usr/bin/python3

'''
Creating a basemodel
not expecting this to be fun at all
'''

from uuid import uuid4
from datetime import datetime

class BaseModel:


    '''Creating a public attribute of Basemodel'''
    def __init__(self, *args, **kargs)

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
