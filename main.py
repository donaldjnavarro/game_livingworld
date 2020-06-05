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
    prompt = "\n: "
    
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
        """Create and name some matter"""
        if arg:
            print("You attempt to create",arg)
            newMatter = matter(arg)
            reality[arg] = newMatter.__dict__
        else:
            print("Please include a name for your creation")

    def do_look(self, arg):
        """Display anything in reality that is here"""
        if not arg:
            if reality:
                print("You see:")
                for thing in reality:
                    if reality[thing]["location"] == "here":
                        print(reality[thing]["name"])
                    # TODO: Will need to create a cap to how many things can display, reality will be getting to be quite a long list
            else:
                print("You see nothing but bleak, empty void. Someone needs to create something.")

    def do_destroy(self, arg):
        """Destroy anything in reality by name"""
        if arg in reality:
            reality.pop(arg)
            print("You remove",arg,"from reality.")

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

    def do_load(self, arg):
        """Load a previously saved reality < Warning > This will overwrite the current reality"""
        global reality
        with open("logs/test.json") as json_file:
            reality = json.load(json_file)



if __name__ == '__main__':
    running = True
    reality = {} # An object to collect everything that is created
    while running == True:
        prompt().cmdloop()
