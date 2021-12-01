from typing import NamedTuple
from numpy.lib.type_check import nan_to_num
import pandas as pd
import numpy as np


data = pd.read_csv("./squirrel_data.csv")

squirrels = data['Primary Fur Color'].unique()
squirrels = np.delete(squirrels, 0)

new_data = data['Primary Fur Color'].value_counts()

print(new_data)