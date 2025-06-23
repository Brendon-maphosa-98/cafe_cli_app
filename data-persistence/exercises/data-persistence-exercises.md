1. Use the below list to write all names to a file where each name is on a new line.

    ```py
    people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
    ```

2. Extend this to use `try-except`.
3. Extend this to use `try-except-finally` and close the file.
4. Extend this to make use of the file context manager (hint: use the keyword `with`).
5. Create a text file with repeated names such as:

    ```sh
    John
    James
    John
    Sally
    John
    Sally
    Mark
    John
    ```

    1. Create a Python script that reads in the repeated-names file. Create a dictionary where the keys are the names from the file and the values are the number of times each name appears in the text file.
    2. Write out to another file where each line looks like:

    ```sh
    Name: John, Count: 4
    ```
