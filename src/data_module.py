products = []


orders = [
    {
        "order1": {
            "customer_name": "Alice Smith",
            "customer_address": "High Road, MANCHESTER",
            "customer_phone": "07123456789",
            "status": "ready for pickup",
            "courier": "John",
            "item(s)_ordered": ["Latte", "Blueberry Muffin"],
        }
    },
    {
        "order2": {
            "customer_name": "James Carter",
            "customer_address": "Oak Street, LIVERPOOL",
            "customer_phone": "07234567890",
            "status": "preparing",
            "courier": "Alice",
            "item(s)_ordered": ["Flat White", "Croissant"],
        }
    },
    {
        "order3": {
            "customer_name": "Laura Green",
            "customer_address": "Maple Avenue, SHEFFIELD",
            "customer_phone": "07345678901",
            "status": "delivered",
            "courier": "Michael",
            "item(s)_ordered": ["Americano", "Cold Brew", "Blueberry Muffin"],
        }
    },
]

order_status = ["preparing", "ready for pick up", "enroute", "delivered"]

couriers = []

## Persistence functions


# ingestion function
def ingest_function(prodlist, courlist):
    temp_prod_list = prodlist
    temp_cour_list = courlist
    with open(
        "./data/products.txt",
        "r",
    ) as read_object:
        for line in read_object.readlines():
            temp_prod_list.append(line.rstrip("\n"))
        prodlist = temp_prod_list
    with open(
        "./data/couriers.txt",
        "r",
    ) as read_object:
        for line in read_object.readlines():
            temp_cour_list.append(line.rstrip("\n"))
        prodlist = temp_cour_list


# persistence function
def persistence_function(prodlist, courlist):
    temp_prod_list = prodlist
    temp_cour_list = courlist
    with open(
        "./data/products.txt",
        "w",
    ) as write_object:
        for line in temp_prod_list[:-1]:
            write_object.write(f"{line}\n")
        write_object.write(temp_prod_list[-1])
    with open(
        "./data/couriers.txt",
        "w",
    ) as write_object:
        for line in temp_cour_list[:-1]:
            write_object.write(f"{line}\n")
        write_object.write(temp_cour_list[-1])
