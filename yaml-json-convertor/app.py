import yaml
import json


class Config_manager():
    def __init__(self, file, input_file, output_file):
        self.file = file
        with open(file, "r") as f:
            self.content = f.read()
        self.input_file = open(file, "r")
        self.output_file = open(file, "w")


    def check_file_type(self):
        
        try:
            json.loads(self.content)
            return "JSON"
        except json.JSONDecodeError:
            pass
    
        try:
            if self.content.strip().startswith("---"): # it is common to use --- to start a yaml file
                yaml.safe_load(self.content)
                return "YAML"
        except yaml.YAMLError:
            pass
    
        return "NONE"
    
    def json_to_yaml(self):
        json_obj = json.loads(self.input_file)
        yaml.dump(json_obj, self.output_file)

    def yaml_to_json(self):
        yaml_obj = yaml.safe_load(self.input_file)
        json.dump(yaml_obj, self.output_file)


    def convertor(self):
        file_type = self.check_file_type()
        if file_type == "JSON":
            self.json_to_yaml()

        elif file_type == "YAML":
            self.yaml_to_json()

        elif file_type == "NONE":
            return f"ERROR: the {self.file} is not a valid yaml or json, please try again.(yaml file should be started with ---)"


        









