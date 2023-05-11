import json
import os
import numpy as np
import math
from tinytag import TinyTag

global folder_path

def get_files(dir_path):
    return os.listdir(dir_path)

def extract_metadata(file_name):
    print(file_name)
    full_path = folder_path + '/' + file_name
    audio = TinyTag.get(full_path)
    return file_name, audio.title

def save_as_json(data, save_path):
    with open(save_path, "w") as f:
        json.dump(data, f)
    return

def get_absoulute_path(filename):
    package_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(package_dir,filename)
    return filepath

if __name__ == '__main__':
    folder_path = get_absoulute_path("dataset/audiofiles")
    save_path = get_absoulute_path("dataset/dataset.json")
    train_dataset_save_path = get_absoulute_path('dataset/train.json')
    test_dataset_save_path = get_absoulute_path('dataset/test.json')
    dataset = []
    train_dataset = []
    test_dataset = []
    files = get_files(folder_path)

    for file in files:
        # TODO split into validation and test dataset
        filename, transcript = extract_metadata(file)
        # print(filename, transcript)
        record = {}
        record["key"] = filename
        record["text"] = transcript
        dataset.append(record)
    save_as_json(dataset, save_path)

    #split into train and test dataset
    dataset = np.array(dataset)
    split_position = math.floor(len(dataset)*0.8)

    [train_dataset, test_dataset] = np.split(dataset,[split_position-1])

    save_as_json(train_dataset.tolist(), train_dataset_save_path)
    save_as_json(test_dataset.tolist(), test_dataset_save_path)

    print("Complete")