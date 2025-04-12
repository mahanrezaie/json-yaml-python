from yaml import safe_load, YAMLError

def open_file(file):
    try:
        with open(file, "r") as f:
            yaml_dict = safe_load(f)
            return yaml_dict

    except YAMLError as e:
        print(f"Error: {file} is not a valid YAML - {e}")

def key_value_devider(yaml_dict: dict):
    for key, value in yaml_dict.items():
        print(f"{key}: {value}")



test = open_file("parse.yaml")
yaml_dict = key_value_devider(test)


