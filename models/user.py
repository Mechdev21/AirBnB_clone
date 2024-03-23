#!/usr/bin/python3
""" Creating the user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines a user class model"""
    def __init__(self,email = " ", password = " ", first_name = " ", last_name = " ", *args, **kwargs):
        """class user constructor"""
        super().__init__(*args, **kwargs)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
