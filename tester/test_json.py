import os.path
import json

def write_json(filename, data):

    try:
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data written to {filename}")
    except Exception as e:
        print(f"Error writing to {filename}: {str(e)}")

def read_json(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except json.JSONDecodeError:
        print(f"Invalid JSON in file {filename}")
        return None

test_data = {
    "userID": 1,
    "username": "user",
    "adminID": 1,
    "adminname": "admin"

}
write_test_file = "test_jsonW"
read_test_file = "test_jsonR"

def test_json_write():
    write_json(write_test_file, test_data)

    assert os.path.exists(write_test_file)

    with open(write_test_file, "r") as file:
        written_data = json.load(file)

    assert written_data == test_data


def test_json_read():
    with open(read_test_file, "w") as file:
        json.dump(test_data, file)

    data_from_function = read_json(read_test_file)

    assert data_from_function == test_data

def delete_testfiles():
    if os.path.exists("test_jsonR"):
        os.remove("test_jsonR")
    if os.path.exists("test_jsonW"):
        os.remove("test_jsonW")

delete_testfiles()