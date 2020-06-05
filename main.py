import cmd
import json
from datetime import datetime

class matter(object):
    """Physical things are composed of matter"""
    def __init__(self, name, location="here"):
        self.name = name
        self.location = location

    def __getitem__(self, item):
        """Enable bracket syntax for calling attributes of objects created with this class"""
        return getattr(self, item)

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
            newMatter = matter(arg)
            reality[arg] = newMatter.__dict__

    def do_look(self, arg):
        if not arg:
            for thing in reality:
                if reality[thing]["location"] == "here":
                    print(reality[thing]["name"],"is here.")

    def do_destroy(self, arg):
        """Destroy anything in reality by name"""
        if arg in reality:
            reality.pop(arg)

    def do_save(self, arg):
        """Save everything in reality to a JSON file"""
        if arg:
            filename = arg
        else:
            filename = "untitled-"+datetime.now().strftime("%Y-%m-%d-%H%M%S")
        filename = filename+".json" # extension
        filename = "logs/"+filename # folder
        # Save as JSON file
        json_output = open(filename, "w") 
        json.dump(reality, json_output, indent = 6) 
        json_output.close()
        print("Reality saved to",filename)

if __name__ == '__main__':
    running = True
    reality = {} # An object to collect everything that is created
    while running == True:
        prompt().cmdloop()
