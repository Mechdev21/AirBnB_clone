#!/usr/bin/python3

from models.base_models.py import BaseModel
"""
This modue imports from BaseModel
"""


class City(BaseModel):
    """Public class attributes"""
    def __init__(self, state_id="", name=""):

        """Calling BaseModel"""
        super().__init__()
        self.state_id = state_id
        self.name = name
