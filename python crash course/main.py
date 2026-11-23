# Part 1 - basics - print | strings | lists

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
print (my_list)         # ['new', 2, 3] - lists are mutable

nest = [1, 2, [3, 4]]
print(nest)
print(nest[2][1])       # 4

n_nest = [1, 2, 3,[4, 5,['target']]]
print(n_nest[3][2][0])  # target




# Part 2 - Dictionaries | truples | sets | booleans | comparision operators

d = {'key1':'value', 'key2':123}
print(d['key1'])        # value
print(d['key2'])        # 123

d = {'k1':[1,2,3]}
print(d['k1'][1])       # 2
my_list = d['k1']
print(my_list[0])       # 1

d = {'k1':{'innerkey':[1, 2, 3]}}
print(d['k1']['innerkey'][1])   # 2


my_list = [1,2,3]
t = (1, 2, 3)
print(t[0])

my_list[0] = 'new'
print(my_list)

#t[0] = 'new'            # ERROR - truples are imutable


set1 = {1,2,3}
print(set1)

n_set = {1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,}
print(n_set)            # {1, 2, 3} - sets are unique

m_list = [1,1,1,2,2,2,3,3,4]
print(set(m_list)) # {1, 2, 3, 4}

print(set([1,1,1,2,2,2,3,3,4]))

set2 = {1,2,3}
set2.add(4)
print(set2)

# 1 > 2
# 1 < 2
# 1 >= 2
# 1 <= 2
# 1 == 2
# 1 != 2

print( 1 < 2 and 2 > 3)
print( 1 < 2 or 2 > 3)

if 1<2 : 
    print('ok!')
if 1 == 2 : 
    print('first')
elif 3 == 3 :
    print('middle')
else :
    print('last')




# Part 3 - loops | functions

seq = [1,2,3,4,5]

for i in seq:
    print(i)

i = 1

while i < 5:
    print(f"i is: {i}")
    i += 1

for x in range(0,5):
    print(x)

z = [1,2,3,4]
out = []
for num in z:
    out.append(num**2)

print(out)

out = [num**2 for num in z]
print(out)


def my_func(param1):
    print(param1)

my_func('hello')


def my_func(name):
    print('Hello '+name)

my_func('Jose')


def square(num):
    """
    for long comments in 
    multiple 
    lines
    """
    return num**2

output = square(2)
print(output)



# Part 4 - lambda | map | filter | lower | upper | slip | pop | unpacking


def times2(var):
    return var*2

print(times2(5))

seq = [1,2,3,4,5]

print(list(map(times2, seq)))

t = lambda var:var*2
print(t(6))

print(list(map(lambda num: num*3,seq)))


print(list(filter(lambda num: num%2 == 0, seq)))

s = 'hello my name is Sam'
t = 'Go Sports! #Sports'
print(s.lower())
print(s.upper())
print(s.split())
print(t.split('#'))

d = {'k1': 1, 'k2': 2}
print(d)
print(d.keys())             # dict_keys(['k1', 'k2'])
print(d.items())            # dict_items([('k1', 1), ('k2', 2)])
print(d.values())           # dict_values([1, 2])

lst = [1,2,3]
print(lst.pop())            # 3 - brings the last item - remove the item from the list
print(lst)                  # [1, 2]
first = lst.pop(0)          # 1
print(first)

lst.append('new')
print(lst)


print('x' in [1,2,3])
print('x' in ['x','y','z'])

x = [(1,2),(3,4),(5,6)]

for item in x:
    print(item)

for a,b in x:
    print(a)
    print(b)


