# master loop function
def master_loop_function(products_list):
    print("\n\nHello and welcome to Brendon's coffee shop")
    print(menu_choice)
    menu_choice = input_function(exit_app, product_menu)
    if menu_choice == 1:
        product_loop(products_list)
    elif menu_choice == 0:
        print("\nUntil next time, Bye!\n")
        exit


master_loop_function(PRODUCTS)
