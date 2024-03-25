#!/usr/bin/python3

"""This modue imports from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Public class attributes
    Attributes:
        state_id: it would be the state.id
        name: an empty string
    """
    state_id = ""
    name = ""