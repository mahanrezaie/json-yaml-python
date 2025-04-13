import yaml
import json
import cmd


class Config_manager():
    def check_file_type(self, file):
        with open(file, "r") as f:
            self.content = f.read()
        try:
            json.loads(self.content)
            return "JSON"
        except json.JSONDecodeError:
            pass
    
        try:
            yaml.safe_load(self.content)
            return "YAML"
        except yaml.YAMLError:
            pass
    
        
    
    def json_to_yaml(self, output_file):
        output_file = open(output_file, "w")
        json_obj = json.loads(self.content)
        yaml.dump(json_obj, output_file)

    def yaml_to_json(self, output_file):
        output_file = open(output_file, "w")
        yaml_obj = yaml.safe_load(self.content)
        json.dump(yaml_obj, output_file)


    def convertor(self, file, output_file):
        file_type = self.check_file_type(file)
        if file_type == "JSON":
            self.json_to_yaml(f"{output_file}.yaml")

        elif file_type == "YAML":
            self.yaml_to_json(f"{output_file}.json")

        else:
             print(f"ERROR: the {file} is not a valid yaml or json, please try again.(yaml file should be started with ---)")


        
class ConfCli(cmd.Cmd, Config_manager):
    intro = "Welcome to the Configuration manager cli!"
    prompt = "manager-cli: "
    def __init__(self):
        super().__init__()

    def do_convert(self, arg):
        "Convert json to yaml or yaml to json."
        file = get_file("Enter the file you want to convert: ")
        file_type = self.check_file_type(file)
        if file_type == "YAML":
            file_type = "json"
        elif file_type == "JSON":
            file_type = "yaml"
        output_file = input(f" please enter a name your .{file_type} for output: ")
        self.convertor(file, output_file)
        

        

def get_file(prompt):
    while True:
        file = input(prompt)  # Get file path from user
        try:
            with open(file, "r") as f:
                return file  # Return the file if it exists
        except FileNotFoundError:
            print("File does not exist. Please try again.")

#Config = Config_manager("test2.yaml", "test2.json")
#print(Config.check_file_type())
#Config = Config_manager()
#print(Config.check_file_type("test.yaml"))
if __name__ == '__main__':
    ConfCli().cmdloop()
