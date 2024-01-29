import json


def read_and_print_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print(f"The file {filename} was not found.")
    except json.JSONDecodeError:
        print(f"The file {filename} does not contain valid JSON.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


filename = "test_data/sample.json"
read_and_print_json(filename)
