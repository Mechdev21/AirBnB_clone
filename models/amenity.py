#!/usr/bin/python3

from models.base_model import BaseModel

"""
Creating a class that inherit from Base
Model
"""


class Amenity(BaseModel):
    """Public class attribute"""
    def __init__(self, name="", *args, **kwargs):

        """calling BaseModel"""
        super().__init__(*args, *kwargs)
        self.name = name
