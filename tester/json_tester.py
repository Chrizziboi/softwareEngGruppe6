import os.path
import json
import backend.json.read as jsonR
import backend.json.write as jsonW
import pytest

test_data = {
    "userID": 1,
    "username": "user",
    "adminID": 1,
    "adminname": "admin"

}
write_test_file = "test_jsonW"
read_test_file = "test_jsonR"

def test_json_write():
    jsonW.write_json(write_test_file, test_data)

    assert os.path.exists(write_test_file)

    with open(write_test_file, "r") as file:
        written_data = json.load(file)

    assert written_data == test_data


def test_json_read():
    with open(read_test_file, "w") as file:
        json.dump(test_data, file)

    data_from_function = jsonR.read_json(read_test_file)

    assert data_from_function == test_data

def delete_testfiles():
    if os.path.exists("test_jsonR"):
        os.remove("test_jsonR")
    if os.path.exists("test_jsonW"):
        os.remove("test_jsonW")

delete_testfiles()