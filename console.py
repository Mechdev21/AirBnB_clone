#!/usr/bin/python3
"""Begining of the console"""

import cmd
import os
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This is a custom console class
    """
    prompt = "(hbnb)"

    def do_create(self, line):

        """Creates a new instance of a model"""
        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1 and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            try:
                if not os.path.exists("file.json"):
                    with open("file.json", "w") as f:
                        json.dump({}, f)
                class_name = classes[args[0]]
                obj = class_name()
                obj.save()
                print(obj.id)
            except Exception as e:
                print(f"Error creating object: {str(e)}")

    def do_show(self, line):
        """Show details of a specific instance"""
        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        args = shlex.split(line)
        instant = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1 and args[0] in classes:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in instant:
                print("** no instance found **")
            else:
                print(instant[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        args = shlex.split(line)
        instant = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1 and args[0] in classes:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in instant:
                print("** no instance found **")
            else:
                del instant[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based"""
        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        args = shlex.split(line)
        instant = storage.all()
        if len(args) == 0:
            print([str(i) for i in instant.values()])
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            if len(args) == 1:
                instances = [str(v) for v in instant.values()
                             if v.__class__.__name__ == args[0]]
            print(instances)

    def do_update(self, line):
        """Updates the class provided with thehelp of the id"""
        classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity, "Place": Place,
                   "Review": Review}
        args = shlex.split(line)

        if len(args) == 0:
            print("** class name missing **")
        elif len(args) < 2 and args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) < 2 and args[0] in classes:
            print("** instance id missing **")
        else:
            key = f"{classes[args[0]].__name__}.{args[1]}"
            dic = storage.all()
            if key not in dic:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                attr_k = args[2]
                attr_v = args[3]
                instant = dic[key]
                setattr(instant, attr_k, attr_v)
                storage.save()


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
