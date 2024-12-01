import pandas as pd
import numpy as np

# Read the data
data = pd.read_csv('puzzle.csv', header=None)

# Convert each column to an numpy array
list1 = data[0]
list2 = data[1]

list3 = abs(np.array(sorted(list1)) - np.array(sorted(list2)))

# Answer for part 1
print(f"Part 1 answer: {sum(list3)}")

data["left_count_in_right"] = [data[1].to_list().count(x) for x in data[0].values]
data["occ"] = data[0].values * data["left_count_in_right"]

# Answer for part 2
print(f"Part 2 answer: {sum(data["occ"])}")
