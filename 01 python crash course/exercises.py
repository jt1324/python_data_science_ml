# Python Crash Course Exercises


# 1. What is 7 to the power of 4?
print(7**4)


# 2. Split this string: 
s = "Hi there Sam!"
# into a list.
print(s.split())


# 3. Given the variables:
planet = "Earth"
diameter = 12742
# Use .format() to print the following string:
# The diameter of Earth is 12742 kilometers.
print(f"The diameter of {planet} is {diameter} kilometers.")


# 4. Given this nested list, use indexing to grab the word "hello"
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2])


# 5. Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/trick
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])


# 6. What is the main difference between a tuple and a list?
print("Lists are mutable and truples no.")


# 7. Create a function that grabs the email website domain from a string in the form:
# email =  'user@domain.com'
# So for example, passing "user@domain.com" would return: domain.com
def get_email(email):
    print(email.split('@')[1])

get_email('user@domain.com')

# 8. Create a basic function that returns True if the word 'dog' is contained in the input string. 
# Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization.
def dog(text):
    if ('dog').lower() in (text).lower():
        print('True')
    else:
        print('False')

dog('I do not have a dog')
dog('I do have a DOG')
dog('I do not have a cat')


# 9. Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases.
def count(words):
    return words.lower().split().count('dog')

print (count('dog DOG Dog cat horse'))


# 10. Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:
seq = ['soup','dog','salad','cat','great']
# should be filtered down to:
# ['soup','salad']
print(list(filter(lambda num: num[0] == 's', seq)))



# 11. You are driving a little too fast, and a police officer stops you. Write a function
# to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
# If your speed is 60 or less, the result is "No Ticket". If speed is between 61
# and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your
# birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.
def drive(speed, bday=False):
    if bday == False:
        if speed <= 60:
            return 'No ticket'
        elif speed <= 80:
            return 'Small ticket'
        else:
            return 'Big ticket'
    else:
        if speed-5 <= 60:
            return 'No ticket'
        elif speed-5 <= 80:
            return 'Small ticket'
        else:
            return 'Big ticket'

print(drive(65, True))
