"""# Make a list of premier league teams
Teams =["Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton & Hove Albion", "Burnley", "Chelsea", "Crystal Palace", "Everton", "Fulham", "Leeds United", "Liverpool", "Manchester City", "Manchester United", "Newcastle United", "Nottingham Forest", "Sunderland", "Tottenham", "West Ham", "Wolverhampton"]

#create function to print a messege based on the index position of the team selected
def Result():
    selected = int(input('based on the list above and your understanding of python indexing, give the index position of the team you support >'))
    print(f'the team you selected is {Teams[selected]}')

# Function to add teams into the list
def dream_team():
    chosen_team = input('if you could add any time to the league next season which would it be? ')
    Teams.append(chosen_team)

#function to remove undesirable team
def rmv_team():
    removed = input('if you could remove your teams rivals which team would it be?, you can give the name of the team or it\'s index position in the Teams list' )
    Teams.remove(removed)

#function to add desired team at desired finishing position
def desired_team():
    desired = input('if you could add any team to the league which would it be? ')
    position = int(input('what position would it be'))
    Teams.insert(position, desired)
  

dream_team()
rmv_team()
desired_team()

print(Teams)"""
#### Part 1

### strings
# Create a variable which will store your first name. Print out the variable.
MyName = 'Brendon'
print(MyName)

# 2. Create a second variable which will store your last name. Concatenate the two variables and print out the result.
MySecondName = 'Maphosa'
print(MyName, MySecondName)

# Extend the above to print the following using an `f-string`: `Hi, my name is {first_name} {last_name}`.
print(f'Hi my name is {MyName} {MySecondName}')

### Integers
# 1. Create two variables that store integer values. Calculate the product (the number you get by multiplying two or more other numbers together) of the two integers and store it in a third variable. Print the value of this variable.
Num1 = 5
Num2 = 10
product = Num1 * Num2
print(product)

# 2. Extend the above to print out the following: `The product of {x} and {y} is {product}`, replacing `x, y, product` with the values for the above.
print(f'The product of {Num1} and {Num2} is {product}')

### lists
# starter list
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

# 1. Retrieve the third element (the second-indexed element) and store it in its own variable. Print the variable.
ThirdEl = people[2]
print(ThirdEl)

# 2. Retrieve the element third from the back of the list and store it in its own variable. Print the variable.
ThirdNegEl = people[-3]
print(ThirdNegEl)

# 3. Split the list into a new list with just the names Mark, Lisa, Joe and Barry.
NewSplitList = people[2:6]

# 4. Print whether or not the first and last element in the list are equal to one another.
print(NewSplitList[0] == NewSplitList[3])

### input
# 1. Accept input from the user for their name. Print their name out.
UserFirstName = input('What is your first name? ')
UserSecondName = input('What is your first name? ')
UserName = f'The users name is {UserFirstName} {UserSecondName}!'
print(UserName)

# 2. Accept two integer inputs from the user and calculate the product. Print out the product.
UserInt1 = int(input('Enter one number '))
UserInt2 = int(input('Enter another number '))
UserProduct = UserInt1 * UserInt2
print(f'The product of your two integer inputs is {UserProduct}')

# 3. Accept two integer inputs from the user. Use the comparison operator to print out if the two values are equal (`True`), or if they're not (`False`).
Cominput1 = int(input('Enter one number '))
Cominput2 = int(input('Enter the second number '))
if Cominput1 == Cominput2:
    print('True, those two numbers are equal to eachother')
else:
    print('False, those two numbers are not equal to eachother')

#### Part 2

### Input and Numbers

# 1. Accept an integer input from the user. If the number is even, print out an appropriate message, and vice versa if it is odd.
Userinput = int(input('Enter a number to check if it is even or odd '))
if Userinput % 1 == 0: 
    print(f'The number {Userinput} is an even number')
else: print(f'The number {Userinput} is an odd number')