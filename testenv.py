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
selected_item_index = []
list = [
    {1: {"Product": "Espresso", "Price": "1.50"}},
    {2: {"Product": "Cappuccino", "Price": "2.50"}},
    {3: {"Product": "Latte", "Price": "2.75"}},
    {4: {"Product": "Americano", "Price": "2.00"}},
    {5: {"Product": "Mocha", "Price": "3.00"}},
    {6: {"Product": "Iced Coffee", "Price": "2.80"}},
    {7: {"Product": "Flat White", "Price": "2.60"}},
    {8: {"Product": "Hot Brew", "Price": "2.20"}},
    {9: {"Product": "Croissant", "Price": "1.80"}},
    {10: {"Product": "Blueberry Muffin", "Price": "2.10"}},
    {11: {"Product": "White Bread", "Price": "1.40"}},
    {12: {"Product": "Cheese", "Price": "2.30"}},
    {13: {"Product": "Brown bread", "Price": "1.60"}},
]
"""
num = "5, 8, 10, 13"
print(num)
num = num.split(",")
print(num)
num.remove("5")
print(num)
print(type(num))
num = str(num)
print(num)
print(type(num))
num = num.strip("[").strip("]").replace("'", "").strip()
num = num.replace("  ", " ")
print(num)
print(len(num))
# for x in num:
#    print(x)
"""


def master():
    choice = input("Enter option (0 to exit): ")
    if choice == "0":
        exit()
    else:
        master()  # ⚠️ calls itself again


master()
