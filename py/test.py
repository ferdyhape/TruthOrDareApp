import json


def read_json_file(path_file):
    try:
        with open(path_file) as file:
            data = file.read()
            data_json = json.loads(data)
            
        return data_json
    except FileNotFoundError:
        print(f"File {path_file} not found.")
    except json.JSONDecodeError:
        print(f"Error!!!")


json_data = read_json_file("../data/data.json")

print(json_data['truth_questions'])