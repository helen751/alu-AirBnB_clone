"""Command Line Intepretter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This is the class for the console which is inheriting from cmd.Cmd"""
    prompt = "(hbnb) > "

    def do_quit(self, arg):
        """Quiting the program"""
        return True

    def do_EOF(self, arg):
        """End of the file indication for the program to quit"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
