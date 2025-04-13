import yaml
import json
import cmd


class Config_manager():
    def __init__(self, file, output_file):
        self.file = file
        with open(file, "r") as f:
            self.content = f.read()
        self.output_file = output_file

    def __str__(self):
        return self.content

    def check_file_type(self):
        
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
        json_obj = json.loads(self.content)
        yaml.dump(json_obj, output_file)

    def yaml_to_json(self, output_file):
        yaml_obj = yaml.safe_load(self.content)
        json.dump(yaml_obj, output_file)


    def convertor(self):
        output_file = open(self.output_file, "w")
        file_type = self.check_file_type()
        if file_type == "JSON":
            self.json_to_yaml(output_file)

        elif file_type == "YAML":
            self.yaml_to_json(output_file)

        else:
             print(f"ERROR: the {self.file} is not a valid yaml or json, please try again.(yaml file should be started with ---)")


        
class ConfCli(cmd.Cmd, Config_manager):
    intro = "Welcome to the Configuration manager cli!"
    prompt = "manager-cli"
    def __init__(self):
        super().__init__()

    def do_convert(self, arg):
        "Convert json to yaml or yaml to json."
        file = get_file("Enter the file you want to convert: ")


        





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
Config.convertor()

