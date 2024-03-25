#!/usr/bin/python3

"""This class inherit from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Creating a public attribute
    Attribute:
        name: an empty string
    """
    name = ""