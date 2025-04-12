import yaml
import json

def check_file_type(file: str):
    with open(file, "r") as f:
        content = f.read()

    try:
        json.loads(content)
        return "JSON"
    except json.JSONDecodeError:
        pass

    try:
        if content.strip().startswith("---"): # it is common to use --- to start a yaml file
            yaml.safe_load(content)
            return "YAML"
    except yaml.YAMLError:
        pass

    print(f"The file {file} is not JSON or YAML.")




