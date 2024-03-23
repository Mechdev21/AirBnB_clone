#!/usr/bin/python3
"""Begining of the console"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """ custom console class"""
    prompt = "(hbnb)"

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
