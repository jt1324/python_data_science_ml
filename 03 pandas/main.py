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




# Groupby

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

byComp = df.groupby('Company')                          # Grouping by comlum 'COmpany'
print(byComp.mean(numeric_only=True))                   # Average of values for the group
print(byComp.sum(numeric_only=True))                    # Sum of values for the group
print(byComp.sum().loc['FB'])                           # Filtering after group

print(df.groupby('Company').sum().loc['GOOG'])          # Applying all in one line of code

print(df.groupby('Company').count())                    # Counting
print(df.groupby('Company').max())                      # Maximum - including Names
print(df.groupby('Company').min())                      # Minimum - including names

print(df.groupby('Company').describe())                 # Show details like, counmt, avg, min, max, ...

print(df.groupby('Company').describe().transpose()['MSFT'])



# Merging, Joining, and Concatenating

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                        'B': ['B4', 'B5', 'B6', 'B7'],
                        'C': ['C4', 'C5', 'C6', 'C7'],
                        'D': ['D4', 'D5', 'D6', 'D7']},
                        index=[4, 5, 6, 7])

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                        'B': ['B8', 'B9', 'B10', 'B11'],
                        'C': ['C8', 'C9', 'C10', 'C11'],
                        'D': ['D8', 'D9', 'D10', 'D11']},
                        index=[8, 9, 10, 11])

print(df1)
print(df2)
print(df3)

# Concatenation

union_all = pd.concat([df1,df2,df3])                             # Union all
print(union_all)

union = pd.concat([df1,df2,df3],axis=1)                          # Union
print(union)

# Merge

left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
    
    
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})

print(right)
print(left)

merged = pd.merge(left,right,how='inner',on='key')                  # Inner join
print(merged)


left1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                        'A': ['A0', 'A1', 'A2', 'A3'],
                        'B': ['B0', 'B1', 'B2', 'B3']})
    
right1 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                         'C': ['C0', 'C1', 'C2', 'C3'],
                         'D': ['D0', 'D1', 'D2', 'D3']})

print(right1)
print(left1)

merged1 = pd.merge(left1,right1,on=['key1', 'key2'])                
print(merged1)

merged2 = pd.merge(left1,right1, how='outer', on=['key1', 'key2'])      # Outer join
print(merged2)

merged3 = pd.merge(left1,right1, how='left', on=['key1', 'key2'])      # Left join
print(merged3)

# Joining - similar to merge, but is based in teh index rather than on or more columns like merge

left2 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                     'B': ['B0', 'B1', 'B2']},
                      index=['K0', 'K1', 'K2'])
    
right2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                    'D': ['D0', 'D2', 'D3']},
                      index=['K0', 'K2', 'K3'])

print(left2)
print(right2)

left_t = left2.join(right2)
print(left_t)

outer_t = left2.join(right2, how='outer')
print(outer_t)



# Operations

df = pd.DataFrame({'col1':[1,2,3,4],'col2':[444,555,666,444],'col3':['abc','def','ghi','xyz']})

print(df.head())

# Finding unique values

print(df['col2'].unique())                                  # Shows the unique values
print(len(df['col2'].unique()))                             # Shows how many unique values
print(df['col2'].nunique())                                 # Same result as above - qty of unique values

print(df['col2'].value_counts())                            # Shows the unique values and how many times they appear

# Apply

def times2(x):
    return x*2

print(df['col1'].apply(times2))

print(df['col3'].apply(len))

print(df['col2'].apply(lambda x: x*2))

# Getting column and index names

print(df.columns)
print(df.index)

# Sorting and ordering a data frame

print(df.sort_values('col2'))                                       # Ordering data by column - Ascending
print(df.sort_values('col2', ascending=False))                      # Ordering data by column - Descending
print(df.sort_values(['col2', 'col1'], ascending=[False, True]))    # Ordering data by more than 1 column - Descending & Ascending

# Checking nulls

print(df.isnull())

# Pivot tables

data = {'A':['foo','foo','foo','bar','bar','bar'],
       'B':['one','one','two','two','one','one'],
       'C':['x','y','x','y','x','y'],
       'D':[1,3,2,5,4,1]}
    
df = pd.DataFrame(data)

print(df.pivot_table(values='D',index=['A', 'B'],columns=['C']))