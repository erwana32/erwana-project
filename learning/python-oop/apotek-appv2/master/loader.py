import json

FILE_PATH = "master/obat.json"

def load_master():
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def save_master(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)