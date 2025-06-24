# file = open("people.txt", "w")
# file.write("Susan")
# file.close()
# print("hello everyone")

with open("hello.txt", "r") as file_handle:
    text_content = file_handle.read()
    print(f"text = {text_content}")
