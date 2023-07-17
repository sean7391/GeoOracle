import os
from collections import defaultdict

def get_images_distribution():
    images_dir = 'world_dataset_3' # CHANGE DIRECTORY

    square_id_counts = defaultdict(int)

    for file in os.listdir(images_dir):
        square_id = file.split(',')[0]
        square_id_counts[square_id] += 1

    return square_id_counts

distribution = get_images_distribution()
print(len(distribution))
cnt = 0 
for square_id, count in distribution.items():
    if count > 50:
        cnt += 1
        print(f'{square_id}: {count}')

print(cnt)



# import matplotlib.pyplot as plt
# import numpy as np

# def plot_distribution(distribution):
#     # Prepare data for histogram
#     values = list(distribution.values())
    
#     # Create histogram
#     plt.hist(values, bins=range(1, 102), edgecolor='black', align='left')
    
#     # Set x and y axis labels
#     plt.xlabel('Number of images per square')
#     plt.ylabel('Number of squares')

#     # Set x ticks
#     plt.xticks(np.arange(1, 101, 5))  # show every 5th label to avoid congestion

#     # Show the plot
#     plt.show()

# # Call the function
# plot_distribution(distribution)

