# function holding messege for returning to the previous menu


def rtrn_opt():
    rtrn = int(input("-----------------\n\nInput 0 to return to the previous menu\n\n"))
    if rtrn == 0:
        return rtrn
    else:
        print("\nThats an invalid option, please try again\n")
        rtrn_opt()


# product loop function


def product_loop(products_list):
    Menu_choice = input_function(
        Main_menu, view_option, create_option, update_option, remove_option
    )
    if Menu_choice == 1:
        list_output(products_list)
        return_choice = rtrn_opt()
        while return_choice == 0:
            product_loop(products_list)
            return_choice += 1
    elif Menu_choice == 2:
        products_list = new_product(created_product, products_list)
        return_choice = rtrn_opt()
        while return_choice == 0:
            product_loop(products_list)
            return_choice += 1
    elif Menu_choice == 3:
        products_list = update_item(
            remove_product,
            replacement_product,
            list_output(products_list),
            products_list,
        )
        return_choice = rtrn_opt()
        while return_choice == 0:
            product_loop(products_list)
            return_choice += 1
    elif Menu_choice == 4:
        products_list = del_item(
            remove_product, list_output(products_list), products_list
        )
        return_choice = rtrn_opt()
        while return_choice == 0:
            product_loop(products_list)
            return_choice += 1
    elif Menu_choice == 0:
        master_loop_function(products_list)
    else:
        print("\nInvalid input, try again\n")
        product_loop(products_list)
