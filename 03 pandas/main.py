import numpy as np
import pandas as pd

# Series

labels = ['a', 'b', 'c']
my_data = [10, 20,30]
arr = np.array(my_data)
d = {'a':10, 'b':20, 'c':30}

print(pd.Series(data = my_data))

print(pd.Series(data=my_data, index=labels))
print(pd.Series(my_data, labels))                       # Same result as above - is not necessary to specify data and index

print(pd.Series(arr, labels))

print(pd.Series(d))

ser1 = pd.Series([1,2,3,4], ['UK', 'USA', 'Germany', 'Japan'])
print(ser1)

ser2 = pd.Series([1,2,5,4], ['UK', 'USA', 'Brazil', 'Japan'])
print(ser2)

print(ser1['UK'])

ser3 = pd.Series(data=labels)
print(ser3)

print(ser3[2])

print(ser1 + ser2)



# DataFrames - Part 1

from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

print(df['W'])                                          # Selecting a single column
print(df.W)                                             # Same result as bove, but better avoind using
print(df[['W', 'Z']])                                   # Selecting multiple columns
df['new'] = df['W'] + df['Y']                           # Creating a new column
print(df)

df.drop('new', axis=1, inplace=True)                    # Drop a column (axis=1)
print(df)

# df.drop('E', axis=0, inplace=True)                    # Drop a row (axis=0)
print(df)

print(df.shape)                                         # (5, 4) axis 0-rows = 5 | axis 1-columns = 4

print(df.loc['C'])                                      # Selecting rows
print(df.iloc[2])                                       # Same result as above

print(df.loc['B','Y'])                                  # Selecting specific cell
print(df.loc[['A','B'],['W','Y']])                      # Selecting a range of cells
