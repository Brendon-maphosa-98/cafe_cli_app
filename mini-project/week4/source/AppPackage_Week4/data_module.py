import csv

products = []

orders = []

order_status = ["preparing", "ready for pick up", "enroute", "delivered"]

couriers = []

## Persistence functions


# ingestion function
def ingest_function(prodlist, courlist,orderslist):
    temp_prod_list = prodlist
    temp_cour_list = courlist
    with open(
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week4/data/products3.csv",
        "r",
    ) as read_object:
        for line in read_object.readlines():
            temp_prod_list.append(line.rstrip("\n"))
        prodlist = temp_prod_list
    with open(
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week4/data/couriers3.csv",
        "r",
    ) as read_object:
        for line in read_object.readlines():
            temp_cour_list.append(line.rstrip("\n"))
        prodlist = temp_cour_list
    with open("/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week4/data/orders3.csv", "r") as read_object:
            pass


# persistence function
def persistence_function(prodlist, courlist,orderslist):
    temp_prod_list = prodlist
    temp_cour_list = courlist
    temp_orders_list = orderslist
    with open(
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week4/data/products3.csv",
        "w",
    ) as write_object:
        for line in temp_prod_list[:-1]:
            write_object.write(f"{line}\n")
        write_object.write(temp_prod_list[-1])
    with open(
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week4/data/couriers3.csv",
        "w",
    ) as write_object:
        for line in temp_cour_list[:-1]:
            write_object.write(f"{line}\n")
        write_object.write(temp_cour_list[-1])
    with open("/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week4/data/orders3.csv", "r") as write_object:
        pass