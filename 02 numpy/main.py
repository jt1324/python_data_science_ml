# NumPy - Arrays

my_list = [1, 2, 3]
print (my_list)

import numpy as np

arr = np.array(my_list)
print(arr)

my_mat = [[1,2,3],[4,5,6],[7,8,9]]
arr2 = np.array(my_mat)
print(arr2)

test1 = np.arange(0,11)
print(test1)                            # [ 0  1  2  3  4  5  6  7  8  9 10]

test2 = np.arange(0,11, 2)      
print(test2)                            # [ 0  2  4  6  8 10]

test3 = np.zeros((5,5))
print(test3)                            

test4 = np.ones((3,4))
print(test4)  

test5 = np.linspace(0,5,10)
print(test5)

test6 = np.eye(5)
print(test6)

test7 = np.random.rand(5)
print(test7)

test8 = np.random.rand(5,5)
print(test8)

test9 = np.random.randn(2)
print(test9)

test10 = np.random.randn(4,3)
print(test10)

test11 = np.random.randint(1,100)
print(test11)

test12 = np.random.randint(1,100, 10)
print(test12)                           # [18 20 89  9 73 43 64  5 57 96]


arr = np.arange(25)
print(arr)

ranarr = np.random.randint(0,50,10)
print(ranarr)

shape = arr.reshape(5,5)
print(shape)


print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax())
print(ranarr.argmin())

print(arr.shape)

print(arr.dtype)



# NumPy - Indexing & Selection

arr = np.arange(0,11)
print(arr)

print(arr[8])
print(arr[1:5])
print(arr[0:5])
print(arr[:6])
print(arr[5:])

arr[0:5] = 100
print(arr)

arr = np.arange(0,11)

slice_of_arr = arr[0:6]
print(slice_of_arr)
slice_of_arr[:]                         # [0 1 2 3 4 5] - shows the whole array

arr_copy = arr.copy()

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)

print(arr_2d[1][0])                     # 20 - first is row and second is column
print(arr_2d[1,0])                      # 20 - same result

print(arr_2d[:2,1:])                    # [[10 15] [25 30]]
 
arr = np.arange(1,11)
bool_arr = arr > 5
print(bool_arr)                         # [False False False False False  True  True  True  True  True]

print(arr[bool_arr])                    # [ 6  7  8  9 10]
print(arr[arr>5])                       # [ 6  7  8  9 10] - same result - conditional filtering - bring only True numbers for the condition
print(arr[arr<3])                       # [1 2]


