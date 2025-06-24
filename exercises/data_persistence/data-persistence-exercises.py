# 1. Use the below list to write all names to a file where each name is on a new line.


people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

new_people = open("people_list.txt", "w")

for name in people:
    new_people.write(f"{name}\n")


# 2. Extend this to use `try-except`.

try:
    new_people = open("people_list.txt", "w")
    for name in people:
        new_people.write(f"{name}\n")
except FileNotFoundError as file_error:
    print(f"Sorry the file could not be found {file_error}")

# 3. Extend this to use `try-except-finally` and close the file.

try:
    new_people = open("people_list.txt", "w")
    for name in people:
        new_people.write(f"{name}\n")
except FileNotFoundError as file_error:
    print(f"Sorry the file could not be found {file_error}")
finally:
    new_people.close()

# 4. Extend this to make use of the file context manager (hint: use the keyword `with`).

try:
    with open("people_list.txt", "w") as file:
        for name in people:
            file.write(f"{name}\n")
except FileNotFoundError as file_error:
    print(f"Sorry the file could not be found {file_error}")
finally:
    new_people.close()

# 5. Create a text file with repeated names such as:
"""
    John
    James
    John
    Sally
    John
    Sally
    Mark
    John
"""

# 1. Create a Python script that reads in the repeated-names file. Create a dictionary where the keys are the names from the file and the values are the number of times each name appears in the text file.

names_dict = {}
with open("repeated_names.txt", "r") as file:
    dict_keys = file.readlines()
    for key in dict_keys:
        names_dict.update(
            key,
        )


# 2. Write out to another file where each line looks like:

# Name: John, Count: 4
