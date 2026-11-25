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
