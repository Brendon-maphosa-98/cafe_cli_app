orders = [
    {
        "order1": {
            "customer_name": "Alice Smith",
            "customer_address": "High Road, MANCHESTER",
            "customer_phone": "07123456789",
            "status": "ready for pickup",
            "item(s)_ordered": ["Latte", "Blueberry Muffin"],
        }
    },
    {
        "order2": {
            "customer_name": "James Carter",
            "customer_address": "Oak Street, LIVERPOOL",
            "customer_phone": "07234567890",
            "status": "preparing",
            "item(s)_ordered": ["Flat White", "Croissant"],
        }
    },
    {
        "order3": {
            "customer_name": "Laura Green",
            "customer_address": "Maple Avenue, SHEFFIELD",
            "customer_phone": "07345678901",
            "status": "delivered",
            "item(s)_ordered": ["Americano", "Cold Brew", "Blueberry Muffin"],
        }
    },
]
"""
change_selection1 = int(
    input(
        "Which order would like to update the status for? input the number for the associated order > "
    )
)

order_status = ["preparing", "ready for pick up", "enroute", "delivered"]

change_selection2 = int(
    input(
        f"whats the number associated with the status you would like to update {orders[change_selection1].keys()} to?"
    )
)
"""
"""
orders = [
    {
        "order1": {
            "customer_name": "Alice Smith",
            "customer_address": "High Road, MANCHESTER",
            "customer_phone": "07123456789",
            "status": "ready for pickup",
            "item(s)_ordered": ["Latte", "Blueberry Muffin"],
        }
    },
    {
        "order2": {
            "customer_name": "James Carter",
            "customer_address": "Oak Street, LIVERPOOL",
            "customer_phone": "07234567890",
            "status": "preparing",
            "item(s)_ordered": ["Flat White", "Croissant"],
        }
    },
    {
        "order3": {
            "customer_name": "Laura Green",
            "customer_address": "Maple Avenue, SHEFFIELD",
            "customer_phone": "07345678901",
            "status": "delivered",
            "item(s)_ordered": ["Americano", "Cold Brew", "Blueberry Muffin"],
        }
    },
]
"""
"""
product_menu = "Go to the products menu\n"


def input_function(*input_str):
    index_num = 1
    for choice in input_str:
        print(f"{index_num}. {choice}")
    returned_input = int(
        input("\nWhich of the above options would you like to select?\n")
    )
    return returned_input


def rtrn_opt():
    rtrn = int(input("\nInput 0 to return to the previous menu\n\n"))
    if rtrn == 0:
        return rtrn
    else:
        print("\nThats an invalid option, please try again\n")
        rtrn_opt()


print(rtrn_opt())
"""

products_data = {1: "Hellow", 2: "Bye"}

input = int(input("select item number "))

print((products_data[input - 1]))
