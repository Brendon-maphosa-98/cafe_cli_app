import input_output_module as io
import stringVariable_module as stng
import product_menu_module as prodmenu

# import masterLoop_module as master

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
    import masterLoop_module as master

    Menu_choice = io.input_function(
        stng.Main_menu,
        stng.view_option,
        stng.create_option,
        stng.update_option,
        stng.remove_option,
    )
    if Menu_choice == 1:
        io.list_output(products_list)
        return_choice = rtrn_opt()
        while return_choice == 0:
            product_loop(products_list)
            return_choice += 1
    elif Menu_choice == 2:
        products_list = prodmenu.new_product(stng.created_product, products_list)
        return_choice = rtrn_opt()
        while return_choice == 0:
            product_loop(products_list)
            return_choice += 1
    elif Menu_choice == 3:
        products_list = prodmenu.update_item(
            stng.remove_product,
            stng.replacement_product,
            io.list_output(products_list),
            products_list,
        )
        return_choice = rtrn_opt()
        while return_choice == 0:
            product_loop(products_list)
            return_choice += 1
    elif Menu_choice == 4:
        products_list = prodmenu.del_item(
            stng.remove_product, io.list_output(products_list), products_list
        )
        return_choice = rtrn_opt()
        while return_choice == 0:
            product_loop(products_list)
            return_choice += 1
    elif Menu_choice == 0:
        print("menu choice option")
        master.master_loop_function(products_list)
    else:
        print("\nInvalid input, try again\n")
        product_loop(products_list)


# Orders loop function
