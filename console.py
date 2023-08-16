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

    def default(self, line):
        args = line.split(".")
        ln = ""
        if len(args) >= 2:
            sub = args[1].split("(")
            cmd_name = sub[0]
            ln = cmd_name+" "+args[0]
            if (sub[1].startswith("\"")):
                sub_args = sub[1].split("\"")
                ln = ln+" "+sub_args[1]
        r = super(HBNBCommand, self).onecmd(ln)
        if r:
            print("*** unknown syntax: "+line)
        return

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
            return
        cls = classes[arg]
        new_cls = cls()
        mddl.storage.save()
        print(new_cls.id)

    def do_show(self, arg):
        'prints string representation of instance based on class name and id'
        args = utl.validate_args(arg)
        if args:
            print(mddl.storage.all().get(args[0]+"."+args[1]))

    def do_count(self, line):
        'Counts instances of a class'
        if not utl.check_cls_exists(line):
            return
        count = 0
        for key in mddl.storage.all().keys():
            if key.startswith(line):
                count += 1
        print(count)

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
            if not utl.check_cls_exists(arg):
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
