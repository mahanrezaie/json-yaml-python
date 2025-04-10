from yaml import safe_load, YAMLError

def open_file(file):
    try:
        with open(file, "r") as f:
            yaml_string = safe_load(f)
            return yaml_string

    except YAMLError as e:
        print(f"Error: {file} is not a valid YAML - {e}")




test = open_file("test.yaml")
print(test)
