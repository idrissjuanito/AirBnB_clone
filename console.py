#!/usr/bin/python3
""" Module for a custom python console """
import cmd
import models as mddl
import utils as utl
classes = mddl.engine.file_storage.classes


class HBNBCommand(cmd.Cmd):
    """
        Command interpreter class for running commands at a prompt
        Attributes:
            Prompt (str): a default prompt phrase
    """
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        'EOF command to exit the program\n'
        return True

    def do_quit(self, arg):
        'Quit command to exit the program\n'
        return True

    def emptyline(self):
        """ handles empty line on prompt """
        pass

    def do_create(self, arg):
        'Creates a new instance of the BaseModel class'
        if len(arg) == 0:
            print("** class name missing **")
            return
        if not utl.check_cls_exists(arg):
            print("** class doesn't exist **")
            return
        cls = classes[arg]
        new_cls = cls()
        mddl.storage.save()
        print(new_cls.id)

    def do_show(self, arg):
        'prints string representation of instance based on class name and id'
        args = utl.validate_args(arg)
        if args:
            key = args[0] + "." + args[1]
            obj = mddl.storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id'
        args = utl.validate_args(arg)
        if args:
            key = args[0] + "." + args[1]
            obj = mddl.storage.all().get(key)
            if obj is None:
                print("** no instance found **")
            else:
                del mddl.storage.all()[key]
                mddl.storage.save()

    def do_all(self, arg):
        'Prints all string representation of all instances based on class name'
        str_reprs = []
        if len(arg) == 0:
            print([str(val) for val in mddl.storage.all().values()])
        else:
            if not utl.check_cls_exists(arg):
                return
            print([str(val) for key, val in mddl.storage.all().items() if key.split(".")[0] == arg])

    def do_update(self, arg):
        'Updates an instance based on class name and id'
        args = utl.validate_update_args(arg)
        if not args:
            return
        key = args[0] + "." + args[1]
        obj = mddl.storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        if len(args) < 4:
            print("** attribute name missing **")
            return
        setattr(obj, args[2], utl.cast_to_type(args[3]))
        mddl.storage.save()

    def do_count(self, arg):
        'Counts the number of instances of a class'
        if not utl.check_cls_exists(arg):
            return
        count = len([val for key, val in mddl.storage.all().items() if key.split(".")[0] == arg])
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
