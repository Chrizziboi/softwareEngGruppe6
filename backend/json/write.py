import json

def write_json(filename, data):

    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data written to {filename}")
    except Exception as e:
        print(f"Error writing to {filename}: {str(e)}")
