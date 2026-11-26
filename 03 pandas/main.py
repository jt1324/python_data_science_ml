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




# DataFrames - Part 2
# Conditional selection

print(df > 0)

booldf = df > 0
print(df[booldf])

print(df['W']>0)
print(df[df['W']>0])                                    # Only returns positive numbers or True numbers for that column 'W'

print(df[df['Z']<0])

resultdf = df[df['W']>0]['X']                           # selecting only column 'X' from the reult
print(resultdf)

resultdf = df[df['W']>0][['X', 'X']]
print(resultdf)

# Multi conditional selection

print(df[(df['W']>0) & (df['Y']>1)])                    # and = &

print(df[(df['W']>0) | (df['Y']>1)])                    # or = |

# Index

# df.reset_index(inplace=True)
print(df)

newind = 'CA NY WY OR CO'.split()
print(newind)

df['States'] = newind                                   # Adding a column
print(df)

# df.set_index('States', inplace=True)                  # replaces teh index by the column



# DataFrames - Part 3
# Index levels

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

print(list(zip(outside,inside)))
print(hier_index)

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

print(df.loc['G1'])
print(df.loc['G1'].loc[1])

print(df.index.names)
df.index.names = ['Groups', 'Num']                      # adding names for indexes
print(df)

print(df.loc['G2'].loc[2]['B'])                         # FIltering a specific number from the table
print(df.loc['G1'].loc[1]['B']) 

print(df.xs('G1'))
print(df.xs(1,level='Num'))                             # Filtering all 1 from Column 'Num'




# Missing Data

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}

df = pd.DataFrame(d)
print(df)

df.dropna()                                             # delete all the rows that has at leas 1 empty cell
df.dropna(axis=1)                                       # delete all the column that has at leas 1 empty cell

df.dropna(thresh=2)                                     # keep rows with at least 2 non empty cells

# df = df.fillna(value='FILL VALUE')                    # Replacing the na for something
print(df)

# df = df['A'].fillna(value=df['A'].mean())             # Replacing NA in specific columns 
print(df)

