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
    
    def read_config(self, file):
        with open(file, "r") as f:
            content = f.read()
        return content

    def yaml_load(self, file):
        with open(file, "r") as f:
            data = yaml.safe_load(f)
        return(data)

    def json_load(self, file):
        with open(file, "r") as f:
            data = json.loads(f)
        return(data)


    def json_to_yaml(self, output_file):
        output_file = open(output_file, "w")
        json_obj = json.loads(self.content)
        yaml.dump(json_obj, output_file)

    def yaml_to_json(self, output_file):
        output_file = open(output_file, "w")
        yaml_obj = yaml.safe_load(self.content)
        json.dump(yaml_obj, output_file)
     
    def update_json(self, data, output_file):
        with open(output_file, "w") as f:
            json.dump(data, f, indent= 4)


    def update_yaml(self, data, output_file):
        with open(output_file, "w") as f:
            yaml.dump(data, f)
        
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
        
    def do_read(self, arg):
        "Reads a config"
        file = get_file("Enter the file you want to read: ")
        content = self.read_config(file)
        print(content)

    def do_quit(self, arg):
        "Quits the cli"
        print("Goodbye")
        return True

    def do_update(self, arg):
        "Update the config, you can add and "
        file = get_file("Which file do you want to update: ")
        file_type = self.check_file_type(file)
        if file_type == "JSON":
            data = self.json_load(file)
        elif file_type == "YAML":
            data = self.yaml_load(file)
        else:
            print("Unsupported file type.")
            return
        while True:
            print("\nCurrent config: ")
            print(self.read_config(file))

            key = input("Enter the key you want to update or type 'exit':  ")
            if key.lower() == "exit":
                break
            value = input(f"Enter the value for {key}: ")
            # If nested keys are needed (ex: user.name), split them:
            if '.' in key:
                keys = key.split('.')
                d = data
                for k in keys[:-1]:
                    d = d.setdefault(k, {})  # walk to the nested dict
                d[keys[-1]] = value
            else:
                data[key] = value
                
            if file_type == "JSON":
                self.update_json(data, file)
            elif file_type == "YAML":
                self.update_yaml(data, file)

    def help_update(self):
                    print("""
        Update the config file by changing or adding values.
        
        🔹 Usage:
            update
        
        👉 When prompted:
            - Enter the path to the config file (JSON or YAML).
            - Enter the key you want to update.
            - Enter the new value.
        
        💡 Nested Keys:
            To update values inside nested structures, use dot notation.
        
            Example:
                user.name.first
        
        This will update:
            {
                "user": {
                    "name": {
                        "first": "NewValue"
                    }
                }
            }
        
        ✅ Type 'exit' to finish and save your changes.
        """)
        

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
