#!/usr/bin/python3

""" Creating the user class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines a user class model
    
    Attributes:
        email: empty string
        password: empty string
        first_name: empty string
        last_name: empty string
    """
   
    email = ""
    password = ""
    first_name = ""
    last_name = ""