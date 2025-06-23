1. Write a list to a file:

    ```py
    people = ['John', 'Sally', 'Mark', 'Lisa', 'Joe', 'Barry', 'Jane']

    file = open('people.txt', 'w')
    for person in people:
    file.write(person + '\n')
    file.close()
    ```

2. Extend to use `try-except`:

    ```py
    people = ['John', 'Sally', 'Mark', 'Lisa', 'Joe', 'Barry', 'Jane']

    try:
    file = open('people.txt', 'w')
    for person in people:
        file.write(person + '\n')
    file.close()

    except Exception as e:
    print('An error occurred: ' + str(e))
    ```

3. Extend to use `try-except-finally` and close the file:

    ```py
    people = ['John', 'Sally', 'Mark', 'Lisa', 'Joe', 'Barry', 'Jane']
    file = None

    try:
        file = open('people.txt', 'w')
        for person in people:
        file.write(person + '\n')

    except Exception as e:
        print('An error occurred: ' + str(e))
    finally:
        file.close()
    ```

4. Extend to make use of a context manager:

  ```py
  people = ['John', 'Sally', 'Mark', 'Lisa', 'Joe', 'Barry', 'Jane']

  try:
    with open('people.txt', 'w') as file:
      for person in people:
        file.write(person + '\n')
  except Exception as e:
    print('An error occurred: ' + str(e))
  ```

5. Make a file with repeated names
    1. Load it, and make a dictionary of the counts of the names

    ```py
    people = {}

    try:
        with open('input.txt', 'r') as file:
        for line in file.readlines():
            person = line.rstrip()

            if not person in people:
            people[person] = 1
            else:
            people[person] = people[person] + 1
        print(people)
    except Exception as e:
        print('An error occurred: ' + str(e))
    ```

    2. Write out to another file where each line looks like:

    ```py
    try:
        with open('output.txt', 'w') as file:
            for key, value in people.items():
            file.write(f'Name: {key}, Count: {value}\n')
    except Exception as e:
        print('An error occurred: ' + str(e))
    ```
