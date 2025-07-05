from input_output_module import input_function
import stringVariable_module as stng
from data_module import PRODUCTS
import loops_module as loop


# master loop function
def master_loop_function(products_list):

    print("\n\nHello and welcome to Brendon's coffee shop")
    print(stng.menu_choice)
    choice = input_function(stng.exit_app, stng.product_menu)
    if choice == 1:
        loop.product_loop(products_list)
    elif choice == 0:
        print("\nUntil next time, Bye!\n")
        exit()
    else:
        print("Thats not a valid input, please try again")
        master_loop_function(products_list)


master_loop_function(PRODUCTS)
