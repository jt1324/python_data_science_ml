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