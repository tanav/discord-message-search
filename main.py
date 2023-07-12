# initialize path to directory with discord data
path = '/content/drive/MyDrive/messages.zip'

import zipfile
with zipfile.ZipFile(path, 'r') as zf:
    zf.extractall()

import os
import json
import csv
import pandas as pd
import numpy as np

directory = '/content/messages'
for path, dirs, files in os.walk(directory):
    for filename in os.listdir(path):
        if filename.endswith(".json"):
            with open(os.path.join(path, "channel.json")) as jsonfile:
                data = json.load(jsonfile)

                if data["type"] is not 1:
                    break

                print(data["recipients"][1] + "\n")

                df = pd.read_csv(os.path.join(path, "messages.csv"), usecols=["Contents"])
                arr = df.to_numpy()

                print("".join(map(str, arr)) + "\n")