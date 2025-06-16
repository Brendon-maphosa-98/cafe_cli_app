'''

### Loops

#simple for loop interating over a dict

for x in [1,2]:
    print(f'current number is {x}')


# simple while loop

pet_age = 1 #

while pet_age <= 10: 
    print(f'Diego is {pet_age} years old')
    pet_age += 1

# create an iterable list using the range function

for number in range(0,3): # the last number in this range is exclusive, meaning the number 3 here won't print it will only print up to 3
    print(f'number is {number}')

# nested loops

# creating some lists for example use

adjectives = ['red','big','scary']
fruits = ['apple','grape','strawberry','pear']

for adj in adjectives:
    for fruit in fruits:
        print(f'The {adj} {fruit}')

for fruit in fruits: 
    print(fruit)
    if fruit == 'grape':
        break  # break tells python to stop the loop

for fruit in fruits: 
    if fruit == 'grape':
        continue # the continue keywork tells python to skip the iterable value if meets the conditional, and then the code continues after that
    print(fruit)

# For else

for x in range(6):
    print(x)
else:  # The else keyword tells python what to do when the for loop is finished. If it is used in a if statement, else tells python what to do if the if conditional returns false. 
    print('finished')

# Python 2 exercises, loops

# Print the numbers 0 to 10 using a for loop.

for num in range (0,11):
    print(num)

# Print the numbers 0 to 10 using a while loop.
num = 0
while num <= 10:
    print(num)
    num += 1

# Print the list of numbers below using a for loop.

numbers_list = [0, 2, 8, 20, 43, 82, 195, 204, 367]

for num in numbers_list:
    print(num)

# Print the message 'Done!' after printing the numbers 0 to 10 with a for loop.

for num in range (0,11):
    print(num)
else: 
    print('Done!')

 # Take the below two lists and use a nested for loop to determine if any elements from the first list are in the second. If it finds a match, print out the name of the element.

list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

for item in list1:
    for second_item in list2:
        if item == second_item:
            print(f'{item} occurs in both lists')

# Using a while loop, on every iteration generate a random number. If it's a multiple of 5, **break** from the loop. If it's a multiple of 3, end the current iteration with **continue** and print a message to show you are skipping. If it's neither, print the number and continue the loop.
# When the loop has been broken, print a message indicating that this has happened before the program exits.

import random as random

num = 0
while num >= 0:
    num = random.randrange(int(0), int(1000))
    if num % 5 == int():
        print(f'{num} is a multiple of five and so the loop will now be broken')
        break
    if num % 3 >= int():
        print(f'{num} is a multiple of 3 and so will be skipped')
        continue

    print(num)

 '''   
"""
### Dictionaries

car = {'make': 'Land Rover', 'model': 'Range Rover', 'year': 2025, 'isNew': True}

# adding a key + value into an existing dict

car['price'] = '22000'

carprice = car['price']

# updated an existing key value pair in an existing dictionary

car['year'] = 2024

# deleting a key value pair in a dictionary

del car['price']

print(car.items()) #returns a list of tuples of the keys and values
print('')
print('')
print(car.values()) #returns a list of the values
print('')
print('')
print(car.keys()) #returns a list of the keys

print(len(car.items()))

# number of keys
print(len(car))

# clearing the contents of a dict

car.clear()

print(len(car))"""

'''

# Python 2 Exercises

## Dictionaries

car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year' : 1964,
    'isNew': False}

# Add a new key-value pair to the car dictionary for the `colour`. Print out the `colour` to verify it worked.

car['colour'] = 'Grey'
print(car['colour'])

# Update the value of the `model` in the car dictionary. Print out the new value to verify it worked.

car['model'] = 'Fiesta'
print(car['model'])

# Delete the `model` key-pair from the car dictionary. Print out the entire dictionary to verify it worked.

del car['model']
print(car)

# Use the `items()` function to loop through the dictionary and print each key-value pair like so: key: x, value: y

for y in car.items():
    print(f'Key: {y[0]}, Value: {y[1]}')

'''

'''

### Exceptions

numbers = [1,2,3,4,5,6]

try:
    numbers[6] # this would through an IndexError as there is not 6th index position in the list if it was not in this try block
except:
    print('That index position does not exist')

# catching what the exception was 

try:
    numbers[6] 
except: # this takes the exception that could arise and assigns it to the mistake variable
    print('There was an issue')


try:
    numbers[6] 
except Exception as mistake: # this takes the exception that could arise and assigns it to the mistake variable
    print(mistake)

'''

### functions

def add_numbers(a, b):
    return a + b

add_numbers(1,2)

