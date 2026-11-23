# Part 1 - basics

print('this is a string')
print("this is a string")
print("this it's a string")

num = 16
name = 'John'

print(f'Hi, my number is {num} and my name is {name}!')

s = 'hello'
print(s[0])             # h
print(s[0:])            # hello
print(s[:3])            # hel
print(s[2:4])           # ll

print([1, 2, 3])
print(['a', 'b', 'c'])

my_list = ['a', 'b', 'c']
print (my_list)         # ['a', 'b', 'c']

my_list.append('d')
print (my_list)         # ['a', 'b', 'c', 'd']

print(my_list[0])

my_list[0] = 'new'
print (my_list)

nest = [1, 2, [3, 4]]
print(nest)
print(nest[2][1])       # 4

n_nest = [1, 2, 3,[4, 5,['target']]]
print(n_nest[3][2][0])  # target

