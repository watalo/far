import json
import pickle
import os
import sys
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)



temple_path = ''.join([os.getcwd(),'/far/temple.json'])

print(temple_path)

with open(temple_path, 'r') as f:
    f_dict = json.load(f)
    # print(f_dict.get("'))

    


