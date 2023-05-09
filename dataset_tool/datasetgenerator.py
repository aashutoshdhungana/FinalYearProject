import json
import os
from tinytag import TinyTag

global folder_path
global save_path
def get_files(dir_path):
    return os.listdir(dir_path)

def extract_metadata(file_name):
    full_path = folder_path + '/' + file_name
    audio = TinyTag.get(full_path)
    return full_path, audio.title

def save_as_json(data):
    with open(save_path, "w") as f:
        json.dump(data, f)
    return

if __name__ == '__main__':
    folder_path = "./dataset/audiofiles"
    save_path = "./dataset/dataset.json"
    dataset = []
    files = get_files(folder_path)
    for file in files:
        filename, transcript = extract_metadata(file)
        print(filename, transcript)
        record = {}
        record["key"] = filename
        record["text"] = transcript
        dataset.append(record)
    save_as_json(dataset)
    print("Complete")