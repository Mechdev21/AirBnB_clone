#!/usr/bin/python3

from models.base_model import BaseModel
"""
This class inherit from BaseModel
"""


class State(BaseModel):
    """Creating a public attribute"""
    def __init__(self, name=""):

        """calling the parent class"""

        super().__init__()
        self.name = name
