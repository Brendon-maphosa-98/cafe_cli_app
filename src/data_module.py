import csv

# In-memory data stores
products = []  # List of product dicts: {"name": str, "price": float}
orders = []  # List of order dicts: {order_num: {order_details}}
order_status = [  # Valid statuses for orders
    "preparing",
    "ready for pick up",
    "enroute",
    "delivered",
]
couriers = []  # List of courier dicts: {"name": str, "phone_number": str}

## Persistence functions


def ingest_function(prodlist, courlist, orderslist):
    """
    Load data from CSV files into the provided lists.
    - products3.csv → prodlist
    - couriers3.csv → courlist
    - orders3.csv → orderslist
    """
    # Use the passed-in lists as temporary buffers
    temp_prod_list = prodlist
    temp_cour_list = courlist
    temp_orders_list = orderslist

    # Read products CSV, append each row as a dict to temp_prod_list
    with open("mini-project/week4/data/products3.csv", "r") as read_object:
        for row in csv.DictReader(read_object):
            temp_prod_list.append({"name": row["name"], "price": float(row["price"])})
    # Assign back (not strictly needed since list is mutable)
    prodlist = temp_prod_list

    # Read couriers CSV, append each row as a dict to temp_cour_list
    with open("mini-project/week4/data/couriers3.csv", "r") as read_object:
        for row in csv.DictReader(read_object):
            temp_cour_list.append(
                {"name": row["name"], "phone_number": row["phone_number"]}
            )
    courlist = temp_cour_list

    # Read orders CSV, convert each row into a nested dict and append
    with open("mini-project/week4/data/orders3.csv", "r") as read_object:
        for row in csv.DictReader(read_object):
            temp_orders_list.append(
                {
                    int(row["order_num"]): {
                        "customer_name": row["customer_name"],
                        "customer_address": row["customer_address"],
                        "customer_phone": row["customer_phone"],
                        "courier": row["courier"],
                        "status": row["status"],
                        "items": row["items"],
                    }
                }
            )
    orderslist = temp_orders_list
    # After calling this function, products, couriers, and orders lists are populated


def persistence_function(prodlist, courlist, orderslist):
    """
    Write the in-memory lists back out to their respective CSV files.
    - products3.csv ← prodlist
    - couriers3.csv ← courlist
    - orders3.csv ← orderslist
    """
    # Write products back to CSV
    with open("mini-project/week4/data/products3.csv", "w") as write_object:
        fieldnames = ["name", "price"]
        writer = csv.DictWriter(write_object, fieldnames=fieldnames)
        writer.writeheader()
        for product in prodlist:
            writer.writerow(product)

    # Write couriers back to CSV
    with open("mini-project/week4/data/couriers3.csv", "w") as write_object:
        fieldnames = ["name", "phone_number"]
        writer = csv.DictWriter(write_object, fieldnames=fieldnames)
        writer.writeheader()
        for courier in courlist:
            writer.writerow(courier)

    # Write orders back to CSV
    with open("mini-project/week4/data/orders3.csv", "w") as write_object:
        fieldnames = [
            "order_num",
            "customer_name",
            "customer_address",
            "customer_phone",
            "courier",
            "status",
            "items",
        ]
        writer = csv.DictWriter(write_object, fieldnames=fieldnames)
        writer.writeheader()
        # Each order is a dict with a single key: the order number
        for order_dict in orderslist:
            for order_num, details in order_dict.items():
                new_row = {
                    "order_num": order_num,
                    "customer_name": details["customer_name"],
                    "customer_address": details["customer_address"],
                    "customer_phone": details["customer_phone"],
                    "courier": details["courier"],
                    "status": details["status"],
                    "items": details["items"],
                }
                writer.writerow(new_row)
