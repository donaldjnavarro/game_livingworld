import cmd

class matter(location):


class prompt(cmd.Cmd):
    """Global prompt. This class creates the default prompt interface. All menus should inherit this class"""
    prompt = ": "
    
    def do_quit(self, arg):
        """Close the program"""
        quit()
    
    def emptyline(self):
        # return cmd.Cmd.emptyline(self) # this will repeat the last entered command
        return False

    def precmd(self, line):
        return cmd.Cmd.precmd(self, line)

    def postcmd(self, stop, line):
        return cmd.Cmd.postcmd(self, stop, line)

    def do_create(self, arg):
        if arg:
            print("You attempt to create",arg)
            created = arg

if __name__ == '__main__':
    running = True
    while running == True:
        prompt().cmdloop()
