#!/usr/bin/python3

from models.base_model import BaseModel
"""
class review inheriting from BaseModel
"""


class Review(BaseModel):

    """creating public class attribute"""
    def __init__(self, place_id="", user_id="", text=""):

        super().__init__()
        self.place_id = place_id
        self.usser_id = user_id
        self.text = text
