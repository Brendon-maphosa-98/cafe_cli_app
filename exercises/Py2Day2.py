### 1.
# Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

Person_i_know = {'first_name': 'James', 'last_name': 'Cooper', 'age': 26, 'City': 'London'}

for key, value in Person_i_know.items():
    print(f'{key}: {value}')

### 2.
# Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

fave_nums = {'saka': 7, 'martinelli': 11, 'havertz': 29, 'odergaard': 8}

for key, value in fave_nums.items():
    print(f'{key}\'s favourite number is {value}')

### 3.
# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'. 

rivers = {'Zambezi': 'Zimbabwe', 'Yangtze': 'China', 'Nile': 'Egypt'}

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt. 

for key, value in rivers.items():
    print(f'The {key} is located in {value}')

# Use a loop to print the name of each river included in the dictionary. 

for value in rivers.values():
    print(value)

# Use a loop to print the name of each country included in the dictionary

for key, value in rivers.items():
    print(key)

### 4.
# Make several dictionaries, where the name of each dictionary is the name of a pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do print everything you know about each pet.

dora = {'type': 'dog', 'owner_name': 'arnold'}
gerald ={'type': 'cat', 'owner_name': 'brendon'}
boris = {'type': 'snake', 'owner_name': 'angeline'}
scarlet = {'type': 'parrot', 'owner_name': 'james'}
pebbles = {'type': 'dog', 'owner_name': 'benjamin'}
ronald = {'type': 'turtle', 'owner_name': 'felicity'}
steve = {'type': 'cat', 'owner_name': 'kirsty'}

pets = []
pets.append(dora)
pets.append(gerald)
pets.append(boris)
pets.append(scarlet)
pets.append(pebbles)
pets.append(ronald)
pets.append(steve)

print(pets)

### 5.
# Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {'steve': 'milan', 'ben': 'new york', 'jerry': ''}