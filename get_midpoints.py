import os
import glob
import numpy as np
import json
import collections
from tqdm import tqdm

square_median = collections.defaultdict(lambda: {"lat": [], "lon": []})

print('getting subdirectories...')
subdirs = glob.glob('500k_world/*/') 

for subdir in tqdm(subdirs, desc='Processing directories'):
    dir_name = os.path.basename(os.path.normpath(subdir))

    square_id, lat, long = dir_name.split(',')

    square_median[int(square_id)]["lat"].append(float(lat))
    square_median[int(square_id)]["lon"].append(float(long))

for square_id in tqdm(square_median.keys(), desc='Calculating medians'):
    square_median[square_id]["lat"] = np.median(square_median[square_id]["lat"])
    square_median[square_id]["lon"] = np.median(square_median[square_id]["lon"])

print(square_median)

with open('500k_median.json', 'w') as f: 
    json.dump(square_median, f)
