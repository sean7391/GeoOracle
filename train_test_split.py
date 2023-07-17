import os
import json
from sklearn.model_selection import train_test_split

def load_train_val_test_paths(path_to_imgdir, test_size=0.05, val_size=0.05, seed=0):
    all_paths = [x for x in os.walk(path_to_imgdir)][1:] 

    all_paths = [path[0] for path in all_paths]

    train_paths, test_paths = train_test_split(all_paths, test_size=test_size, random_state=seed)
    train_paths, val_paths = train_test_split(train_paths, test_size=val_size/(1-test_size), random_state=seed)

    print('Train size: ', len(train_paths))
    print('Test size: ', len(test_paths))
    print('Val size: ', len(val_paths))

    return train_paths, val_paths, test_paths

dir_path = 'world_data'  # CHANGE TO RIGHT DIRECTORY
train_paths, val_paths, test_paths = load_train_val_test_paths(dir_path, test_size=0.1, val_size=0.1, seed=0)
prefix = '/kaggle/input/world-data/' # CHANGE KAGGLE PREFIX
train_paths = [prefix + path for path in train_paths]
val_paths = [prefix + path for path in val_paths]
test_paths = [prefix + path for path in test_paths]

data_dict = {'train_paths': train_paths, 'val_paths': val_paths, 'test_paths': test_paths}

# CHANGE JSON NAME
json_file = "world_split.json"

with open(json_file, 'w') as outfile:
    json.dump(data_dict, outfile)

print(data_dict)
# with open(json_file, 'r') as infile:
#     data_dict = json.load(infile)

