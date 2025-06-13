list_var = []

def add_to_list():
    with open("/Users/brendon/Documents/Data Engineering/brendon-portfolio/mini-project/Week1/data/test.txt", "r") as test:
        return test.read().split(",")

list_var = add_to_list()

print(list_var)