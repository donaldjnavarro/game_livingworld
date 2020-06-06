import cmd
import json
from datetime import datetime

class matter(object):
    """Physical things are composed of matter"""
    def __init__(self, soul):
        # When creating matter from a payload, use whatever key/value pairs are provided
        if type(soul) is dict:
            for key, value in soul.items():
                setattr(self, key, value)
        # When creating matter within the ui, autogenerate the instance variables
        if type(soul) is str:
            self.name = soul
            self.location = "here"
            self.type = type(self).__name__ # name of the class, for save unpacking
            self.description = (self.name).title()+" is "+self.location+"."

    def __getitem__(self, item):
        """Enable bracket syntax for calling attributes of objects created with this class"""
        return getattr(self, item)

    def describe(self):
        """Display a physical description of the instance"""
        print(self.description)

    def destroy(self):
        """Delete and instance and completely remove it from the reality"""
        print((self.name).title(),"is destroyed, completely removed from reality.")
        reality.pop(self.name)

class prompt(cmd.Cmd):
    """Global prompt. This class creates the default prompt interface. All menus should inherit this class"""
    # Methods in this class should never return True. In this root prompt that would be the equivalent of restarting the app
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
            reality[arg].destroy()

    def do_save(self, arg):
        """Save everything in reality to a JSON file"""
        # Package reality into a dictionary for JSON storage
        realityEgg = {}
        for creation in reality:
            realityEgg[creation] = reality[creation].__dict__
        # Identify save location for reality
        if arg:
            filename = arg
        else:
            filename = "untitled-"+datetime.now().strftime("%Y-%m-%d-%H%M%S")
        filename = "reality/"+filename+".json"
        # Save reality as JSON file
        json_output = open(filename, "w")
        json.dump(realityEgg, json_output, indent = 6) 
        json_output.close()
        print("Reality saved to",filename)

    def do_load(self, arg):
        """Load a previously saved reality < Warning > This will overwrite the current reality"""
        global reality
        global realityEgg
        reality = {} # Purge reality before loading the new one
        realityEgg = {} # Purge reality before loading the new one
        filename = arg
        if not arg:
            print("You need to specify a filename of which JSON file in the reality folder you want to load.")
            return False
        try:
            filename = "reality/"+arg+".json"
            with open(filename) as json_file:
                realityEgg = json.load(json_file)
        except:
            print(filename)
            print("No such file found, or invalid file format.")
            print("Please specify a valid filename.")
            print("Do not include the folder or file extension.")
            return False
        # Convert the realityEgg from JSON into class instances and store them in reality global
        #   "name" key indicates what to name the instance within the reality object
        #   "type" key indicates which class is applied
        print("Loading "+filename)
        print("You begin to create...") if realityEgg else False
        for creation in realityEgg:
            reality[realityEgg[creation]["name"]] = globals()[realityEgg[creation]["type"]](realityEgg[creation])
            print("..."+reality[creation].name)

    def do_reboot(self, arg):
        """End the current reality and restart from scratch."""
        print("You wipe away all of reality.")
        return True

if __name__ == '__main__':
    existance = True
    while existance == True:
        print("There is nothing but void.")
        reality = {} # An object to collect everything that is created
        prompt().cmdloop()
