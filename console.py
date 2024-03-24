#!/usr/bin/python3

"""Begining of the console"""

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is a custom console class
    """
    prompt = "(hbnb)"

    def do_create(self, line):

        """Creates a new instance of a model"""
        classes = {"BaseModel": BaseModel, "User": User}
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        if len(args) == 1 and args[0] not in classes:
            print("** class doesn't exist **")
        try:
            class_name = classes[args[0]]
            obj = class_name()
            print(obj.id)
        except Exception as e:
            print(f"Error creating object: {str(e)}")

    def do_quit(self, line):
        """EXIT the cmdloop"""
        return True

    def do_EOF(self, line):
        """exit upn keyboard interrupt"""
        return True

    def emptyline(self):
        """does nothing upon encontering a blank line"""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
