#!/usr/bin/python3

"""HBNBCommand Class inherits from the cmd.Cmd class,
which provide simple framework for writing line-orinted
command interpreters"""


import cmd
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """attribute is set to ('hbnb') whiich id the prompt
    user will see when they run the console"""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit or exit the program"""
        return True

    def emptyline(self):
        """an empty line + ENTER should not execute anything"""
        pass

    def do_create(self, args):
        """method that Create New Instance Of
        BaseModel or user , to save it(to the JSON file), and print the id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            new_inst = eval(args[0])()
            for param in args[1:]:
                key, val = param.split('=')
                if val.startswith('"'):
                    val = val[1:-1].replace('\\"', '"').replace("_", " ")
                elif '.' in val:
                    val = float(val)
                else:
                    val = int(val)
                setattr(new_inst, key, val)
            new_inst.save()
            print(new_inst.id)

    def do_show(self, args):
        """method Prints the string representation of an instance
        based on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, args):
        """method Deletes an instance based
        on the class name and id"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, args):
        """method Prints all string representation of all instances
        based or not on the class name"""
        args = args.split()
        if len(args) > 0 and args[0] not in ["BaseModel", "User", "Place",
                                             "State", "City", "Amenity",
                                             "Review"]:
            print("** class doesn't exist **")
        else:
            for key, val in models.storage.all().items():
                if len(args) == 0 or args[0] == key.split(".")[0]:
                    print(str(val))

    def do_update(self, args):
        """Updates an instance based on the class name and id by
        adding or updating attribute"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in ["BaseModel", "User", "Place", "State", "City",
                             "Amenity", "Review"]:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0] + "." + args[1] not in models.storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if args[2] not in ["id", "created_at", "updated_at"]:
                setattr(models.storage.all()[key], args[2], args[3])
                models.storage.all()[key].save()

    def do_EOF(self, args):
        """Exit of the program"""
        return True

    def do_count(self, arg):
        """Counts the number of instances of a class"""
        args = arg.split(".")
        if len(args) > 1 and args[1] == "count()":
            count = 0
            for key in models.storage.all():
                if key.split(".")[0] == args[0]:
                    count += 1
            print(count)

    def default(self, arg):
        """Show Spcified Instance By Using Class Name"""
        args = arg.split(".")
        if len(args) > 1:
            if args[1] == "all()":
                self.do_all(args[0])
            elif args[1] == "count()":
                self.do_count(arg)
            elif args[1].startswith("show(") and args[1].endswith(")"):
                id = args[1][6:-2]
                self.do_show(args[0] + " " + id)
            elif args[1].startswith("destroy(") and args[1].endswith(")"):
                id = args[1][9:-2]
                self.do_destroy(args[0] + " " + id)
            elif args[1].startswith("update(") and args[1].endswith(")"):
                update_args = args[1][7:-1].replace("\"", "").split(", ")
                if len(update_args) < 3:
                    print("** attribute name or value missing **")
                else:
                    self.do_update(args[0] + " " + update_args[0] +
                                   " " + update_args[1] + " " + update_args[2])
        else:
            print("** command doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
