import cmd
import json
from datetime import datetime

class matter(object):
    """Physical things are composed of matter"""
    def __init__(self, name, location="here"):
        self.name = name
        self.location = location
        self.type = type(self).__name__ # name of the class, for save unpacking
        self.description = (self.name).title()+" is "+self.location+"."

    def __getitem__(self, item):
        """Enable bracket syntax for calling attributes of objects created with this class"""
        return getattr(self, item)

    def describe(self):
        print(self.description)

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
            newMatter = matter(arg)
            reality[arg] = newMatter
            print("You create "+reality[arg].name+".")
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
        else: # if trying to look at something
            if arg in reality:
                reality[arg].describe()

    def do_destroy(self, arg):
        """Destroy anything in reality by name"""
        if arg in reality:
            reality.pop(arg)
            print("You remove",arg,"from reality.")

    def do_save(self, arg):
        """Save everything in reality to a JSON file"""
        # Package reality into a dictionary for JSON storage
        realitySeed = {}
        for creation in reality:
            realitySeed[creation] = reality[creation].__dict__
        # Identify save location
        if arg:
            filename = arg
        else:
            filename = "untitled-"+datetime.now().strftime("%Y-%m-%d-%H%M%S")
        filename = filename+".json" # extension
        filename = "logs/"+filename # folder
        # Save as JSON file
        json_output = open(filename, "w")
        json.dump(realitySeed, json_output, indent = 6) 
        json_output.close()
        print("Reality saved to",filename)

    def do_load(self, arg):
        """Load a previously saved reality < Warning > This will overwrite the current reality"""
        global reality
        global realityEgg
        reality = {} # Purge reality before loading the new one
        realityEgg = {} # Purge reality before loading the new one
        filename = arg
        with open("logs/"+arg+".json") as json_file:
            realityEgg = json.load(json_file)
        
        # Convert the realityEgg from JSON into class instances and store them in reality
        #   "name" key indicates what to name the instance within the reality object
        #   "type" key indicates which class is applied
        print("Created:") if realityEgg else False
        for creation in realityEgg:
            reality[realityEgg[creation]["name"]] = globals()[realityEgg[creation]["type"]](creation)
            print(reality[creation].name)

if __name__ == '__main__':
    running = True
    reality = {} # An object to collect everything that is created
    while running == True:
        prompt().cmdloop()
