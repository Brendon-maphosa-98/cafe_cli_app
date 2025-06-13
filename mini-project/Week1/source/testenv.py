test_list = ["Mocha","tea","coffee"]

#def print_prod_names():
    #for item in test_list:
        #print(f"{} {item}")

def testfunc():
    for item in test_list:
        itemnum = test_list.index(f"{item}") + 1
        print(f"{itemnum} {item}")
testfunc()