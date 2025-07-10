products = []

orders = []

order_status = ["preparing", "ready for pick up", "enroute", "delivered"]

couriers = []

## Persistence functions


# ingestion function
def ingest_function(prodlist, courlist):
    temp_prod_list = prodlist
    temp_cour_list = courlist
    with open(
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week3/data/products2.txt",
        "r",
    ) as read_object:
        for line in read_object.readlines():
            temp_prod_list.append(line.rstrip("\n"))
        prodlist = temp_prod_list
    with open(
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week3/data/couriers2.txt",
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
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week3/data/products2.txt",
        "w",
    ) as write_object:
        for line in temp_prod_list[:-1]:
            write_object.write(f"{line}\n")
        write_object.write(temp_prod_list[-1])
    with open(
        "/Users/brendon/Documents/Data-Engineering/brendon-portfolio/mini-project/week3/data/couriers2.txt",
        "w",
    ) as write_object:
        for line in temp_cour_list[:-1]:
            write_object.write(f"{line}\n")
        write_object.write(temp_cour_list[-1])
