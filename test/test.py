import json
import pickle
import os

temple_path = ''.join([os.getcwd(),'/far/temple.json'])

print(temple_path)

with open(temple_path, 'r') as f:
    f_dict = json.load(f)
    # print(f_dict.get("'))

    


