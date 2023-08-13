#!/usr/bin/python3
""" Module for a custom python console """
import cmd
import models as mddl
import utils as utl


class HBNBCommand(cmd.Cmd):
    """
        Command interpreter class for running commands at a prompt
        Attributes:
            Prompt (str): a default prompt phrase
    """
    prompt = "(hbnb)"

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_create(self, arg):
        'Creates a new instance of the BaseModel class'
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg != "BaseModel":
            print("** class doesn't exist **")
            return
        new_base = mddl.base_model.BaseModel()
        mddl.storage.save()
        print(new_base.id)

    def do_show(self, arg):
        'prints string representation of instance based on class name and id'
        args = utl.validate_args(arg)
        if args:
            print(mddl.storage.all().get(args[0]+"."+args[1]))

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        args = utl.validate_args(arg)
        if args:
            store_objects = mddl.storage.all()
            del store_objects[args[0]+"."+args[1]]
            mddl.storage.save()

    def do_all(self, arg):
        'Prints all string representation of all instances based on class name'
        str_reprs = list()
        if len(arg) == 0:
            for key, val in mddl.storage.all().items():
                str_reprs.append(val.__str__())
        else:
            if not utils.check_cls_exists(arg):
                return
            for key, val in mddl.storage.all().items():
                if key.split(".")[0] == arg:
                    str_reprs.append(val.__str__())
        print(str_reprs)

    def do_update(self, arg):
        'Updates an instance based on class name and id'
        args = utl.validate_update_args(arg)
        if not args:
            return
        obj = mddl.storage.all().get(args[0]+"."+args[1])
        obj.__setattr__(args[2], utl.cast_to_type(args[3]))
        mddl.storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
