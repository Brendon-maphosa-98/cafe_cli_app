try:
    file_handle = open("helo.txt", "r")

    text_content = file_handle.readlines()

    for line in text_content:
        print(f"my name is {line}")

except FileNotFoundError as whoops:
    print(f"Sorry, could not find the file: {whoops}")

except Exception as whoops:
    print(f"unexpected error: {whoops}")
